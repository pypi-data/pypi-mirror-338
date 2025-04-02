#!/usr/bin/env python3
"""WandB Logger - A command-line application for managing WandB training logs."""

import sys
import logging
from pathlib import Path
import click

from .config import BASE_DIR, DEFAULT_LIMIT
from .ui.console import console, create_panel
from .wandb_api import WandbAPI
from .commands import (
    login_command, logout_command, status_command,
    fetch_command, recent_command, recent_runs_command,
    list_command, cache_command, metrics_command, help_command
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('wandb_logger')

# Create WandB API instance
wandb_api = WandbAPI(data_dir=BASE_DIR / 'data')

# Create CLI group
@click.group()
def cli():
    """WandB Logger - A command-line application for managing WandB training logs."""
    # Display header
    console.print(create_panel(
        "[bold cyan]WandB Logger[/bold cyan]", 
        title="A tool for managing WandB training logs"
    ))

@cli.command()
@click.option('--api-key', help='WandB API key')
def login(api_key):
    """Log in to your WandB account."""
    login_command(wandb_api, api_key)

@cli.command()
def logout():
    """Log out from your WandB account."""
    logout_command(wandb_api)

@cli.command()
def status():
    """Check your WandB login status."""
    status_command(wandb_api)

@cli.command()
@click.argument('run_url')
@click.option('--metrics', '-m', multiple=True, help='Specific metrics to fetch (can be used multiple times)')
@click.option('--force-refresh', '-f', is_flag=True, help='Force refresh data from WandB (ignore cache)')
@click.option('--all', '-a', is_flag=True, help='Fetch all metrics without selection')
@click.option('--select/--no-select', '-s/-n', is_flag=True, default=True, help='Interactively select which metrics to include in the report')
@click.option('--clean', '-c', is_flag=True, help='Clean up existing graph files before generating new ones')
def fetch(run_url, metrics, force_refresh, all, select, clean):
    """Fetch logs and graphs from a WandB run."""
    # If --all is specified, disable selection
    if all:
        select = False
    fetch_command(wandb_api, run_url, metrics, force_refresh, select, clean)

@cli.command()
@click.option('--limit', '-l', default=DEFAULT_LIMIT, help='Maximum number of recent runs to show')
@click.option('--metrics', '-m', multiple=True, help='Specific metrics to fetch (can be used multiple times)')
@click.option('--force-refresh', '-f', is_flag=True, help='Force refresh data from WandB (ignore cache)')
@click.option('--select/--no-select', '-s/-n', is_flag=True, default=True, help='Interactively select which metrics to include in the report')
@click.option('--clean', '-c', is_flag=True, help='Clean up existing graph files before generating new ones')
def recent(limit, metrics, force_refresh, select, clean):
    """Fetch and select from your recent WandB runs."""
    recent_command(wandb_api, limit, metrics, force_refresh, select, clean)

@cli.command('recent-runs')
@click.option('--limit', '-l', default=DEFAULT_LIMIT, help='Maximum number of recent runs to show')
@click.option('--metrics', '-m', multiple=True, help='Specific metrics to fetch (can be used multiple times)')
@click.option('--force-refresh', '-f', is_flag=True, help='Force refresh data from WandB (ignore cache)')
@click.option('--select/--no-select', '-s/-n', is_flag=True, default=True, help='Interactively select which metrics to include in the report')
@click.option('--clean', '-c', is_flag=True, help='Clean up existing graph files before generating new ones')
@click.option('--project', '-p', help='Filter runs by project name')
@click.option('--entity', '-e', help='Username or organization name to fetch runs from')
@click.option('--max-projects', default=3, help='Maximum number of most recent projects to fetch (default: 3)')
@click.option('--all-projects', is_flag=True, help='Fetch runs from all projects (may be slow)')
def recent_runs(limit, metrics, force_refresh, select, clean, project, entity, max_projects, all_projects):
    """Browse and select from your recent WandB runs across all projects."""
    recent_runs_command(wandb_api, limit, metrics, force_refresh, select, clean, project, entity, max_projects, all_projects)

@cli.command()
def list():
    """List all saved runs."""
    list_command(wandb_api)

@cli.command()
@click.argument('run_url')
@click.option('--force-refresh', '-f', is_flag=True, help='Force refresh data from WandB (ignore cache)')
def metrics(run_url, force_refresh):
    """List available metrics for a WandB run."""
    metrics_command(wandb_api, run_url, force_refresh)

@cli.command()
@click.option('--clear', is_flag=True, help='Clear cache to free up disk space')
def cache(clear):
    """Manage the cache used for storing WandB data."""
    cache_command(wandb_api, clear)

@cli.command()
def help():
    """Show help information."""
    help_command()

if __name__ == "__main__":
    try:
        cli()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)
