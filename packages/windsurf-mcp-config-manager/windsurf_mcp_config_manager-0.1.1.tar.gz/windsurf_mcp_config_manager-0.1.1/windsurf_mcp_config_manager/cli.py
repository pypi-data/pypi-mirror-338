#!/usr/bin/env python3
"""
Windsurf MCP Config Manager CLI - A utility to manage the mcp_config.json file
for Windsurf/Codium MCP server configurations.
"""

import json
import os
import shutil
from pathlib import Path

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


@cli.command()
@click.argument('name')
@click.option('--command', required=True, help="Command to run the MCP server")
@click.option('--args', help="Arguments for the command (comma-separated)")
@click.option('--env', multiple=True, help="Environment variables in KEY=VALUE format")
@click.pass_context
def add(ctx, name, command, args, env):
    """Add a new MCP server configuration."""
    config = load_config(ctx.obj['CONFIG_PATH'])
    
    # Parse arguments
    arg_list = []
    if args:
        arg_list = [arg.strip() for arg in args.split(',')]
    
    # Parse environment variables
    env_vars = {}
    for env_pair in env:
        key, value = env_pair.split('=', 1)
        env_vars[key] = value
    
    # Create the server config
    server_config = {
        "command": command,
        "args": arg_list,
        "env": env_vars
    }
    
    # Add to the config
    config["mcpServers"][name] = server_config
    
    # Save the updated config
    save_config(config, ctx.obj['CONFIG_PATH'])
    click.echo(f"Added MCP server '{name}'")


@cli.command()
@click.argument('name')
@click.pass_context
def delete(ctx, name):
    """Delete an MCP server configuration."""
    config = load_config(ctx.obj['CONFIG_PATH'])
    
    if name in config.get("mcpServers", {}):
        del config["mcpServers"][name]
        save_config(config, ctx.obj['CONFIG_PATH'])
        click.echo(f"Deleted MCP server '{name}'")
    else:
        click.echo(f"Error: MCP server '{name}' not found", err=True)
        ctx.exit(1)


@cli.command()
@click.argument('name')
@click.option('--command', help="New command to run the MCP server")
@click.option('--args', help="New arguments for the command (comma-separated)")
@click.option('--env', multiple=True, help="Environment variables to add/update in KEY=VALUE format")
@click.pass_context
def update(ctx, name, command, args, env):
    """Update an existing MCP server configuration."""
    config = load_config(ctx.obj['CONFIG_PATH'])
    
    if name not in config.get("mcpServers", {}):
        click.echo(f"Error: MCP server '{name}' not found", err=True)
        ctx.exit(1)
    
    server_config = config["mcpServers"][name]
    
    # Update command if provided
    if command:
        server_config["command"] = command
    
    # Update args if provided
    if args:
        server_config["args"] = [arg.strip() for arg in args.split(',')]
    
    # Update environment variables if provided
    if env:
        env_vars = server_config.get("env", {})
        for env_pair in env:
            key, value = env_pair.split('=', 1)
            env_vars[key] = value
        server_config["env"] = env_vars
    
    # Save the updated config
    save_config(config, ctx.obj['CONFIG_PATH'])
    click.echo(f"Updated MCP server '{name}'")


@cli.command()
@click.pass_context
def list(ctx):
    """List all configured MCP servers."""
    config = load_config(ctx.obj['CONFIG_PATH'])
    
    if not config.get("mcpServers"):
        click.echo("No MCP servers configured")
        return
    
    click.echo("Configured MCP servers:")
    for name, server in config["mcpServers"].items():
        click.echo(f"\n{name}:")
        click.echo(f"  Command: {server.get('command', 'N/A')}")
        click.echo(f"  Args: {', '.join(server.get('args', []))}")
        if server.get('env'):
            click.echo("  Environment variables:")
            for key, value in server.get('env', {}).items():
                click.echo(f"    {key}={value}")


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
