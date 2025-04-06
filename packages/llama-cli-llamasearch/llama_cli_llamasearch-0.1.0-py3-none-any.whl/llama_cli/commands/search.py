"""
Search commands for Llama CLI
"""
import os
import sys
import json
from typing import Dict, Any, List, Optional

import typer
import requests
from rich.prompt import Prompt

from llama_cli.commands.auth import get_api_key
from llama_cli.config import load_config, get_config_value
from llama_cli.utils.output import get_console, print_success, print_error, print_warning, print_output

# Create the search app
app = typer.Typer(help="Search commands")
console = get_console()


@app.command("query")
def search_query(
    query: str = typer.Argument(..., help="Search query"),
    index: Optional[str] = typer.Option(
        None, "--index", "-i", help="Index to search in"
    ),
    limit: int = typer.Option(
        10, "--limit", "-l", help="Maximum number of results"
    ),
    output_format: str = typer.Option(
        "table", "--format", "-f", help="Output format (json, yaml, table)"
    ),
    profile: Optional[str] = typer.Option(
        None, "--profile", "-p", help="Profile to use"
    ),
):
    """
    Perform a search query
    
    Example:
        llama search query "machine learning frameworks"
        llama search query "machine learning frameworks" --index docs --limit 20
        llama search query "machine learning frameworks" --format json
    """
    # Load config
    config = load_config()
    active_profile = profile or config.get("default_profile", "default")
    
    # Get API key
    api_key = get_api_key(active_profile)
    if not api_key:
        print_error("Not authenticated. Please run 'llama auth login' first.")
        return
    
    # Get search configuration
    search_config = get_config_value("search", config) or {}
    default_index = search_config.get("default_index", "main")
    
    # Get API URL
    if "profiles" in config and active_profile in config["profiles"]:
        api_url = config["profiles"][active_profile].get("api_url", "https://api.llamasearch.ai")
    else:
        api_url = "https://api.llamasearch.ai"
    
    # Perform search query
    console.print(f"Searching for [bold cyan]{query}[/]...")
    
    try:
        response = requests.post(
            f"{api_url}/search/query",
            json={
                "query": query,
                "index": index or default_index,
                "limit": limit,
            },
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            timeout=30,
        )
        
        # Check response
        if response.status_code == 200:
            # Parse results
            results = response.json()
            
            if "results" in results and results["results"]:
                # Print results
                print_output(results["results"], output_format, title=f"Search Results for '{query}'")
                console.print(f"\nFound {len(results['results'])} results in {results.get('time_ms', 0)}ms")
            else:
                print_warning("No results found")
        else:
            print_error(f"Search failed: {response.text}")
    except Exception as e:
        print_error(f"Search failed: {e}")


@app.command("index")
def search_index(
    action: str = typer.Argument(
        "list", help="Action to perform (list, create, delete, stats)"
    ),
    name: Optional[str] = typer.Option(
        None, "--name", "-n", help="Index name"
    ),
    schema: Optional[str] = typer.Option(
        None, "--schema", "-s", help="Schema file path"
    ),
    force: bool = typer.Option(
        False, "--force", help="Force delete without confirmation"
    ),
    output_format: str = typer.Option(
        "table", "--format", "-f", help="Output format (json, yaml, table)"
    ),
    profile: Optional[str] = typer.Option(
        None, "--profile", "-p", help="Profile to use"
    ),
):
    """
    Manage search indices
    
    Example:
        llama search index list
        llama search index create my-index --schema schema.yaml
        llama search index stats my-index
        llama search index delete my-index --force
    """
    # Load config
    config = load_config()
    active_profile = profile or config.get("default_profile", "default")
    
    # Get API key
    api_key = get_api_key(active_profile)
    if not api_key:
        print_error("Not authenticated. Please run 'llama auth login' first.")
        return
    
    # Get API URL
    if "profiles" in config and active_profile in config["profiles"]:
        api_url = config["profiles"][active_profile].get("api_url", "https://api.llamasearch.ai")
    else:
        api_url = "https://api.llamasearch.ai"
    
    # Handle different actions
    if action == "list":
        # List indices
        try:
            response = requests.get(
                f"{api_url}/search/indices",
                headers={
                    "Authorization": f"Bearer {api_key}",
                },
                timeout=30,
            )
            
            # Check response
            if response.status_code == 200:
                # Parse results
                results = response.json()
                
                if "indices" in results and results["indices"]:
                    # Print results
                    print_output(results["indices"], output_format, title="Search Indices")
                else:
                    print_warning("No indices found")
            else:
                print_error(f"Failed to list indices: {response.text}")
        except Exception as e:
            print_error(f"Failed to list indices: {e}")
    
    elif action == "create":
        # Create index
        if not name:
            print_error("Index name is required. Use --name option.")
            return
        
        # Load schema if provided
        if schema:
            try:
                if not os.path.exists(schema):
                    print_error(f"Schema file not found: {schema}")
                    return
                
                with open(schema, "r") as f:
                    if schema.endswith(".json"):
                        schema_data = json.load(f)
                    elif schema.endswith((".yaml", ".yml")):
                        import yaml
                        schema_data = yaml.safe_load(f)
                    else:
                        print_error("Schema file must be JSON or YAML")
                        return
            except Exception as e:
                print_error(f"Failed to load schema: {e}")
                return
        else:
            # Use default schema
            schema_data = {
                "fields": [
                    {"name": "title", "type": "text", "indexed": True},
                    {"name": "content", "type": "text", "indexed": True},
                    {"name": "url", "type": "keyword", "indexed": True},
                    {"name": "timestamp", "type": "date", "indexed": True},
                ]
            }
        
        # Create index
        try:
            response = requests.post(
                f"{api_url}/search/indices",
                json={
                    "name": name,
                    "schema": schema_data,
                },
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                timeout=30,
            )
            
            # Check response
            if response.status_code == 200:
                print_success(f"Index '{name}' created successfully")
            else:
                print_error(f"Failed to create index: {response.text}")
        except Exception as e:
            print_error(f"Failed to create index: {e}")
    
    elif action == "delete":
        # Delete index
        if not name:
            print_error("Index name is required. Use --name option.")
            return
        
        # Confirm deletion
        if not force:
            from rich.prompt import Confirm
            confirm = Confirm.ask(
                f"Are you sure you want to delete index '{name}'?",
                default=False,
            )
            if not confirm:
                console.print("Index deletion cancelled")
                return
        
        # Delete index
        try:
            response = requests.delete(
                f"{api_url}/search/indices/{name}",
                headers={
                    "Authorization": f"Bearer {api_key}",
                },
                timeout=30,
            )
            
            # Check response
            if response.status_code == 200:
                print_success(f"Index '{name}' deleted successfully")
            else:
                print_error(f"Failed to delete index: {response.text}")
        except Exception as e:
            print_error(f"Failed to delete index: {e}")
    
    elif action == "stats":
        # Get index stats
        if not name:
            print_error("Index name is required. Use --name option.")
            return
        
        # Get stats
        try:
            response = requests.get(
                f"{api_url}/search/indices/{name}/stats",
                headers={
                    "Authorization": f"Bearer {api_key}",
                },
                timeout=30,
            )
            
            # Check response
            if response.status_code == 200:
                # Parse results
                results = response.json()
                
                # Print results
                print_output(results, output_format, title=f"Stats for Index '{name}'")
            else:
                print_error(f"Failed to get index stats: {response.text}")
        except Exception as e:
            print_error(f"Failed to get index stats: {e}")
    
    else:
        print_error(f"Unknown action: {action}")
        console.print("Available actions: list, create, delete, stats")


@app.command("vector")
def vector_search(
    query: str = typer.Argument(..., help="Search query"),
    model: str = typer.Option(
        "text-embedding-ada-002", "--model", "-m", help="Embedding model to use"
    ),
    index: Optional[str] = typer.Option(
        None, "--index", "-i", help="Index to search in"
    ),
    top_k: int = typer.Option(
        5, "--top", "-t", help="Number of top results to return"
    ),
    output_format: str = typer.Option(
        "table", "--format", "-f", help="Output format (json, yaml, table)"
    ),
    profile: Optional[str] = typer.Option(
        None, "--profile", "-p", help="Profile to use"
    ),
):
    """
    Perform vector search
    
    Example:
        llama search vector "semantic query"
        llama search vector "semantic query" --model text-embedding-ada-002 --top 10
        llama search vector "semantic query" --index docs --format json
    """
    # Load config
    config = load_config()
    active_profile = profile or config.get("default_profile", "default")
    
    # Get API key
    api_key = get_api_key(active_profile)
    if not api_key:
        print_error("Not authenticated. Please run 'llama auth login' first.")
        return
    
    # Get search configuration
    search_config = get_config_value("search", config) or {}
    default_index = search_config.get("default_index", "main")
    
    # Get API URL
    if "profiles" in config and active_profile in config["profiles"]:
        api_url = config["profiles"][active_profile].get("api_url", "https://api.llamasearch.ai")
    else:
        api_url = "https://api.llamasearch.ai"
    
    # Perform vector search query
    console.print(f"Performing vector search for [bold cyan]{query}[/] using model [bold green]{model}[/]...")
    
    try:
        response = requests.post(
            f"{api_url}/search/vector",
            json={
                "query": query,
                "model": model,
                "index": index or default_index,
                "top_k": top_k,
            },
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            timeout=30,
        )
        
        # Check response
        if response.status_code == 200:
            # Parse results
            results = response.json()
            
            if "results" in results and results["results"]:
                # Print results
                print_output(results["results"], output_format, title=f"Vector Search Results for '{query}'")
                console.print(f"\nFound {len(results['results'])} results in {results.get('time_ms', 0)}ms")
            else:
                print_warning("No results found")
        else:
            print_error(f"Vector search failed: {response.text}")
    except Exception as e:
        print_error(f"Vector search failed: {e}") 