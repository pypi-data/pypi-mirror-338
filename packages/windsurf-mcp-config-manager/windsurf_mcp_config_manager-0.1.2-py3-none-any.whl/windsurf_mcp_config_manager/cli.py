#!/usr/bin/env python3
"""
Windsurf MCP Config Manager CLI - A utility to manage the mcp_config.json file
for Windsurf/Codium MCP server configurations.
"""

import json
import os
import shutil
from pathlib import Path
from tabulate import tabulate

import click

# Default config file path
DEFAULT_CONFIG_PATH = os.path.expanduser("~/.codeium/windsurf/mcp_config.json")


def load_config(config_path):
    """Load the configuration file or return an empty dict if it doesn't exist."""
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            # If the file exists but is empty or invalid JSON
            return {"mcpServers": {}}
    else:
        # If the file doesn't exist
        return {"mcpServers": {}}


def save_config(config, config_path):
    """Save the configuration to the file, creating directories if needed."""
    # Create a backup of the existing file if it exists
    if os.path.exists(config_path):
        backup_path = f"{config_path}.bak"
        shutil.copy2(config_path, backup_path)
        click.echo(f"Backup created at {backup_path}")
    
    # Ensure the directory exists
    directory = os.path.dirname(config_path)
    if directory:  # Only create directories if there's a directory path
        os.makedirs(directory, exist_ok=True)
    
    # Write the config file
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    click.echo(f"Configuration saved to {config_path}")


@click.group()
@click.option('--config', default=DEFAULT_CONFIG_PATH, 
              help=f"Path to the config file (default: {DEFAULT_CONFIG_PATH})")
@click.pass_context
def cli(ctx, config):
    """Manage Windsurf MCP server configurations."""
    ctx.ensure_object(dict)
    ctx.obj['CONFIG_PATH'] = config
    ctx.obj['CONFIG'] = load_config(config)


@cli.command()
@click.argument('name')
@click.option('--command', required=True, help="Command to run the MCP server")
@click.option('--args', help="Arguments for the command (comma-separated)")
@click.option('--env', multiple=True, help="Environment variables in KEY=VALUE format")
@click.pass_context
def add(ctx, name, command, args, env):
    """Add a new MCP server configuration."""
    config = ctx.obj['CONFIG']
    
    # Check if the server already exists
    if name in config["mcpServers"]:
        click.echo(f"Error: MCP server '{name}' already exists.")
        return
    
    # Parse arguments
    arg_list = []
    if args:
        arg_list = [arg.strip() for arg in args.split(',')]
    
    # Parse environment variables
    env_dict = {}
    for e in env:
        if '=' in e:
            key, value = e.split('=', 1)
            env_dict[key] = value
    
    # Add the server configuration
    config["mcpServers"][name] = {
        "command": command,
        "args": arg_list,
        "env": env_dict
    }
    
    save_config(config, ctx.obj['CONFIG_PATH'])
    click.echo(f"Added MCP server '{name}'")


@cli.command()
@click.argument('name')
@click.pass_context
def delete(ctx, name):
    """Delete an MCP server configuration."""
    config = ctx.obj['CONFIG']
    
    # Check if the server exists
    if name not in config["mcpServers"]:
        click.echo(f"Error: MCP server '{name}' does not exist.")
        return
    
    # Delete the server configuration
    del config["mcpServers"][name]
    
    save_config(config, ctx.obj['CONFIG_PATH'])
    click.echo(f"Deleted MCP server '{name}'")


@cli.command()
@click.argument('name')
@click.option('--command', help="New command to run the MCP server")
@click.option('--args', help="New arguments for the command (comma-separated)")
@click.option('--env', multiple=True, help="Environment variables to add/update")
@click.pass_context
def update(ctx, name, command, args, env):
    """Update an existing MCP server configuration."""
    config = ctx.obj['CONFIG']
    
    # Check if the server exists
    if name not in config["mcpServers"]:
        click.echo(f"Error: MCP server '{name}' does not exist.")
        return
    
    # Update the command if provided
    if command:
        config["mcpServers"][name]["command"] = command
    
    # Update arguments if provided
    if args:
        arg_list = [arg.strip() for arg in args.split(',')]
        config["mcpServers"][name]["args"] = arg_list
    
    # Update environment variables if provided
    if env:
        for e in env:
            if '=' in e:
                key, value = e.split('=', 1)
                config["mcpServers"][name]["env"][key] = value
    
    save_config(config, ctx.obj['CONFIG_PATH'])
    click.echo(f"Updated MCP server '{name}'")


@cli.command()
@click.option('--format', type=click.Choice(['table', 'pretty', 'simple']), default='pretty', 
              help="Output format (table, pretty, or simple)")
@click.pass_context
def list(ctx, format):
    """List all configured MCP servers."""
    config = ctx.obj['CONFIG']
    
    if not config["mcpServers"]:
        click.echo("No MCP servers configured.")
        return
    
    if format == 'simple':
        # Simple text format (original style)
        click.echo("Configured MCP servers:\n")
        for name, server in config["mcpServers"].items():
            click.echo(f"{name}:")
            click.echo(f"  Command: {server['command']}")
            args_str = ", ".join(server['args'])
            click.echo(f"  Args: {args_str}")
            click.echo("  Environment variables:")
            for key, value in server.get('env', {}).items():
                click.echo(f"    {key}={value}")
            click.echo("")
    else:
        # Table format using tabulate
        headers = ["Name", "Command", "Arguments", "Environment Variables"]
        table_data = []
        
        for name, server in config["mcpServers"].items():
            args_str = ", ".join(server['args'])
            env_str = ", ".join([f"{k}={v}" for k, v in server.get('env', {}).items()])
            table_data.append([name, server['command'], args_str, env_str])
        
        if format == 'table':
            table_format = 'grid'
        else:  # pretty
            table_format = 'fancy_grid'
            
        click.echo(tabulate(table_data, headers=headers, tablefmt=table_format))


def main():
    """Main entry point for the CLI."""
    cli(obj={})


if __name__ == "__main__":
    main()
