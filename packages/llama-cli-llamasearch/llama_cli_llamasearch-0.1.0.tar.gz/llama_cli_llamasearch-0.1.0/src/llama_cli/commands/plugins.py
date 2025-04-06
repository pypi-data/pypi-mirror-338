"""
Plugin management commands for Llama CLI
"""
import os
import sys
import shutil
from pathlib import Path
from typing import Dict, Any, List, Optional

import typer
from rich.prompt import Prompt, Confirm

from llama_cli.config import load_config, save_config
from llama_cli.utils.output import get_console, print_success, print_error, print_warning, print_output

# Create the plugins app
app = typer.Typer(help="Plugin management")
console = get_console()

# Plugins directory
PLUGINS_DIR = os.path.expanduser("~/.config/llama/plugins")


@app.command("list")
def list_plugins(
    output_format: str = typer.Option(
        "table", "--format", "-f", help="Output format (json, yaml, table)"
    ),
):
    """
    List installed plugins
    
    Example:
        llama plugins list
        llama plugins list --format json
    """
    # Ensure plugins directory exists
    os.makedirs(PLUGINS_DIR, exist_ok=True)
    
    # Get installed plugins
    plugins = []
    for plugin_dir in os.listdir(PLUGINS_DIR):
        plugin_path = os.path.join(PLUGINS_DIR, plugin_dir)
        if os.path.isdir(plugin_path):
            # Check for metadata
            metadata_path = os.path.join(plugin_path, "plugin.json")
            metadata = {}
            if os.path.exists(metadata_path):
                try:
                    import json
                    with open(metadata_path, "r") as f:
                        metadata = json.load(f)
                except Exception:
                    pass
            
            plugins.append({
                "Name": plugin_dir,
                "Version": metadata.get("version", "Unknown"),
                "Description": metadata.get("description", "No description"),
                "Author": metadata.get("author", "Unknown"),
            })
    
    if not plugins:
        print_warning("No plugins installed")
        console.print("\nInstall plugins with [bold]llama plugins install <plugin-name>[/]")
        return
    
    print_output(plugins, output_format, title="Installed Plugins")


@app.command("install")
def install_plugin(
    plugin_name: str = typer.Argument(..., help="Plugin name or GitHub repository URL"),
    version: Optional[str] = typer.Option(
        None, "--version", "-v", help="Plugin version to install"
    ),
    force: bool = typer.Option(
        False, "--force", help="Force reinstall if already installed"
    ),
):
    """
    Install a plugin
    
    Example:
        llama plugins install llamasearch-plugin-example
        llama plugins install https://github.com/llamasearch/llama-plugin-example
        llama plugins install llamasearch-plugin-example --version 1.0.0
        llama plugins install llamasearch-plugin-example --force
    """
    # Ensure plugins directory exists
    os.makedirs(PLUGINS_DIR, exist_ok=True)
    
    # Get plugin name from URL if needed
    if plugin_name.startswith(("http://", "https://")):
        # Extract plugin name from URL
        import re
        match = re.search(r'/([^/]+)/?$', plugin_name)
        if match:
            plugin_dir_name = match.group(1)
            # Remove .git suffix if present
            if plugin_dir_name.endswith(".git"):
                plugin_dir_name = plugin_dir_name[:-4]
        else:
            print_error("Invalid plugin URL format")
            return
    else:
        plugin_dir_name = plugin_name
    
    # Check if plugin is already installed
    plugin_path = os.path.join(PLUGINS_DIR, plugin_dir_name)
    if os.path.exists(plugin_path) and not force:
        overwrite = Confirm.ask(
            f"Plugin '{plugin_dir_name}' is already installed. Reinstall?",
            default=False,
        )
        if not overwrite:
            console.print("Plugin installation cancelled")
            return
        
        # Remove existing plugin
        try:
            shutil.rmtree(plugin_path)
        except Exception as e:
            print_error(f"Failed to remove existing plugin: {e}")
            return
    
    # Install plugin
    console.print(f"Installing plugin '{plugin_dir_name}'...")
    
    try:
        # Clone repository if URL provided
        if plugin_name.startswith(("http://", "https://")):
            import subprocess
            
            # Clone repository
            if version:
                # Clone specific version (tag)
                subprocess.run(
                    ["git", "clone", "--branch", version, "--depth", "1", plugin_name, plugin_path],
                    check=True,
                )
            else:
                # Clone latest version
                subprocess.run(
                    ["git", "clone", "--depth", "1", plugin_name, plugin_path],
                    check=True,
                )
        else:
            # TODO: Implement plugin installation from PyPI or other sources
            # For now, create a placeholder directory
            os.makedirs(plugin_path, exist_ok=True)
            with open(os.path.join(plugin_path, "plugin.json"), "w") as f:
                import json
                json.dump({
                    "name": plugin_dir_name,
                    "version": version or "0.1.0",
                    "description": "Plugin installed via placeholder",
                    "author": "Manual installation",
                }, f, indent=2)
            
            print_warning("Plugin installation from name is not fully implemented")
            print_warning("A placeholder plugin has been created")
        
        print_success(f"Plugin '{plugin_dir_name}' installed successfully")
    except Exception as e:
        print_error(f"Failed to install plugin: {e}")
        
        # Clean up
        if os.path.exists(plugin_path):
            try:
                shutil.rmtree(plugin_path)
            except Exception:
                pass


@app.command("uninstall")
def uninstall_plugin(
    plugin_name: str = typer.Argument(..., help="Plugin name"),
    force: bool = typer.Option(
        False, "--force", help="Skip confirmation"
    ),
):
    """
    Uninstall a plugin
    
    Example:
        llama plugins uninstall llamasearch-plugin-example
        llama plugins uninstall llamasearch-plugin-example --force
    """
    # Ensure plugins directory exists
    os.makedirs(PLUGINS_DIR, exist_ok=True)
    
    # Check if plugin is installed
    plugin_path = os.path.join(PLUGINS_DIR, plugin_name)
    if not os.path.exists(plugin_path):
        print_error(f"Plugin '{plugin_name}' is not installed")
        return
    
    # Confirm uninstallation
    if not force:
        confirm = Confirm.ask(
            f"Are you sure you want to uninstall plugin '{plugin_name}'?",
            default=False,
        )
        if not confirm:
            console.print("Plugin uninstallation cancelled")
            return
    
    # Uninstall plugin
    try:
        shutil.rmtree(plugin_path)
        print_success(f"Plugin '{plugin_name}' uninstalled successfully")
    except Exception as e:
        print_error(f"Failed to uninstall plugin: {e}")


@app.command("update")
def update_plugin(
    plugin_name: str = typer.Argument(..., help="Plugin name"),
    version: Optional[str] = typer.Option(
        None, "--version", "-v", help="Plugin version to update to"
    ),
):
    """
    Update a plugin
    
    Example:
        llama plugins update llamasearch-plugin-example
        llama plugins update llamasearch-plugin-example --version 1.1.0
    """
    # Ensure plugins directory exists
    os.makedirs(PLUGINS_DIR, exist_ok=True)
    
    # Check if plugin is installed
    plugin_path = os.path.join(PLUGINS_DIR, plugin_name)
    if not os.path.exists(plugin_path):
        print_error(f"Plugin '{plugin_name}' is not installed")
        return
    
    # Check if plugin has a Git repository
    git_dir = os.path.join(plugin_path, ".git")
    if not os.path.exists(git_dir):
        print_error(f"Plugin '{plugin_name}' is not a Git repository and cannot be updated")
        return
    
    # Update plugin
    console.print(f"Updating plugin '{plugin_name}'...")
    
    try:
        import subprocess
        
        # Change to plugin directory
        cwd = os.getcwd()
        os.chdir(plugin_path)
        
        if version:
            # Update to specific version (tag)
            subprocess.run(
                ["git", "fetch", "--tags"],
                check=True,
            )
            subprocess.run(
                ["git", "checkout", version],
                check=True,
            )
        else:
            # Update to latest version
            subprocess.run(
                ["git", "pull"],
                check=True,
            )
        
        # Restore working directory
        os.chdir(cwd)
        
        print_success(f"Plugin '{plugin_name}' updated successfully")
    except Exception as e:
        # Restore working directory
        if 'cwd' in locals():
            os.chdir(cwd)
        
        print_error(f"Failed to update plugin: {e}")


@app.command("info")
def plugin_info(
    plugin_name: str = typer.Argument(..., help="Plugin name"),
    output_format: str = typer.Option(
        "table", "--format", "-f", help="Output format (json, yaml, table)"
    ),
):
    """
    Show plugin information
    
    Example:
        llama plugins info llamasearch-plugin-example
        llama plugins info llamasearch-plugin-example --format json
    """
    # Ensure plugins directory exists
    os.makedirs(PLUGINS_DIR, exist_ok=True)
    
    # Check if plugin is installed
    plugin_path = os.path.join(PLUGINS_DIR, plugin_name)
    if not os.path.exists(plugin_path):
        print_error(f"Plugin '{plugin_name}' is not installed")
        return
    
    # Get plugin metadata
    metadata_path = os.path.join(plugin_path, "plugin.json")
    metadata = {}
    if os.path.exists(metadata_path):
        try:
            import json
            with open(metadata_path, "r") as f:
                metadata = json.load(f)
        except Exception as e:
            print_warning(f"Failed to read plugin metadata: {e}")
    
    # Check if plugin has a Git repository
    git_dir = os.path.join(plugin_path, ".git")
    if os.path.exists(git_dir):
        try:
            import subprocess
            
            # Get Git information
            cwd = os.getcwd()
            os.chdir(plugin_path)
            
            # Get current branch/tag
            branch_proc = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
            )
            branch = branch_proc.stdout.strip()
            
            # Get latest commit
            commit_proc = subprocess.run(
                ["git", "log", "-1", "--format=%h %s"],
                capture_output=True,
                text=True,
                check=True,
            )
            commit = commit_proc.stdout.strip()
            
            # Get remote URL
            remote_proc = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True,
                text=True,
                check=False,
            )
            remote = remote_proc.stdout.strip() if remote_proc.returncode == 0 else "Unknown"
            
            # Restore working directory
            os.chdir(cwd)
            
            metadata["git"] = {
                "branch": branch,
                "commit": commit,
                "remote": remote,
            }
        except Exception as e:
            # Restore working directory
            if 'cwd' in locals():
                os.chdir(cwd)
            
            print_warning(f"Failed to get Git information: {e}")
    
    # Display plugin information
    if output_format in ["json", "yaml"]:
        print_output(metadata, output_format, title=f"Plugin: {plugin_name}")
    else:
        console.print(f"\n[bold]Plugin:[/] [bold cyan]{plugin_name}[/]")
        console.print(f"[bold]Version:[/] {metadata.get('version', 'Unknown')}")
        console.print(f"[bold]Description:[/] {metadata.get('description', 'No description')}")
        console.print(f"[bold]Author:[/] {metadata.get('author', 'Unknown')}")
        
        if "git" in metadata:
            console.print("\n[bold]Git Information:[/]")
            console.print(f"  [bold]Branch:[/] {metadata['git']['branch']}")
            console.print(f"  [bold]Commit:[/] {metadata['git']['commit']}")
            console.print(f"  [bold]Remote:[/] {metadata['git']['remote']}")
        
        if "commands" in metadata:
            console.print("\n[bold]Commands:[/]")
            for command in metadata["commands"]:
                console.print(f"  [bold cyan]{command['name']}[/] - {command.get('description', 'No description')}")
        
        console.print("")


@app.command("create")
def create_plugin(
    plugin_name: str = typer.Argument(..., help="Plugin name"),
    output_dir: str = typer.Option(
        ".", "--output", "-o", help="Output directory"
    ),
    description: Optional[str] = typer.Option(
        None, "--description", "-d", help="Plugin description"
    ),
    author: Optional[str] = typer.Option(
        None, "--author", "-a", help="Plugin author"
    ),
):
    """
    Create a new plugin template
    
    Example:
        llama plugins create my-plugin
        llama plugins create my-plugin --output ~/projects
        llama plugins create my-plugin --description "My awesome plugin" --author "Your Name"
    """
    # Sanitize plugin name
    import re
    plugin_dir_name = re.sub(r'[^a-zA-Z0-9_-]', '-', plugin_name)
    
    # Create output directory
    plugin_path = os.path.join(os.path.expanduser(output_dir), plugin_dir_name)
    if os.path.exists(plugin_path):
        overwrite = Confirm.ask(
            f"Directory '{plugin_path}' already exists. Overwrite?",
            default=False,
        )
        if not overwrite:
            console.print("Plugin creation cancelled")
            return
        
        # Remove existing directory
        try:
            shutil.rmtree(plugin_path)
        except Exception as e:
            print_error(f"Failed to remove existing directory: {e}")
            return
    
    # Create plugin directory
    os.makedirs(plugin_path, exist_ok=True)
    
    # Create plugin structure
    try:
        # Create plugin.json
        import json
        with open(os.path.join(plugin_path, "plugin.json"), "w") as f:
            json.dump({
                "name": plugin_name,
                "version": "0.1.0",
                "description": description or f"LlamaSearch.ai CLI plugin: {plugin_name}",
                "author": author or "LlamaSearch.ai",
                "commands": [
                    {
                        "name": "example",
                        "description": "Example command added by the plugin",
                    }
                ]
            }, f, indent=2)
        
        # Create plugin package
        package_dir = os.path.join(plugin_path, "llama_plugin")
        os.makedirs(package_dir, exist_ok=True)
        
        # Create __init__.py
        with open(os.path.join(package_dir, "__init__.py"), "w") as f:
            f.write(f"""\"\"\"
{plugin_name} - LlamaSearch.ai CLI plugin
\"\"\"

__version__ = "0.1.0"
""")
        
        # Create plugin.py
        with open(os.path.join(package_dir, "plugin.py"), "w") as f:
            f.write(f"""\"\"\"
Plugin implementation for {plugin_name}
\"\"\"
import os
import sys
import typer
from rich.console import Console

app = typer.Typer(help="{description or f'LlamaSearch.ai CLI plugin: {plugin_name}'}")
console = Console()


@app.command("example")
def example_command():
    \"\"\"
    Example command added by the plugin
    \"\"\"
    console.print("[bold green]Hello from the plugin![/]")
    console.print("This is an example command added by the plugin.")
    console.print("Customize this command or add new ones in [bold]plugin.py[/]")


def get_commands():
    \"\"\"
    Return the plugin commands
    
    Returns:
        dict: Plugin commands
    \"\"\"
    return {{
        "example": app
    }}
""")
        
        # Create setup.py
        with open(os.path.join(plugin_path, "setup.py"), "w") as f:
            f.write(f"""#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="{plugin_name}",
    version="0.1.0",
    description="{description or f'LlamaSearch.ai CLI plugin: {plugin_name}'}",
    author="{author or 'LlamaSearch.ai'}",
    packages=find_packages(),
    install_requires=[
        "typer>=0.4.0",
        "rich>=10.0.0",
    ],
    entry_points={{
        "llama_cli.plugins": [
            "{plugin_name}=llama_plugin.plugin:get_commands",
        ],
    }},
)
""")
        
        # Create README.md
        with open(os.path.join(plugin_path, "README.md"), "w") as f:
            f.write(f"""# {plugin_name}

{description or f'LlamaSearch.ai CLI plugin: {plugin_name}'}

## Installation

```bash
# Install from the plugin directory
cd {plugin_path}
pip install -e .

# Or install using the llama CLI
llama plugins install {plugin_path}
```

## Usage

```bash
# Run the example command
llama example

# Get help for the example command
llama example --help
```

## Development

This plugin was created with the `llama plugins create` command. To modify it:

1. Edit `llama_plugin/plugin.py` to add or modify commands
2. Update `plugin.json` with metadata about your plugin
3. Install the plugin in development mode: `pip install -e .`

""")
        
        # Create .gitignore
        with open(os.path.join(plugin_path, ".gitignore"), "w") as f:
            f.write("""# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo
""")
        
        print_success(f"Plugin template created at {plugin_path}")
        console.print(f"\nNext steps:")
        console.print(f"1. [bold]cd {plugin_path}[/]")
        console.print(f"2. Edit [bold]llama_plugin/plugin.py[/] to add your commands")
        console.print(f"3. Install the plugin: [bold]pip install -e .[/]")
        console.print(f"4. Test your command: [bold]llama example[/]")
    except Exception as e:
        print_error(f"Failed to create plugin template: {e}")
        
        # Clean up
        if os.path.exists(plugin_path):
            try:
                shutil.rmtree(plugin_path)
            except Exception:
                pass 