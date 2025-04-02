import time
from pathlib import Path
import click

from ..ui.console import (
    console, get_progress_columns, create_panel, 
    display_error, display_success, display_info, 
    display_warning, ask_confirmation, ask_input, Progress
)
from ..config import DATA_DIR

def fetch_command(wandb_api, run_url, metrics, force_refresh, select, clean):
    if not wandb_api.logged_in:
        display_error("Not logged in to WandB. Please run 'login' first.")
        return

    fetch_run(wandb_api, run_url, metrics, force_refresh, select, clean)

def fetch_run(wandb_api, run_url, metrics, force_refresh, select, clean):
    console.print(create_panel(f"[bold cyan]Fetching run: {run_url}[/bold cyan]"))
    
    start_time = time.time()
    
    # First, check if the run is valid before attempting to create graphs
    with Progress(*get_progress_columns()) as progress:
        task = progress.add_task("[cyan]Validating run...", total=1)
        run = wandb_api.get_run(run_url, use_cache=not force_refresh)
        progress.update(task, advance=1)
    
    if not run:
        display_error("Failed to fetch run. Please check the URL and try again.")
        return
    
    # Check if metrics exist in the run before creating graphs
    available_metrics = wandb_api.get_available_metrics(run)
    if not available_metrics:
        display_warning("No metrics found in this run.")
        return
    
    # When using select, automatically clean unless --clean=False is explicitly set
    if select and not clean:
        clean = True
        display_warning("Auto-enabling cleanup for selection mode")
    
    # Clean up existing files if requested
    if clean:
        run_dir = DATA_DIR / run.name
        if run_dir.exists():
            display_warning("Cleaning up existing graph files...")
            png_count = 0
            # Use ** pattern to search recursively for all PNG files
            for png_file in run_dir.glob("**/*.png"):
                try:
                    png_file.unlink()
                    png_count += 1
                except Exception as e:
                    display_error(f"Failed to remove {png_file}: {e}")
            
            if png_count > 0:
                display_success(f"Removed {png_count} existing graph files")
            else:
                display_warning("No existing graph files found")
                
            # Also remove the report file to ensure it's regenerated
            report_file = run_dir / f"{run.name}.md"
            if report_file.exists():
                try:
                    report_file.unlink()
                    display_success("Removed existing report file")
                except Exception as e:
                    display_error(f"Failed to remove report file: {e}")
    
    # If user specified metrics, validate they exist
    if metrics:
        metric_list = list(metrics)
        invalid_metrics = [m for m in metric_list if m not in available_metrics]
        if invalid_metrics:
            display_error(f"The following metrics were not found in the run: {', '.join(invalid_metrics)}")
            display_info("Available metrics:")
            for m in available_metrics:
                console.print(f"  - {m}")
            if not ask_confirmation("Do you want to continue with the valid metrics only?"):
                return
            metric_list = [m for m in metric_list if m in available_metrics]
    else:
        metric_list = available_metrics
    
    # Let user select which metrics to include in the report
    selected_metrics = None
    if select:
        console.print("\n[bold cyan]Select metrics to include in the report:[/bold cyan]")
        
        # Custom implementation of checkbox selection
        metric_choices = {i: metric for i, metric in enumerate(metric_list, 1)}
        
        # Default selects no metrics
        selected_indices = set()
        
        # Print instructions
        console.print("\n[yellow]Instructions:[/yellow]")
        console.print("- Type a number to toggle selection for that metric")
        console.print("- Type 'a' to select all metrics")
        console.print("- Type 'n' to deselect all metrics")
        console.print("- Type 'done' when finished selecting\n")
            
        while True:
            console.print("\n[bold cyan]Available metrics:[/bold cyan]")
            for idx, metric in metric_choices.items():
                selected = idx in selected_indices
                checkbox = "[bold green][X][/bold green]" if selected else "[bold red][ ][/bold red]"
                console.print(f"{idx}. {checkbox} {metric}")
                
            console.print("\n[cyan]Command[/cyan] (Type number to toggle, 'a'=all, 'n'=none, 'done'=finish):")
            choice = ask_input("Enter choice", default="done")
            
            if choice.lower() == "done":
                break
            elif choice.lower() == "a":
                selected_indices = set(metric_choices.keys())
            elif choice.lower() == "n":
                selected_indices = set()
            else:
                try:
                    idx = int(choice)
                    if idx in metric_choices:
                        if idx in selected_indices:
                            selected_indices.remove(idx)
                            display_error(f"Removed: {metric_choices[idx]}")
                        else:
                            selected_indices.add(idx)
                            display_success(f"Added: {metric_choices[idx]}")
                    else:
                        display_error(f"Invalid number: {idx}. Valid range: 1-{len(metric_choices)}")
                except ValueError:
                    display_error(f"Invalid input: {choice}")
        
        # Convert selected indices back to metric names
        selected_metrics = [metric_choices[idx] for idx in selected_indices]
        
        if not selected_metrics:
            display_warning("\nNo metrics selected.")
            if not ask_confirmation("Continue without any graphs?"):
                return
    
    with Progress(*get_progress_columns()) as progress:
        task1 = progress.add_task("[cyan]Fetching and processing metrics...", total=1)
        
        # Fetch and save run
        run_name, md_path = wandb_api.fetch_and_save_run(
            run_url, 
            metrics=metric_list, 
            use_cache=not force_refresh,
            selected_metrics=selected_metrics
        )
        progress.update(task1, advance=1)
        
    if run_name and md_path:
        display_success(f"Successfully fetched run: {run_name}")
        console.print(f"Report file created at: {md_path}")
        console.print(f"Metadata file created at: {(Path(md_path).parent / 'metadata.md')}")
        console.print(f"[cyan]Total processing time: {time.time() - start_time:.2f}s[/cyan]")
    else:
        display_error("Failed to create report file. Please check the logs for details.") 