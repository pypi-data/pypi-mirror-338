# Llama CLI

A powerful command-line interface for interacting with the LlamaSearch.ai ecosystem of tools.

## Features

- **Unified Interface**: Access all LlamaSearch.ai tools through a single, consistent CLI
- **Advanced Command Structure**: Organized command hierarchy with intuitive subcommands
- **Configuration Management**: Save and manage profiles for different environments
- **Interactive Mode**: Terminal UI for exploring available commands and options
- **Shell Completion**: Tab completion for commands, options, and arguments
- **Plugin System**: Extensible architecture for adding custom commands
- **Authentication**: Secure authentication with different LlamaSearch.ai services
- **Batch Processing**: Run commands in batch mode with input/output redirection

## Installation

### Using pip

```bash
pip install llama-cli
```

### From source

```bash
git clone https://llamasearch.ai
cd llama-cli
pip install -e .
```

## Quick Start

After installation, you can use the `llama` command to access all functionality:

```bash
# Show help and available commands
llama --help

# Show version information
llama --version

# Initialize configuration
llama init

# Authenticate with LlamaSearch.ai services
llama auth login
```

## Command Structure

The CLI is organized into categories of commands:

```
llama
├── auth          # Authentication commands
│   ├── login     # Log in to LlamaSearch.ai services
│   ├── logout    # Log out from current session
│   └── status    # Show current authentication status
├── config        # Configuration management
│   ├── get       # Get configuration values
│   ├── set       # Set configuration values
│   └── list      # List available configurations
├── search        # Search commands
│   ├── query     # Perform a search query
│   ├── index     # Manage search indices
│   └── vector    # Vector search operations
├── db            # Database operations
│   ├── query     # Run database queries
│   ├── migrate   # Run database migrations
│   └── backup    # Backup and restore operations
├── kv            # Key-value store operations
│   ├── get       # Get values from key-value store
│   ├── set       # Set values in key-value store
│   └── delete    # Delete keys from key-value store
├── api           # API client operations
│   ├── request   # Make API requests
│   ├── describe  # Describe API endpoints
│   └── generate  # Generate API client code
├── pdf           # PDF processing tools
│   ├── convert   # Convert PDFs to other formats
│   ├── extract   # Extract content from PDFs
│   └── search    # Search within PDF documents
└── analytics     # Analytics tools
    ├── track     # Track events and metrics
    ├── report    # Generate analytics reports
    └── visualize # Visualize analytics data
```

## Configuration

Llama CLI uses a configuration file located at `~/.config/llama/config.yaml` by default. You can also specify a custom configuration file using the `--config` option.

Example configuration:

```yaml
# Global configuration
default_profile: prod
output_format: json
verbose: false

# Profiles
profiles:
  dev:
    api_url: https://dev.api.llamasearch.ai
    api_key: your_dev_api_key
  prod:
    api_url: https://api.llamasearch.ai
    api_key: your_prod_api_key

# Tool-specific configurations
search:
  default_index: main
  max_results: 50

db:
  connection_string: "sqlite:///data.db"
  timeout: 30
```

## Interactive Mode

Llama CLI includes an interactive shell mode that you can use to explore and run commands:

```bash
llama shell
```

In interactive mode, you can:
- Browse available commands with tab completion
- View inline help and examples
- Execute commands with history and editing
- Use context-aware autocompletion

## Shell Completion

You can enable shell completion for bash, zsh, or fish:

```bash
# For bash
llama completion bash >> ~/.bashrc

# For zsh
llama completion zsh >> ~/.zshrc

# For fish
llama completion fish > ~/.config/fish/completions/llama.fish
```

## Plugin System

Llama CLI can be extended with plugins. Plugins can add new commands or modify existing ones.

To install a plugin:

```bash
llama plugins install llamasearch-plugin-name
```

To create a plugin, use the plugin template:

```bash
llama plugins create my-plugin
```

## Examples

### Search Operations

```bash
# Perform a search query
llama search query "machine learning frameworks" --index docs --limit 10 --format json

# Create a new search index
llama search index create my-index --schema schema.yaml

# Perform vector search
llama search vector "semantic query" --model text-embedding-ada-002 --top 5
```

### Database Operations

```bash
# Execute a SQL query
llama db query "SELECT * FROM users LIMIT 10" --connection prod

# Run database migrations
llama db migrate up --target latest

# Export database data
llama db export users.csv --table users --format csv
```

### Key-Value Store Operations

```bash
# Get a value
llama kv get my-key --store default

# Set a value
llama kv set my-key my-value --ttl 3600

# Delete a key
llama kv delete my-key
```

### API Operations

```bash
# Make a GET request
llama api request get /users/123 --format json

# Generate an API client
llama api generate python --output ./client --spec openapi.yaml
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT 