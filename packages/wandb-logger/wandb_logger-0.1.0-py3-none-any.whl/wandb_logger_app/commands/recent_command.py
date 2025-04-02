from datetime import datetime
import click

from ..ui.console import (
    console, get_progress_columns, create_panel, create_table,
    display_error, display_success, display_warning, 
    ask_confirmation, ask_input, Progress
)
from ..config import DEFAULT_LIMIT
from .fetch_command import fetch_run

def recent_command(wandb_api, limit, metrics, force_refresh, select, clean):
    if not wandb_api.logged_in:
        display_error("Not logged in to WandB. Please run 'login' first.")
        return

    console.print(create_panel("[bold cyan]Recent WandB Runs[/bold cyan]"))
    
    with Progress(*get_progress_columns()) as progress:
        task = progress.add_task("[cyan]Fetching recent runs...", total=1)
        runs = wandb_api.get_recent_runs(limit=limit)
        progress.update(task, advance=1)
    
    if not runs:
        display_warning("No recent runs found. Try logging in again or check your WandB account.")
        
        # Provide a fallback option to manually enter a run URL
        console.print("\n[bold cyan]Would you like to manually enter a run URL instead?[/bold cyan]")
        if ask_confirmation("Enter a run URL manually?"):
            run_url = ask_input("Enter the WandB run URL (e.g., https://wandb.ai/username/project/runs/run_id)")
            
            # Basic validation
            if not run_url.startswith("https://wandb.ai/") or "/runs/" not in run_url:
                display_error("Invalid URL format. Should be https://wandb.ai/username/project/runs/run_id")
                return
                
            # Proceed with fetch using the manually entered URL
            display_success(f"Using manually entered run URL: {run_url}")
            fetch_run(wandb_api, run_url, metrics, force_refresh, select, clean)
        return
    
    # Display the runs with indices
    console.print("\n[bold cyan]Your Recent Runs:[/bold cyan]")
    
    table = create_table(columns=[
        ("#", "cyan"),
        ("Run Name", "green"),
        ("Project", "yellow"),
        ("Created", "magenta")
    ])
    
    for i, run in enumerate(runs, 1):
        created_at = run.get("created_at", "Unknown")
        # Format datetime if it's a string
        if isinstance(created_at, str):
            # Try to format it nicely, but fall back to original string if parsing fails
            try:
                dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                created_at = dt.strftime("%Y-%m-%d %H:%M")
            except Exception:
                pass
                
        table.add_row(
            str(i),
            run.get("name", "Unnamed"),
            f"{run.get('project', 'Unknown')} ({run.get('entity', 'Unknown')})",
            str(created_at)
        )
    
    console.print(table)
    
    # Ask user which run to select
    console.print("\n[cyan]Select a run to fetch (or 'q' to quit):[/cyan]")
    choice = ask_input("Enter run number", default="q")
    
    if choice.lower() == 'q':
        return
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(runs):
            selected_run = runs[idx]
            run_url = selected_run["url"]
            display_success(f"Selected run: {selected_run['name']} ({run_url})")
            
            # Now call the fetch function with the selected run URL
            # Pass the command-line options to the fetch function
            fetch_run(wandb_api, run_url, metrics, force_refresh, select, clean)
        else:
            display_error("Invalid selection. Please choose a number from the list.")
    except ValueError:
        display_error("Invalid input. Please enter a number or 'q' to quit.") 