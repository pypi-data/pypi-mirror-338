"""
Authentication commands for Llama CLI
"""
import os
import sys
import getpass
from typing import Dict, Any, Optional

import typer
import keyring
from rich.prompt import Prompt

from llama_cli.config import load_config, save_config, get_config_value, set_config_value
from llama_cli.utils.output import get_console, print_success, print_error, print_warning

# Create the auth app
app = typer.Typer(help="Authentication commands")
console = get_console()

# Keyring service name
KEYRING_SERVICE = "llama-cli"


@app.command("login")
def login(
    api_key: Optional[str] = typer.Option(
        None, "--api-key", "-k", help="API key for LlamaSearch.ai services"
    ),
    profile: Optional[str] = typer.Option(
        None, "--profile", "-p", help="Profile name to store credentials"
    ),
):
    """
    Log in to LlamaSearch.ai services
    
    Example:
        llama auth login
        llama auth login --api-key YOUR_API_KEY
        llama auth login --profile dev
    """
    # Load config
    config = load_config()
    active_profile = profile or config.get("default_profile", "default")
    
    # Get API key from argument or prompt
    if not api_key:
        api_key = getpass.getpass("Enter your LlamaSearch.ai API key: ")
    
    if not api_key:
        print_error("API key is required", exit_code=1)
    
    # Save API key to keyring
    try:
        keyring.set_password(KEYRING_SERVICE, f"api_key_{active_profile}", api_key)
        
        # Update config with default profile if needed
        if "profiles" not in config:
            config["profiles"] = {}
        
        if active_profile not in config["profiles"]:
            config["profiles"][active_profile] = {}
        
        config["profiles"][active_profile]["api_url"] = "https://api.llamasearch.ai"
        save_config(config)
        
        print_success(f"Successfully logged in to LlamaSearch.ai services with profile '{active_profile}'")
    except Exception as e:
        print_error(f"Failed to save credentials: {e}", exit_code=1)


@app.command("logout")
def logout(
    profile: Optional[str] = typer.Option(
        None, "--profile", "-p", help="Profile name to clear credentials"
    ),
    all_profiles: bool = typer.Option(
        False, "--all", help="Clear credentials for all profiles"
    ),
):
    """
    Log out from LlamaSearch.ai services
    
    Example:
        llama auth logout
        llama auth logout --profile dev
        llama auth logout --all
    """
    # Load config
    config = load_config()
    
    if all_profiles:
        # Get all profiles
        profiles = list(config.get("profiles", {}).keys())
        for profile_name in profiles:
            try:
                keyring.delete_password(KEYRING_SERVICE, f"api_key_{profile_name}")
            except keyring.errors.PasswordDeleteError:
                pass
        print_success("Logged out from all profiles")
    else:
        active_profile = profile or config.get("default_profile", "default")
        try:
            keyring.delete_password(KEYRING_SERVICE, f"api_key_{active_profile}")
            print_success(f"Logged out from profile '{active_profile}'")
        except keyring.errors.PasswordDeleteError:
            print_warning(f"No credentials found for profile '{active_profile}'")


@app.command("status")
def status(
    profile: Optional[str] = typer.Option(
        None, "--profile", "-p", help="Profile name to check status"
    ),
):
    """
    Show current authentication status
    
    Example:
        llama auth status
        llama auth status --profile dev
    """
    # Load config
    config = load_config()
    active_profile = profile or config.get("default_profile", "default")
    
    # Check if API key exists
    try:
        api_key = keyring.get_password(KEYRING_SERVICE, f"api_key_{active_profile}")
        
        if api_key:
            # Show masked API key
            masked_key = api_key[:4] + "*" * (len(api_key) - 8) + api_key[-4:]
            console.print(f"Profile: [bold cyan]{active_profile}[/]")
            console.print(f"API Key: [bold green]{masked_key}[/]")
            console.print(f"API URL: [bold]{config.get('profiles', {}).get(active_profile, {}).get('api_url', 'https://api.llamasearch.ai')}[/]")
            console.print("\nStatus: [bold green]Authenticated[/]")
        else:
            console.print(f"Profile: [bold cyan]{active_profile}[/]")
            console.print("\nStatus: [bold red]Not authenticated[/]")
            console.print("\nRun [bold]llama auth login[/] to authenticate.")
    except Exception:
        console.print(f"Profile: [bold cyan]{active_profile}[/]")
        console.print("\nStatus: [bold red]Not authenticated[/]")
        console.print("\nRun [bold]llama auth login[/] to authenticate.")


@app.command("list")
def list_profiles():
    """
    List all authentication profiles
    
    Example:
        llama auth list
    """
    # Load config
    config = load_config()
    default_profile = config.get("default_profile", "default")
    profiles = config.get("profiles", {})
    
    if not profiles:
        print_warning("No profiles found")
        console.print("\nRun [bold]llama auth login[/] to create a profile.")
        return
    
    console.print("\n[bold]Authentication Profiles:[/]")
    
    for profile_name, profile_data in profiles.items():
        # Check if API key exists
        try:
            api_key = keyring.get_password(KEYRING_SERVICE, f"api_key_{profile_name}")
            
            if api_key:
                status = "[bold green]Authenticated[/]"
                # Show masked API key
                masked_key = api_key[:4] + "*" * (len(api_key) - 8) + api_key[-4:]
                api_key_display = f"API Key: [bold green]{masked_key}[/]"
            else:
                status = "[bold red]Not authenticated[/]"
                api_key_display = "API Key: [bold red]None[/]"
        except Exception:
            status = "[bold red]Not authenticated[/]"
            api_key_display = "API Key: [bold red]None[/]"
        
        # Mark default profile
        if profile_name == default_profile:
            profile_display = f"[bold cyan]{profile_name}[/] [bold yellow](default)[/]"
        else:
            profile_display = f"[bold cyan]{profile_name}[/]"
        
        console.print(f"\n{profile_display}")
        console.print(f"Status: {status}")
        console.print(api_key_display)
        console.print(f"API URL: [bold]{profile_data.get('api_url', 'https://api.llamasearch.ai')}[/]")


def get_api_key(profile: Optional[str] = None) -> Optional[str]:
    """
    Get API key for the given profile
    
    Args:
        profile: Profile name to get API key for
        
    Returns:
        API key if found, None otherwise
    """
    config = load_config()
    active_profile = profile or config.get("default_profile", "default")
    
    try:
        return keyring.get_password(KEYRING_SERVICE, f"api_key_{active_profile}")
    except Exception:
        return None 