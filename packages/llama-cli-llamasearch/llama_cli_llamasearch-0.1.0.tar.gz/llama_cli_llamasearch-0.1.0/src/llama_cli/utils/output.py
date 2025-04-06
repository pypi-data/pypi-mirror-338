"""
Output utilities for Llama CLI
"""
from typing import Any, Dict, List, Optional, Union
import json
import yaml
import csv
import io
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text


# Global console instance
_console = None


def get_console() -> Console:
    """
    Get or create the console instance
    
    Returns:
        Console instance
    """
    global _console
    if _console is None:
        _console = Console()
    return _console


def format_output(
    data: Any,
    output_format: str = "table",
    headers: Optional[List[str]] = None,
    title: Optional[str] = None,
) -> str:
    """
    Format data for output
    
    Args:
        data: Data to format (dict, list, str, etc.)
        output_format: Output format (table, json, yaml, csv)
        headers: Optional list of headers for tabular formats
        title: Optional title for the output
        
    Returns:
        Formatted output string
    """
    console = get_console()
    
    # Handle simple string data
    if isinstance(data, str):
        return data
    
    # Handle empty data
    if not data:
        return "" if output_format in ["json", "yaml", "csv"] else "No data"
    
    # Format based on requested output format
    if output_format == "json":
        return json.dumps(data, indent=2, default=str)
    
    elif output_format == "yaml":
        return yaml.dump(data, default_flow_style=False)
    
    elif output_format == "csv":
        if not isinstance(data, list):
            data = [data]
        
        if not data:
            return ""
        
        # Extract headers if not provided
        if headers is None:
            if isinstance(data[0], dict):
                headers = list(data[0].keys())
            else:
                headers = [f"Column{i+1}" for i in range(len(data[0]) if hasattr(data[0], "__len__") else 1)]
        
        # Generate CSV
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(headers)
        
        for item in data:
            if isinstance(item, dict):
                row = [item.get(h, "") for h in headers]
            elif isinstance(item, (list, tuple)):
                row = item
            else:
                row = [item]
            writer.writerow(row)
        
        return output.getvalue()
    
    # Default to table format for rich console output
    else:
        # Direct return for non-tabular data
        if not isinstance(data, (list, dict)):
            return str(data)
        
        # Convert single dict to list
        if isinstance(data, dict) and not any(isinstance(v, dict) for v in data.values()):
            data = [{"Key": k, "Value": v} for k, v in data.items()]
            if headers is None:
                headers = ["Key", "Value"]
        
        # Create rich table
        table = Table(title=title)
        
        # Determine headers if not provided
        if headers is None:
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                headers = list(data[0].keys())
            elif isinstance(data, dict):
                headers = ["Key", "Value"]
            else:
                headers = [f"Column{i+1}" for i in range(len(data[0]) if hasattr(data[0], "__len__") else 1)]
        
        # Add headers to table
        for header in headers:
            table.add_column(header)
        
        # Add rows to table
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    row = [str(item.get(h, "")) for h in headers]
                elif isinstance(item, (list, tuple)):
                    row = [str(x) for x in item]
                else:
                    row = [str(item)]
                table.add_row(*row)
        elif isinstance(data, dict):
            for k, v in data.items():
                table.add_row(k, str(v))
        
        # Render table to string
        string_io = io.StringIO()
        console_for_capture = Console(file=string_io, width=120)
        console_for_capture.print(table)
        return string_io.getvalue()


def print_output(
    data: Any,
    output_format: str = "table",
    headers: Optional[List[str]] = None,
    title: Optional[str] = None,
) -> None:
    """
    Print formatted data to the console
    
    Args:
        data: Data to print
        output_format: Output format (table, json, yaml, csv)
        headers: Optional list of headers for tabular formats
        title: Optional title for the output
    """
    console = get_console()
    
    if output_format == "json":
        console.print(Syntax(json.dumps(data, indent=2, default=str), "json", theme="monokai"))
    
    elif output_format == "yaml":
        console.print(Syntax(yaml.dump(data, default_flow_style=False), "yaml", theme="monokai"))
    
    elif output_format == "csv":
        formatted = format_output(data, "csv", headers)
        console.print(formatted)
    
    else:  # default to table format
        # Handle simple string data
        if isinstance(data, str):
            console.print(data)
            return
        
        # Handle empty data
        if not data:
            console.print("No data")
            return
        
        # Convert single dict to list
        if isinstance(data, dict) and not any(isinstance(v, dict) for v in data.values()):
            data = [{"Key": k, "Value": v} for k, v in data.items()]
            if headers is None:
                headers = ["Key", "Value"]
        
        # Create rich table
        table = Table(title=title)
        
        # Determine headers if not provided
        if headers is None:
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                headers = list(data[0].keys())
            elif isinstance(data, dict):
                headers = ["Key", "Value"]
            else:
                headers = [f"Column{i+1}" for i in range(len(data[0]) if hasattr(data[0], "__len__") else 1)]
        
        # Add headers to table
        for header in headers:
            table.add_column(header)
        
        # Add rows to table
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    row = [str(item.get(h, "")) for h in headers]
                elif isinstance(item, (list, tuple)):
                    row = [str(x) for x in item]
                else:
                    row = [str(item)]
                table.add_row(*row)
        elif isinstance(data, dict):
            for k, v in data.items():
                table.add_row(k, str(v))
        
        console.print(table)


def print_error(message: str, exit_code: Optional[int] = None) -> None:
    """
    Print an error message
    
    Args:
        message: Error message
        exit_code: Optional exit code (if provided, will exit with this code)
    """
    console = get_console()
    console.print(f"Error: {message}", style="bold red")
    
    if exit_code is not None:
        import sys
        sys.exit(exit_code)


def print_warning(message: str) -> None:
    """
    Print a warning message
    
    Args:
        message: Warning message
    """
    console = get_console()
    console.print(f"Warning: {message}", style="bold yellow")


def print_success(message: str) -> None:
    """
    Print a success message
    
    Args:
        message: Success message
    """
    console = get_console()
    console.print(message, style="bold green")


def print_json(data: Any, title: Optional[str] = None) -> None:
    """
    Print data as formatted JSON
    
    Args:
        data: Data to print as JSON
        title: Optional title
    """
    console = get_console()
    json_str = json.dumps(data, indent=2, default=str)
    
    if title:
        console.print(f"\n{title}:", style="bold")
    
    console.print(Syntax(json_str, "json", theme="monokai"))


def print_yaml(data: Any, title: Optional[str] = None) -> None:
    """
    Print data as formatted YAML
    
    Args:
        data: Data to print as YAML
        title: Optional title
    """
    console = get_console()
    yaml_str = yaml.dump(data, default_flow_style=False)
    
    if title:
        console.print(f"\n{title}:", style="bold")
    
    console.print(Syntax(yaml_str, "yaml", theme="monokai")) 