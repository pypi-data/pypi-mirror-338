"""
Interactive shell for Llama CLI
"""
import os
import sys
import shlex
from typing import Dict, Any, List, Optional

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.syntax import Syntax

from llama_cli import __version__
from llama_cli.utils.output import get_console, print_error, print_success


# Command history file
HISTORY_FILE = os.path.expanduser("~/.config/llama/history")


class LlamaCommandCompleter(Completer):
    """Command completer for Llama CLI interactive shell"""
    
    def __init__(self, commands: Dict[str, Any]):
        self.commands = commands
    
    def get_completions(self, document, complete_event):
        # Get word being completed
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        text = document.text_before_cursor.lstrip()
        
        # Get all words
        words = shlex.split(text) if text else []
        
        # Complete command
        if len(words) <= 1:
            for command in sorted(self.commands.keys()):
                if command.startswith(word_before_cursor):
                    yield Completion(
                        command, 
                        start_position=-len(word_before_cursor),
                        display=command,
                        display_meta=self.commands[command].get("help", "")
                    )
            return
        
        # Complete subcommand
        command = words[0]
        if command in self.commands and "subcommands" in self.commands[command]:
            subcommands = self.commands[command]["subcommands"]
            if len(words) == 1 or (len(words) == 2 and not document.text_before_cursor.endswith(" ")):
                for subcommand in sorted(subcommands.keys()):
                    if subcommand.startswith(word_before_cursor):
                        yield Completion(
                            subcommand,
                            start_position=-len(word_before_cursor),
                            display=subcommand,
                            display_meta=subcommands[subcommand].get("help", "")
                        )
            # Complete options
            elif len(words) >= 2:
                subcommand = words[1]
                if subcommand in subcommands and "options" in subcommands[subcommand]:
                    options = subcommands[subcommand]["options"]
                    for option in sorted(options.keys()):
                        if option.startswith(word_before_cursor):
                            yield Completion(
                                option,
                                start_position=-len(word_before_cursor),
                                display=option,
                                display_meta=options[option]
                            )


def get_available_commands() -> Dict[str, Any]:
    """
    Get available commands for completion
    
    Returns:
        Dictionary of commands and their subcommands/options
    """
    # This is a simplified version of the command structure
    # In a real implementation, this would be generated dynamically from the CLI app
    return {
        "auth": {
            "help": "Authentication commands",
            "subcommands": {
                "login": {
                    "help": "Log in to LlamaSearch.ai services",
                    "options": {
                        "--api-key": "API key for authentication",
                        "--profile": "Profile to store credentials",
                    }
                },
                "logout": {
                    "help": "Log out from LlamaSearch.ai services",
                    "options": {
                        "--profile": "Profile to clear credentials",
                        "--all": "Clear all profiles",
                    }
                },
                "status": {
                    "help": "Show authentication status",
                    "options": {
                        "--profile": "Profile to check status for",
                    }
                },
                "list": {
                    "help": "List authentication profiles",
                }
            }
        },
        "config": {
            "help": "Configuration management",
            "subcommands": {
                "get": {
                    "help": "Get configuration value",
                    "options": {
                        "--profile": "Profile to get configuration from",
                        "--format": "Output format (json, yaml, table)",
                    }
                },
                "set": {
                    "help": "Set configuration value",
                    "options": {
                        "--profile": "Profile to set configuration for",
                    }
                },
                "list": {
                    "help": "List configuration values",
                    "options": {
                        "--profile": "Profile to list configuration for",
                        "--format": "Output format (json, yaml, table)",
                    }
                },
                "init": {
                    "help": "Initialize configuration with default values",
                    "options": {
                        "--force": "Force overwrite existing configuration",
                    }
                },
                "path": {
                    "help": "Show configuration file path",
                },
                "edit": {
                    "help": "Open configuration file in editor",
                },
                "profiles": {
                    "help": "List configuration profiles",
                    "options": {
                        "--format": "Output format (json, yaml, table)",
                    }
                },
                "create-profile": {
                    "help": "Create a new configuration profile",
                    "options": {
                        "--api-url": "API URL for the profile",
                        "--default": "Set as default profile",
                    }
                },
                "delete-profile": {
                    "help": "Delete a configuration profile",
                    "options": {
                        "--force": "Skip confirmation",
                    }
                },
                "default-profile": {
                    "help": "Set the default configuration profile",
                }
            }
        },
        "search": {
            "help": "Search commands",
            "subcommands": {
                "query": {
                    "help": "Perform a search query",
                    "options": {
                        "--index": "Index to search in",
                        "--limit": "Maximum number of results",
                        "--format": "Output format (json, yaml, table)",
                    }
                },
                "index": {
                    "help": "Manage search indices",
                    "options": {
                        "--format": "Output format (json, yaml, table)",
                    }
                }
            }
        },
        "db": {
            "help": "Database operations",
            "subcommands": {
                "query": {
                    "help": "Run database queries",
                    "options": {
                        "--connection": "Database connection to use",
                        "--format": "Output format (json, yaml, table, csv)",
                    }
                },
                "migrate": {
                    "help": "Run database migrations",
                    "options": {
                        "--target": "Migration target version",
                        "--dry-run": "Show migrations without applying",
                    }
                },
                "backup": {
                    "help": "Backup and restore operations",
                    "options": {
                        "--file": "Backup file path",
                        "--compress": "Compress backup",
                    }
                }
            }
        },
        "kv": {
            "help": "Key-value store operations",
            "subcommands": {
                "get": {
                    "help": "Get values from key-value store",
                    "options": {
                        "--store": "Key-value store to use",
                        "--format": "Output format (json, yaml, table)",
                    }
                },
                "set": {
                    "help": "Set values in key-value store",
                    "options": {
                        "--store": "Key-value store to use",
                        "--ttl": "Time to live in seconds",
                    }
                },
                "delete": {
                    "help": "Delete keys from key-value store",
                    "options": {
                        "--store": "Key-value store to use",
                        "--force": "Skip confirmation",
                    }
                }
            }
        },
        "api": {
            "help": "API client operations",
            "subcommands": {
                "request": {
                    "help": "Make API requests",
                    "options": {
                        "--method": "HTTP method (GET, POST, PUT, DELETE)",
                        "--data": "Request data",
                        "--format": "Output format (json, yaml, table)",
                    }
                },
                "describe": {
                    "help": "Describe API endpoints",
                    "options": {
                        "--format": "Output format (json, yaml, table)",
                    }
                },
                "generate": {
                    "help": "Generate API client code",
                    "options": {
                        "--language": "Programming language",
                        "--output": "Output directory",
                    }
                }
            }
        },
        "exit": {
            "help": "Exit the shell",
        },
        "quit": {
            "help": "Exit the shell",
        },
        "help": {
            "help": "Show help for a command",
        }
    }


def print_shell_help(commands: Dict[str, Any]) -> None:
    """
    Print help information for the shell
    
    Args:
        commands: Dictionary of commands and their metadata
    """
    console = get_console()
    console.print("\n[bold]Available Commands:[/]")
    
    for command, data in sorted(commands.items()):
        help_text = data.get("help", "")
        console.print(f"  [bold cyan]{command}[/] - {help_text}")
    
    console.print("\n[bold]Shell Features:[/]")
    console.print("  • Tab completion for commands and options")
    console.print("  • Command history (up/down arrows)")
    console.print("  • Command history search (Ctrl+R)")
    console.print("  • Auto-suggestions based on history")
    console.print("  • Type 'exit' or 'quit' to exit the shell")
    console.print("  • Type 'help <command>' for detailed help on a command")
    console.print("")


def print_command_help(command: str, commands: Dict[str, Any]) -> None:
    """
    Print help information for a specific command
    
    Args:
        command: Command name
        commands: Dictionary of commands and their metadata
    """
    console = get_console()
    
    if command not in commands:
        print_error(f"Unknown command: {command}")
        return
    
    data = commands[command]
    help_text = data.get("help", "No help available")
    
    console.print(f"\n[bold]Command:[/] [bold cyan]{command}[/]")
    console.print(f"[bold]Description:[/] {help_text}")
    
    if "subcommands" in data:
        console.print("\n[bold]Subcommands:[/]")
        for subcommand, subdata in sorted(data["subcommands"].items()):
            subhelp = subdata.get("help", "")
            console.print(f"  [bold cyan]{subcommand}[/] - {subhelp}")
            
            if "options" in subdata:
                console.print("  [bold]Options:[/]")
                for option, option_help in sorted(subdata["options"].items()):
                    console.print(f"    [bold green]{option}[/] - {option_help}")
    
    console.print("")


def execute_command(command_line: str) -> None:
    """
    Execute a command in the shell
    
    Args:
        command_line: Command line to execute
    """
    if not command_line.strip():
        return
    
    # Split command line into arguments
    try:
        args = shlex.split(command_line)
    except Exception as e:
        print_error(f"Invalid command line: {e}")
        return
    
    # Handle built-in commands
    command = args[0]
    
    if command in ["exit", "quit"]:
        print_success("Exiting Llama CLI shell")
        sys.exit(0)
    
    if command == "help":
        if len(args) > 1:
            print_command_help(args[1], get_available_commands())
        else:
            print_shell_help(get_available_commands())
        return
    
    # Execute command using the main CLI app
    try:
        # In a real implementation, we would use the CLI app directly
        # Here we just simulate it by printing the command
        console = get_console()
        console.print(f"[bold]Executing:[/] llama {command_line}")
        
        # Create command
        cmd = ["llama"] + args
        cmd_str = " ".join(cmd)
        
        # Run the command
        os.system(cmd_str)
    except Exception as e:
        print_error(f"Error executing command: {e}")


def start_shell() -> None:
    """Start the interactive shell"""
    console = get_console()
    
    # Create command history directory if it doesn't exist
    history_dir = os.path.dirname(HISTORY_FILE)
    os.makedirs(history_dir, exist_ok=True)
    
    # Create prompt session with history and auto-suggest
    session = PromptSession(
        history=FileHistory(HISTORY_FILE),
        auto_suggest=AutoSuggestFromHistory(),
        completer=LlamaCommandCompleter(get_available_commands()),
        style=Style.from_dict({
            "prompt": "ansigreen bold",
        }),
        complete_while_typing=True,
    )
    
    # Print welcome message
    console.print(f"\n[bold yellow]Llama CLI Interactive Shell v{__version__}[/]")
    console.print("Type [bold cyan]help[/] for a list of commands, or [bold cyan]exit[/] to quit.\n")
    
    # Main loop
    while True:
        try:
            # Get command from user
            command = session.prompt("llama> ")
            
            # Execute command
            execute_command(command)
        except KeyboardInterrupt:
            console.print("\nUse [bold]exit[/] or [bold]quit[/] to exit the shell.")
        except EOFError:
            print_success("\nExiting Llama CLI shell")
            break
        except Exception as e:
            print_error(f"Error: {e}")


if __name__ == "__main__":
    start_shell() 