#!/usr/bin/env python3
"""
Windsurf MCP Config Manager CLI - A utility to manage the mcp_config.json file
for Windsurf/Codium MCP server configurations.
"""

import os
import sys
import json
import click
import requests
from pathlib import Path
from tabulate import tabulate
import re
from urllib.parse import urlparse

# Constants
DEFAULT_CONFIG_DIR = os.path.expanduser("~/.codeium/windsurf")
DEFAULT_CONFIG_FILE = "mcp_config.json"

def load_config():
    """Load the MCP server configuration."""
    config_path = os.path.join(DEFAULT_CONFIG_DIR, DEFAULT_CONFIG_FILE)
    
    # Create default config if it doesn't exist
    if not os.path.exists(config_path):
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        default_config = {"mcpServers": {}}
        with open(config_path, "w") as f:
            json.dump(default_config, f, indent=2)
        return default_config
    
    # Load existing config
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        click.echo(f"Error: {config_path} is not a valid JSON file.")
        return {"mcpServers": {}}


def save_config(config, config_path):
    """Save the MCP server configuration."""
    # Create a backup of the current config
    if os.path.exists(config_path):
        backup_path = f"{config_path}.bak"
        try:
            with open(config_path, "r") as src, open(backup_path, "w") as dst:
                dst.write(src.read())
            click.echo(f"Backup created at {backup_path}")
        except Exception as e:
            click.echo(f"Warning: Failed to create backup: {e}")
    
    # Save the new config
    os.makedirs(os.path.dirname(config_path), exist_ok=True)
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)
    click.echo(f"Configuration saved to {config_path}")


def check_pypi_package(package_name):
    """Check if a package exists on PyPI and get its latest version."""
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=5)
        if response.status_code == 200:
            data = response.json()
            version = data["info"]["version"]
            click.echo(f"Found package '{package_name}' on PyPI (version {version})")
            return True, version
        else:
            click.echo(f"Package '{package_name}' not found on PyPI")
            return False, None
    except Exception as e:
        click.echo(f"Error checking PyPI: {e}")
        return False, None


@click.group()
@click.pass_context
def cli(ctx):
    """Manage Windsurf MCP server configurations."""
    ctx.ensure_object(dict)
    ctx.obj["CONFIG_PATH"] = os.path.join(DEFAULT_CONFIG_DIR, DEFAULT_CONFIG_FILE)
    ctx.obj["CONFIG"] = load_config()


@cli.command()
@click.argument('name', required=True)
@click.option('--url', help='URL of the MCP server')
@click.option('--package', help='Package name to use with pipx or npx')
@click.option('--pipx', is_flag=True, help='Use pipx to run the package')
@click.option('--npx', is_flag=True, help='Use npx to run the package')
@click.pass_context
def add(ctx, name, url, package, pipx, npx):
    """Add a new MCP server configuration."""
    config = ctx.obj['CONFIG']
    
    if pipx and npx:
        click.echo("Error: Cannot specify both --pipx and --npx")
        return
        
    if (pipx or npx) and not package:
        click.echo("Error: --package is required when using --pipx or --npx")
        return
        
    if name in config["mcpServers"]:
        click.echo(f"Error: MCP server '{name}' already exists")
        return
    
    # Set up command and args based on package manager options
    if pipx:
        command = "pipx"
        arg_list = ["run", package]
        
        # Check if the package exists on PyPI
        exists, _ = check_pypi_package(package)
        
        if url:
            arg_list.append(url)
            
    elif npx:
        command = "npx"
        arg_list = ["-y", package]
        
        if url:
            arg_list.append(url)
    else:
        # For direct command
        if not url:
            click.echo("Error: URL is required when not using --pipx or --npx")
            return
            
        command = "mcp-proxy"
        arg_list = [url]
    
    # Add the server configuration
    config["mcpServers"][name] = {
        "command": command,
        "args": arg_list,
        "env": {}
    }
    
    save_config(config, ctx.obj['CONFIG_PATH'])
    click.echo(f"Added MCP server '{name}'")


@cli.command()
@click.argument('name')
@click.pass_context
def delete(ctx, name):
    """Delete an MCP server configuration."""
    config = ctx.obj['CONFIG']
    
    if name not in config["mcpServers"]:
        click.echo(f"Error: MCP server '{name}' not found")
        return
    
    del config["mcpServers"][name]
    save_config(config, ctx.obj['CONFIG_PATH'])
    click.echo(f"Deleted MCP server '{name}'")


@cli.command()
@click.pass_context
def list(ctx):
    """List all MCP server configurations."""
    config = ctx.obj['CONFIG']
    
    if not config["mcpServers"]:
        click.echo("No MCP servers configured")
        return
    
    # Prepare table data
    table_data = []
    for name, server in config["mcpServers"].items():
        command = server["command"]
        args = " ".join(server["args"])
        env = ", ".join([f"{k}={v}" for k, v in server["env"].items()]) if server["env"] else ""
        
        table_data.append([name, command, args, env])
    
    # Print table
    headers = ["Name", "Command", "Arguments", "Environment"]
    click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))


@cli.command()
@click.argument('name')
@click.option('--url', help='URL of the MCP server')
@click.option('--package', help='Package name to use with pipx or npx')
@click.option('--pipx', is_flag=True, help='Use pipx to run the package')
@click.option('--npx', is_flag=True, help='Use npx to run the package')
@click.pass_context
def update(ctx, name, url, package, pipx, npx):
    """Update an existing MCP server configuration."""
    config = ctx.obj['CONFIG']
    
    if name not in config["mcpServers"]:
        click.echo(f"Error: MCP server '{name}' not found")
        return
    
    server = config["mcpServers"][name]
    
    # Handle package manager options
    if pipx and npx:
        click.echo("Error: Cannot specify both --pipx and --npx")
        return
    
    if pipx:
        server["command"] = "pipx"
        if package:
            server["args"] = ["run", package]
            
            # Check if the package exists on PyPI
            exists, _ = check_pypi_package(package)
            
            if url:
                # Update the URL (last argument)
                if len(server["args"]) > 2:
                    server["args"][2] = url
                else:
                    server["args"].append(url)
        elif url and len(server["args"]) > 2:
            # Just update the URL
            server["args"][2] = url
    
    elif npx:
        server["command"] = "npx"
        if package:
            server["args"] = ["-y", package]
            if url:
                # Update the URL (last argument)
                if len(server["args"]) > 2:
                    server["args"][2] = url
                else:
                    server["args"].append(url)
        elif url and len(server["args"]) > 2:
            # Just update the URL
            server["args"][2] = url
    
    elif url:
        # For direct command, just update the URL (first argument)
        if server["args"]:
            server["args"][0] = url
        else:
            server["args"] = [url]
    
    save_config(config, ctx.obj['CONFIG_PATH'])
    click.echo(f"Updated MCP server '{name}'")


def main():
    """Entry point for the console script."""
    cli()


if __name__ == "__main__":
    main()
