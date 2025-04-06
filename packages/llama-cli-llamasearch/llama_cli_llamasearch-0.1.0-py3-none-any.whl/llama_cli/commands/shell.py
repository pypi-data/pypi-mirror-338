"""
Shell command for Llama CLI
"""
import typer

from llama_cli.utils.output import get_console, print_warning

# Create the shell app
app = typer.Typer(help="Interactive shell", hidden=True)
console = get_console()

# This module is only for command registration
# The actual shell implementation is in llama_cli.interactive 