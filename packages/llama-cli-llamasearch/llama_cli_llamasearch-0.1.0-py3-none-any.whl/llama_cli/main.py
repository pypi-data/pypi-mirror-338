#!/usr/bin/env python3
"""
Llama CLI - Command-line interface for LlamaSearch.ai tools
"""
import os
import sys
from typing import Optional, List

import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from llama_cli import __version__
from llama_cli.commands import (
    auth,
    config,
    search,
    db,
    kv,
    api,
    pdf,
    analytics,
    shell,
    plugins,
)
from llama_cli.config import load_config
from llama_cli.utils.output import get_console

# Create the main CLI app
app = typer.Typer(
    name="llama",
    help="Command-line interface for LlamaSearch.ai tools",
    add_completion=False,
)

# Add all command groups
app.add_typer(auth.app, name="auth")
app.add_typer(config.app, name="config")
app.add_typer(search.app, name="search")
app.add_typer(db.app, name="db")
app.add_typer(kv.app, name="kv")
app.add_typer(api.app, name="api")
app.add_typer(pdf.app, name="pdf")
app.add_typer(analytics.app, name="analytics")
app.add_typer(plugins.app, name="plugins")

console = get_console()


def version_callback(value: bool):
    """Print version information and exit"""
    if value:
        console.print(f"Llama CLI version: {__version__}")
        raise typer.Exit()


def print_banner():
    """Print the Llama CLI banner"""
    banner = Text()
    banner.append("\n")
    banner.append("    ██       ██                                 ██████  ██      ██ \n", "yellow")
    banner.append("    ██       ██                                ██    ██ ██      ██ \n", "yellow") 
    banner.append("    ██       ██   ████   ████████████   ████  ██       ██      ██ \n", "yellow")
    banner.append("    ██       ██ ██    ██ ██    ██    ██     ██ ██       ██      ██ \n", "yellow")
    banner.append("    ██       ██ ████████ ██    ██    ██  █████ ██       ██      ██ \n", "yellow")
    banner.append("    ██       ██ ██       ██    ██    ██ ██  ██ ██       ██      ██ \n", "yellow")
    banner.append("    ███████  ██  ██████  ██    ██    ██  ██████ ██    ██ ██      ██ \n", "yellow")
    banner.append("    ███████  ██           ████  ████             ██████  ████████  \n", "yellow")
    banner.append("\n")
    banner.append(f"LlamaSearch.ai CLI v{__version__}", "cyan")
    banner.append(" - Command-line interface for LlamaSearch.ai tools\n\n", "bright_black")
    
    console.print(Panel(banner, border_style="yellow", padding=(1, 2)))


@app.callback()
def main(
    ctx: typer.Context,
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", callback=version_callback, is_eager=True, 
        help="Show version information and exit"
    ),
    config_file: Optional[str] = typer.Option(
        None, "--config", "-c", help="Path to configuration file"
    ),
    profile: Optional[str] = typer.Option(
        None, "--profile", "-p", help="Configuration profile to use"
    ),
    verbose: bool = typer.Option(
        False, "--verbose", help="Enable verbose output"
    ),
    quiet: bool = typer.Option(
        False, "--quiet", help="Suppress informational output"
    ),
    output_format: Optional[str] = typer.Option(
        None, "--format", "-f", help="Output format (json, yaml, table, csv)"
    ),
    show_banner: bool = typer.Option(
        True, "--no-banner/--banner", help="Show/hide the banner"
    ),
):
    """
    Command-line interface for LlamaSearch.ai tools
    
    Run 'llama --help' to see available commands.
    """
    # Load configuration
    config_data = load_config(config_file, profile)
    
    # Store context values for use in commands
    ctx.obj = {
        "config": config_data,
        "verbose": verbose,
        "quiet": quiet,
        "output_format": output_format or config_data.get("output_format", "table"),
        "profile": profile or config_data.get("default_profile"),
    }
    
    # Show banner if not quiet and banner is enabled
    if show_banner and not quiet and ctx.invoked_subcommand != "completion":
        print_banner()


@app.command()
def completion(
    shell: str = typer.Argument(..., help="Shell type (bash, zsh, fish)"),
):
    """
    Generate shell completion script
    
    Example:
        llama completion bash >> ~/.bashrc
        llama completion zsh >> ~/.zshrc
        llama completion fish > ~/.config/fish/completions/llama.fish
    """
    if shell == "bash":
        console.print(typer.completion.get_bash_completion_script("llama"))
    elif shell == "zsh":
        console.print(typer.completion.get_zsh_completion_script("llama"))
    elif shell == "fish":
        console.print(typer.completion.get_fish_completion_script("llama"))
    else:
        console.print(f"Unsupported shell: {shell}", style="red")
        console.print("Supported shells: bash, zsh, fish")
        raise typer.Exit(1)


@app.command()
def shell():
    """
    Launch interactive shell mode
    
    Example:
        llama shell
    """
    from llama_cli.interactive import start_shell
    start_shell()


@app.command()
def init():
    """
    Initialize Llama CLI with default configuration
    
    Example:
        llama init
    """
    from llama_cli.config import initialize_config
    initialize_config()
    console.print("Llama CLI initialized successfully!", style="green")


if __name__ == "__main__":
    app() 