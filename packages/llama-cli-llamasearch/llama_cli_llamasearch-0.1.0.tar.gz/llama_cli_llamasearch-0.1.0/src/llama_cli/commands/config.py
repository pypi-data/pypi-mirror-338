"""
Configuration commands for Llama CLI
"""
import os
import sys
from typing import Dict, Any, Optional

import typer
import yaml
from rich.prompt import Prompt, Confirm

from llama_cli.config import (
    load_config, 
    save_config, 
    get_config_value, 
    set_config_value,
    get_config_path,
    DEFAULT_CONFIG_DIR,
    DEFAULT_CONFIG_FILE,
)
from llama_cli.utils.output import (
    get_console, 
    print_success, 
    print_error, 
    print_warning,
    print_output,
)

# Create the config app
app = typer.Typer(help="Configuration management")
console = get_console()


@app.command("get")
def get(
    key: str = typer.Argument(..., help="Configuration key (dot notation supported)"),
    profile: Optional[str] = typer.Option(
        None, "--profile", "-p", help="Profile name to get configuration from"
    ),
    output_format: str = typer.Option(
        "table", "--format", "-f", help="Output format (json, yaml, table)"
    ),
):
    """
    Get configuration value
    
    Example:
        llama config get output_format
        llama config get search.max_results
        llama config get api_url --profile dev
    """
    # Load config
    config = load_config()
    
    # Get configuration value
    if profile:
        if "profiles" not in config or profile not in config["profiles"]:
            print_error(f"Profile '{profile}' not found", exit_code=1)
        
        value = get_config_value(key, config["profiles"].get(profile, {}))
    else:
        value = get_config_value(key, config)
    
    if value is not None:
        # Print the value
        if isinstance(value, (dict, list)):
            print_output(value, output_format, title=f"Configuration: {key}")
        else:
            console.print(f"{key} = {value}")
    else:
        print_warning(f"Configuration key '{key}' not found")


@app.command("set")
def set_config(
    key: str = typer.Argument(..., help="Configuration key (dot notation supported)"),
    value: str = typer.Argument(..., help="Configuration value"),
    profile: Optional[str] = typer.Option(
        None, "--profile", "-p", help="Profile name to set configuration for"
    ),
):
    """
    Set configuration value
    
    Example:
        llama config set output_format json
        llama config set search.max_results 100
        llama config set api_url https://dev.api.llamasearch.ai --profile dev
    """
    # Convert value to appropriate type
    if value.lower() == "true":
        parsed_value = True
    elif value.lower() == "false":
        parsed_value = False
    elif value.isdigit():
        parsed_value = int(value)
    elif value.replace(".", "", 1).isdigit() and value.count(".") == 1:
        parsed_value = float(value)
    else:
        try:
            # Try to parse as YAML/JSON
            parsed_value = yaml.safe_load(value)
        except:
            # Use as string
            parsed_value = value
    
    # Set configuration value
    success = set_config_value(key, parsed_value, profile=profile)
    
    if success:
        target = f" for profile '{profile}'" if profile else ""
        print_success(f"Configuration value '{key}' set to '{parsed_value}'{target}")
    else:
        print_error(f"Failed to set configuration value")


@app.command("list")
def list_config(
    profile: Optional[str] = typer.Option(
        None, "--profile", "-p", help="Profile name to list configuration for"
    ),
    output_format: str = typer.Option(
        "table", "--format", "-f", help="Output format (json, yaml, table)"
    ),
):
    """
    List configuration values
    
    Example:
        llama config list
        llama config list --profile dev
        llama config list --format json
    """
    # Load config
    config = load_config()
    
    # Print configuration
    if profile:
        if "profiles" not in config or profile not in config["profiles"]:
            print_error(f"Profile '{profile}' not found", exit_code=1)
        
        title = f"Configuration for profile '{profile}'"
        data = config["profiles"].get(profile, {})
    else:
        # Exclude profiles from main config display to avoid clutter
        data = {k: v for k, v in config.items() if k != "profiles"}
        title = "Global Configuration"
    
    print_output(data, output_format, title=title)


@app.command("init")
def init_config(
    force: bool = typer.Option(
        False, "--force", help="Force overwrite existing configuration"
    ),
):
    """
    Initialize configuration with default values
    
    Example:
        llama config init
        llama config init --force
    """
    from llama_cli.config import initialize_config
    
    # Check if configuration file exists
    if os.path.exists(DEFAULT_CONFIG_FILE) and not force:
        overwrite = Confirm.ask(
            f"Configuration file already exists at {DEFAULT_CONFIG_FILE}. Overwrite?",
            default=False,
        )
        if not overwrite:
            console.print("Configuration initialization cancelled")
            return
    
    # Initialize configuration
    success = initialize_config()
    
    if success:
        print_success(f"Configuration initialized at {DEFAULT_CONFIG_FILE}")
    else:
        print_error("Failed to initialize configuration")


@app.command("path")
def config_path():
    """
    Show configuration file path
    
    Example:
        llama config path
    """
    console.print(f"Configuration file: {get_config_path()}")
    console.print(f"Configuration directory: {DEFAULT_CONFIG_DIR}")


@app.command("edit")
def edit_config():
    """
    Open configuration file in editor
    
    Example:
        llama config edit
    """
    import subprocess
    
    # Ensure config file exists
    if not os.path.exists(DEFAULT_CONFIG_FILE):
        initialize = Confirm.ask(
            f"Configuration file does not exist at {DEFAULT_CONFIG_FILE}. Initialize it?",
            default=True,
        )
        if initialize:
            from llama_cli.config import initialize_config
            initialize_config()
        else:
            console.print("Configuration edit cancelled")
            return
    
    # Get editor from environment or use default
    editor = os.environ.get("EDITOR", "vi")
    
    try:
        subprocess.run([editor, DEFAULT_CONFIG_FILE])
        print_success("Configuration file updated")
    except Exception as e:
        print_error(f"Failed to open editor: {e}")


@app.command("profiles")
def list_profiles(
    output_format: str = typer.Option(
        "table", "--format", "-f", help="Output format (json, yaml, table)"
    ),
):
    """
    List configuration profiles
    
    Example:
        llama config profiles
        llama config profiles --format json
    """
    # Load config
    config = load_config()
    
    # Get profiles
    profiles = config.get("profiles", {})
    default_profile = config.get("default_profile", "default")
    
    if not profiles:
        print_warning("No profiles found")
        return
    
    # Prepare data for output
    profiles_data = []
    for name, data in profiles.items():
        is_default = name == default_profile
        profiles_data.append({
            "Name": name,
            "Default": "Yes" if is_default else "No",
            "API URL": data.get("api_url", "https://api.llamasearch.ai"),
        })
    
    print_output(profiles_data, output_format, title="Configuration Profiles")


@app.command("create-profile")
def create_profile(
    name: str = typer.Argument(..., help="Profile name"),
    api_url: str = typer.Option(
        "https://api.llamasearch.ai", "--api-url", "-u", help="API URL for the profile"
    ),
    set_default: bool = typer.Option(
        False, "--default", help="Set as default profile"
    ),
):
    """
    Create a new configuration profile
    
    Example:
        llama config create-profile dev
        llama config create-profile staging --api-url https://staging.api.llamasearch.ai
        llama config create-profile prod --default
    """
    # Load config
    config = load_config()
    
    # Check if profile already exists
    if "profiles" in config and name in config["profiles"]:
        overwrite = Confirm.ask(
            f"Profile '{name}' already exists. Overwrite?",
            default=False,
        )
        if not overwrite:
            console.print("Profile creation cancelled")
            return
    
    # Create profile
    if "profiles" not in config:
        config["profiles"] = {}
    
    config["profiles"][name] = {"api_url": api_url}
    
    # Set as default if requested
    if set_default:
        config["default_profile"] = name
    
    # Save config
    success = save_config(config)
    
    if success:
        print_success(f"Profile '{name}' created")
        if set_default:
            print_success(f"Profile '{name}' set as default")
    else:
        print_error("Failed to create profile")


@app.command("delete-profile")
def delete_profile(
    name: str = typer.Argument(..., help="Profile name"),
    force: bool = typer.Option(
        False, "--force", help="Skip confirmation"
    ),
):
    """
    Delete a configuration profile
    
    Example:
        llama config delete-profile dev
        llama config delete-profile staging --force
    """
    # Load config
    config = load_config()
    
    # Check if profile exists
    if "profiles" not in config or name not in config["profiles"]:
        print_error(f"Profile '{name}' not found", exit_code=1)
    
    # Check if it's the default profile
    if name == config.get("default_profile"):
        print_warning(f"'{name}' is the default profile")
        if not force:
            confirm = Confirm.ask(
                "Deleting the default profile will reset to 'default'. Continue?",
                default=False,
            )
            if not confirm:
                console.print("Profile deletion cancelled")
                return
        config["default_profile"] = "default"
    
    # Confirm deletion
    if not force:
        confirm = Confirm.ask(
            f"Are you sure you want to delete profile '{name}'?",
            default=False,
        )
        if not confirm:
            console.print("Profile deletion cancelled")
            return
    
    # Delete profile
    del config["profiles"][name]
    
    # Save config
    success = save_config(config)
    
    if success:
        print_success(f"Profile '{name}' deleted")
    else:
        print_error("Failed to delete profile")


@app.command("default-profile")
def set_default_profile(
    name: str = typer.Argument(..., help="Profile name"),
):
    """
    Set the default configuration profile
    
    Example:
        llama config default-profile prod
    """
    # Load config
    config = load_config()
    
    # Check if profile exists
    if "profiles" not in config or name not in config["profiles"]:
        print_error(f"Profile '{name}' not found", exit_code=1)
    
    # Set default profile
    config["default_profile"] = name
    
    # Save config
    success = save_config(config)
    
    if success:
        print_success(f"Profile '{name}' set as default")
    else:
        print_error("Failed to set default profile") 