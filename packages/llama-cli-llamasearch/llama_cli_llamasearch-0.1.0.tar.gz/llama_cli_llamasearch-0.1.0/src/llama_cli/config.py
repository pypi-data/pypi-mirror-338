"""
Configuration management for Llama CLI
"""
import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional

import yaml
from rich.console import Console

# Default configuration directory
DEFAULT_CONFIG_DIR = os.path.expanduser("~/.config/llama")
DEFAULT_CONFIG_FILE = os.path.join(DEFAULT_CONFIG_DIR, "config.yaml")

# Console for output
console = Console()


def get_config_path(config_file: Optional[str] = None) -> str:
    """
    Get the path to the configuration file
    
    Args:
        config_file: Optional path to the configuration file
        
    Returns:
        Path to the configuration file
    """
    if config_file:
        return os.path.abspath(os.path.expanduser(config_file))
    return DEFAULT_CONFIG_FILE


def load_config(config_file: Optional[str] = None, profile: Optional[str] = None) -> Dict[str, Any]:
    """
    Load configuration from file
    
    Args:
        config_file: Optional path to the configuration file
        profile: Optional profile name to use
        
    Returns:
        Configuration dictionary
    """
    config_path = get_config_path(config_file)
    
    # Default configuration
    config = {
        "output_format": "table",
        "verbose": False,
        "default_profile": "default",
        "profiles": {
            "default": {
                "api_url": "https://api.llamasearch.ai",
            }
        }
    }
    
    # Try to load configuration from file
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                file_config = yaml.safe_load(f)
                if file_config:
                    config.update(file_config)
        except Exception as e:
            console.print(f"Error loading configuration: {e}", style="red")
    
    # Apply profile-specific settings
    active_profile = profile or config.get("default_profile", "default")
    if active_profile != "default" and active_profile in config.get("profiles", {}):
        profile_config = config["profiles"][active_profile]
        # Only update top-level keys, don't overwrite entire config
        for k, v in profile_config.items():
            if k not in ["profiles"]:  # Don't allow nested profiles
                config[k] = v
    
    return config


def save_config(config: Dict[str, Any], config_file: Optional[str] = None) -> bool:
    """
    Save configuration to file
    
    Args:
        config: Configuration dictionary
        config_file: Optional path to the configuration file
        
    Returns:
        True if successful, False otherwise
    """
    config_path = get_config_path(config_file)
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    
    try:
        with open(config_path, "w") as f:
            yaml.dump(config, f, default_flow_style=False)
        return True
    except Exception as e:
        console.print(f"Error saving configuration: {e}", style="red")
        return False


def initialize_config() -> bool:
    """
    Initialize configuration with default values
    
    Returns:
        True if successful, False otherwise
    """
    # Default configuration
    config = {
        "output_format": "table",
        "verbose": False,
        "default_profile": "default",
        "profiles": {
            "default": {
                "api_url": "https://api.llamasearch.ai",
            }
        },
        "search": {
            "default_index": "main",
            "max_results": 50,
        },
        "db": {
            "connection_string": "sqlite:///data.db",
            "timeout": 30,
        }
    }
    
    # Create directory structure
    os.makedirs(DEFAULT_CONFIG_DIR, exist_ok=True)
    
    # Save configuration
    return save_config(config)


def get_config_value(key: str, config: Optional[Dict[str, Any]] = None, 
                    profile: Optional[str] = None) -> Any:
    """
    Get a configuration value
    
    Args:
        key: Configuration key (dot notation supported for nested keys)
        config: Optional configuration dictionary
        profile: Optional profile name
        
    Returns:
        Configuration value or None if not found
    """
    if config is None:
        config = load_config(profile=profile)
    
    # Handle dot notation (e.g., "search.max_results")
    if "." in key:
        parts = key.split(".")
        curr = config
        for part in parts:
            if isinstance(curr, dict) and part in curr:
                curr = curr[part]
            else:
                return None
        return curr
    
    return config.get(key)


def set_config_value(key: str, value: Any, config_file: Optional[str] = None,
                    profile: Optional[str] = None) -> bool:
    """
    Set a configuration value
    
    Args:
        key: Configuration key (dot notation supported for nested keys)
        value: Value to set
        config_file: Optional path to the configuration file
        profile: Optional profile name
        
    Returns:
        True if successful, False otherwise
    """
    config = load_config(config_file, profile)
    
    # Handle profile-specific setting
    if profile:
        if "profiles" not in config:
            config["profiles"] = {}
        if profile not in config["profiles"]:
            config["profiles"][profile] = {}
        
        # Handle dot notation for profile settings
        if "." in key:
            parts = key.split(".")
            curr = config["profiles"][profile]
            for part in parts[:-1]:
                if part not in curr:
                    curr[part] = {}
                curr = curr[part]
            curr[parts[-1]] = value
        else:
            config["profiles"][profile][key] = value
    else:
        # Handle dot notation for global settings
        if "." in key:
            parts = key.split(".")
            curr = config
            for part in parts[:-1]:
                if part not in curr:
                    curr[part] = {}
                curr = curr[part]
            curr[parts[-1]] = value
        else:
            config[key] = value
    
    return save_config(config, config_file) 