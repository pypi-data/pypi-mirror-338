#!/usr/bin/env python3
"""
Windsurf MCP Config Manager CLI - A utility to manage the mcp_config.json file
for Windsurf/Codium MCP server configurations.
"""

import json
import os
import shutil
import requests
from pathlib import Path
from tabulate import tabulate

import click

# Default config file path
DEFAULT_CONFIG_PATH = os.path.expanduser("~/.codeium/windsurf/mcp_config.json")


def check_pypi_package(package_name):
    """Check if a package exists on PyPI and return its information."""
    try:
        response = requests.get(f"https://pypi.org/pypi/{package_name}/json", timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception:
        return None


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


def extract_name_from_url(url):
    """Extract a name from a URL for use as an MCP server name."""
    if not url:
        return None
        
    try:
        # Try to extract a meaningful name from the URL
        from urllib.parse import urlparse
        
        # Parse the URL
        parsed_url = urlparse(url)
        
        # Try different strategies to get a meaningful name
        if parsed_url.path and parsed_url.path != "/":
            # Use the last part of the path
            path_parts = [p for p in parsed_url.path.split("/") if p]
            if path_parts:
                return path_parts[-1].replace("-", "_").lower()
        
        # If no path, use the hostname without domain extension
        if parsed_url.netloc:
            hostname = parsed_url.netloc.split(":")[0]  # Remove port if present
            parts = hostname.split(".")
            if len(parts) > 2:
                # For subdomains like api.example.com, use the subdomain
                return parts[0].replace("-", "_").lower()
            elif len(parts) == 2:
                # For example.com, use the first part
                return parts[0].replace("-", "_").lower()
            else:
                return hostname.replace("-", "_").lower()
                
        # Fallback: use a hash of the URL
        import hashlib
        return f"mcp_{hashlib.md5(url.encode()).hexdigest()[:8]}"
    except Exception:
        # If anything goes wrong, return None
        return None


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
@click.argument('name', required=False)
@click.option('--command', help="Command to run the MCP server")
@click.option('--args', help="Arguments for the command (comma-separated)")
@click.option('--env', multiple=True, help="Environment variables in KEY=VALUE format")
@click.option('--pipx', is_flag=True, help="Use pipx to run a Python package")
@click.option('--npx', is_flag=True, help="Use npx to run a Node.js package")
@click.option('--package', help="Package name to install with pipx or npx")
@click.option('--url', help="URL for the MCP server")
@click.option('--auto-detect', is_flag=True, help="Auto-detect package manager based on URL")
@click.pass_context
def add(ctx, name, command, args, env, pipx, npx, package, url, auto_detect):
    """Add a new MCP server configuration. If name is not provided, it will be extracted from the URL."""
    config = ctx.obj['CONFIG']
    
    # If name is not provided, try to extract it from the URL
    if not name:
        if not url:
            click.echo("Error: Either name or URL must be provided.")
            return
            
        name = extract_name_from_url(url)
        if not name:
            click.echo("Error: Could not extract a valid name from the URL. Please provide a name explicitly.")
            return
            
        click.echo(f"Using extracted name from URL: '{name}'")
    
    # Check if the server already exists
    if name in config["mcpServers"]:
        click.echo(f"Error: MCP server '{name}' already exists.")
        return
    
    # Auto-detect package manager from URL if requested
    if auto_detect and url and not (pipx or npx):
        if "python" in url.lower() or "pypi" in url.lower():
            pipx = True
            click.echo(f"Auto-detected Python package from URL: {url}")
        elif "node" in url.lower() or "npm" in url.lower():
            npx = True
            click.echo(f"Auto-detected Node.js package from URL: {url}")
    
    # Handle package manager options
    if pipx and npx:
        click.echo("Error: Cannot use both --pipx and --npx at the same time.")
        return
    
    if (pipx or npx) and not package:
        click.echo("Error: --package is required when using --pipx or --npx.")
        return
    
    # Set up command and args based on package manager options
    if pipx:
        command = "pipx"
        arg_list = ["run"]
        if package:
            # Check if package exists on PyPI
            package_info = check_pypi_package(package)
            if package_info:
                click.echo(f"Found package '{package}' on PyPI (version {package_info['info']['version']})")
                
                # Check if we need to use --spec
                if ":" in package or "==" in package or "@" in package:
                    arg_list.extend(["--spec", package, package.split(":")[0].split("==")[0].split("@")[0]])
                else:
                    arg_list.append(package)
            else:
                click.echo(f"Warning: Package '{package}' not found on PyPI. Using as specified.")
                # Use --spec to be safe when package not found
                arg_list.extend(["--spec", package, package.split(":")[0].split("==")[0].split("@")[0]])
                
            if url:
                arg_list.append(url)
    elif npx:
        command = "npx"
        arg_list = ["-y", package]
        if url:
            arg_list.append(url)
    else:
        # Parse arguments for standard command
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
@click.option('--pipx', is_flag=True, help="Use pipx to run a Python package")
@click.option('--npx', is_flag=True, help="Use npx to run a Node.js package")
@click.option('--package', help="Package name to install with pipx or npx")
@click.option('--url', help="URL for the MCP server")
@click.option('--auto-detect', is_flag=True, help="Auto-detect package manager based on URL")
@click.pass_context
def update(ctx, name, command, args, env, pipx, npx, package, url, auto_detect):
    """Update an existing MCP server configuration."""
    config = ctx.obj['CONFIG']
    
    # Check if the server exists
    if name not in config["mcpServers"]:
        click.echo(f"Error: MCP server '{name}' does not exist.")
        return
    
    # Auto-detect package manager from URL if requested
    if auto_detect and url and not (pipx or npx):
        if "python" in url.lower() or "pypi" in url.lower():
            pipx = True
            click.echo(f"Auto-detected Python package from URL: {url}")
        elif "node" in url.lower() or "npm" in url.lower():
            npx = True
            click.echo(f"Auto-detected Node.js package from URL: {url}")
    
    # Handle package manager options
    if pipx and npx:
        click.echo("Error: Cannot use both --pipx and --npx at the same time.")
        return
    
    # Set up command and args based on package manager options
    if pipx:
        command = "pipx"
        arg_list = ["run"]
        if package:
            # Check if package exists on PyPI
            package_info = check_pypi_package(package)
            if package_info:
                click.echo(f"Found package '{package}' on PyPI (version {package_info['info']['version']})")
                
                # Check if we need to use --spec
                if ":" in package or "==" in package or "@" in package:
                    arg_list.extend(["--spec", package, package.split(":")[0].split("==")[0].split("@")[0]])
                else:
                    arg_list.append(package)
            else:
                click.echo(f"Warning: Package '{package}' not found on PyPI. Using as specified.")
                # Use --spec to be safe when package not found
                arg_list.extend(["--spec", package, package.split(":")[0].split("==")[0].split("@")[0]])
                
            if url:
                arg_list.append(url)
        config["mcpServers"][name]["command"] = command
        config["mcpServers"][name]["args"] = arg_list
    elif npx:
        command = "npx"
        arg_list = ["-y", package]
        if url:
            arg_list.append(url)
        config["mcpServers"][name]["command"] = command
        config["mcpServers"][name]["args"] = arg_list
    else:
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
