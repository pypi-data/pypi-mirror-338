import os
from pathlib import Path

from ..ui.console import (
    console, get_progress_columns, create_panel, create_table,
    display_error, display_info, display_success, display_warning,
    Progress
)
from ..config import DATA_DIR, CACHE_DIR

def list_command(wandb_api):
    console.print(create_panel("[bold cyan]Saved Runs[/bold cyan]"))
    
    if not DATA_DIR.exists():
        display_warning("No saved runs found")
        return
        
    # Get list of run directories
    run_dirs = [d for d in DATA_DIR.iterdir() if d.is_dir() and not d.name.startswith('.')]
    
    if not run_dirs:
        display_warning("No saved runs found")
        return
        
    # Create table of runs
    table = create_table(columns=[
        ("#", "cyan"),
        ("Run Name", "green"),
        ("Report File", "yellow"),
        ("Graphs", "magenta")
    ])
    
    for i, run_dir in enumerate(sorted(run_dirs), 1):
        # Count number of PNG files in the run directory
        png_files = list(run_dir.glob("**/*.png"))
        num_graphs = len(png_files)
        
        # Check if report file exists
        report_file = run_dir / f"{run_dir.name}.md"
        report_status = "✅" if report_file.exists() else "❌"
        
        table.add_row(
            str(i),
            run_dir.name,
            report_status,
            str(num_graphs)
        )
    
    console.print(table)
    display_info(f"Total saved runs: {len(run_dirs)}")

def cache_command(wandb_api, clear=False):
    console.print(create_panel("[bold cyan]Cache Statistics[/bold cyan]"))
    
    if not CACHE_DIR.exists():
        display_info("Cache directory does not exist")
        return
        
    # Get list of cache files
    cache_files = list(CACHE_DIR.glob("*.json"))
    
    # Calculate total size
    total_size = sum(f.stat().st_size for f in cache_files)
    total_size_mb = total_size / (1024 * 1024)
    
    display_info(f"Cache directory: {CACHE_DIR}")
    display_info(f"Number of cached runs: {len(cache_files)}")
    display_info(f"Total cache size: {total_size_mb:.2f} MB")
    
    if clear:
        display_warning("Clearing cache...")
        for f in cache_files:
            try:
                f.unlink()
            except Exception as e:
                display_error(f"Failed to remove {f}: {e}")
        display_success("Cache cleared successfully")

def metrics_command(wandb_api, run_url, force_refresh):
    if not wandb_api.logged_in:
        display_error("Not logged in to WandB. Please run 'login' first.")
        return
    
    display_info(f"Fetching metrics for run: {run_url}")
    
    with Progress(*get_progress_columns()) as progress:
        task = progress.add_task("[cyan]Fetching run...", total=1)
        run = wandb_api.get_run(run_url, use_cache=not force_refresh)
        progress.update(task, advance=1)
    
    if not run:
        display_error("Failed to fetch run. Please check the URL and try again.")
        return
        
    with Progress(*get_progress_columns()) as progress:
        task = progress.add_task("[cyan]Fetching metrics...", total=1)
        metrics = wandb_api.get_available_metrics(run)
        progress.update(task, advance=1)
    
    if metrics:
        table = create_table(title=f"Available Metrics for Run: {run.name}", columns=[
            ("Metric Name", "cyan")
        ])
        
        for metric in metrics:
            table.add_row(metric)
        
        console.print(table)
    else:
        display_warning("No metrics found for this run.")

def help_command():
    console.print(create_panel("[bold cyan]WandB Logger Help[/bold cyan]"))
    console.print("Available commands:")
    console.print("  [bold]login[/bold] - Log in to your WandB account")
    console.print("  [bold]logout[/bold] - Log out from your WandB account")
    console.print("  [bold]status[/bold] - Check your WandB login status")
    console.print("  [bold]fetch [RUN_URL][/bold] - Fetch logs and graphs from a specific WandB run")
    console.print("    [bold]--metrics, -m[/bold] - Specify metrics to fetch (can be used multiple times)")
    console.print("    [bold]--force-refresh, -f[/bold] - Force refresh data from WandB (ignore cache)")
    console.print("    [bold]--select/--no-select, -s/-n[/bold] - Toggle interactive metric selection (default: off)")
    console.print("    [bold]--clean, -c[/bold] - Clean up existing graph files before generating new ones")
    console.print("  [bold]recent[/bold] - Fetch and select from your recent WandB runs")
    console.print("    [bold]--limit, -l[/bold] - Maximum number of recent runs to show (default: 10)")
    console.print("    [bold]--metrics, -m[/bold] - Specify metrics to fetch (can be used multiple times)")
    console.print("    [bold]--force-refresh, -f[/bold] - Force refresh data from WandB (ignore cache)")
    console.print("    [bold]--select/--no-select, -s/-n[/bold] - Toggle interactive metric selection (default: on)")
    console.print("    [bold]--clean, -c[/bold] - Clean up existing graph files before generating new ones")
    console.print("  [bold]list[/bold] - List all saved runs")
    console.print("  [bold]metrics [RUN_URL][/bold] - List available metrics for a WandB run")
    console.print("    [bold]--force-refresh, -f[/bold] - Force refresh data from WandB (ignore cache)")
    console.print("  [bold]cache[/bold] - Show cache statistics")
    console.print("    [bold]--clear[/bold] - Clear cache to free up disk space")
    console.print("  [bold]help[/bold] - Show this help information")
    
    console.print("\nExample workflow:")
    console.print("  1. Login to WandB: [bold]wandb-logger login[/bold]")
    console.print("  2. View recent runs: [bold]wandb-logger recent[/bold]")
    console.print("  3. Or fetch a specific run: [bold]wandb-logger fetch https://wandb.ai/username/project/runs/run_id --select[/bold]")
    console.print("  4. Refresh with clean option: [bold]wandb-logger fetch https://wandb.ai/username/project/runs/run_id --select --clean[/bold]")
    console.print("  5. List saved runs: [bold]wandb-logger list[/bold]") 