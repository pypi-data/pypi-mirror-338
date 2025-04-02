import click
from datetime import datetime, timezone
import time

from ..ui.console import (
    console, create_panel, create_table,
    display_error, display_success, display_info,
    display_warning, ask_confirmation, ask_input, Progress,
    get_progress_columns
)
from ..config import DEFAULT_LIMIT
from .fetch_command import fetch_run

def recent_runs_command(wandb_api, limit=DEFAULT_LIMIT, metrics=None, force_refresh=False, select=True, clean=False, project=None, entity=None, max_projects=3, all_projects=False):
    """Display a list of recent runs across all projects or a specific project and allow selecting one."""
    if not wandb_api.logged_in:
        display_error("Not logged in to WandB. Please run 'login' first.")
        return

    console.print(create_panel("[bold cyan]Recent WandB Runs[/bold cyan]"))
    
    try:
        # Get all runs for the current user, or runs from a specific project
        start_time = time.time()
        
        # Get the API and check current user info
        api = wandb_api.api
        try:
            # The viewer property returns a User object directly
            current_user = api.viewer.entity
            display_info(f"Logged in as: [bold green]{current_user}[/bold green]")
            
            # Use provided entity or default to current user
            entity_to_use = entity or current_user
            display_info(f"Fetching runs for entity: [bold green]{entity_to_use}[/bold green]")
        except Exception as e:
            # If we can't get the current user, just use the provided entity or warn
            display_warning(f"Could not determine current user: {e}")
            if entity:
                entity_to_use = entity
                display_info(f"Using provided entity: [bold green]{entity_to_use}[/bold green]")
            else:
                display_error("Could not determine user and no entity provided. Please specify --entity.")
                return
        
        if project:
            display_info(f"Fetching runs in project: [bold cyan]{project}[/bold cyan] (limit: {limit})...")
            # Get runs from the specific project
            runs = api.runs(f"{entity_to_use}/{project}", per_page=limit)
        else:
            # Get runs from all projects
            runs = []
            projects = []
            projects_loaded = False
            
            try:
                # Get all projects for the specified entity
                # Manually collect projects since the iterator may not support length
                try:
                    projects_to_fetch = []
                    for project in api.projects(entity=entity_to_use):
                        projects.append(project)
                    projects_loaded = True
                    
                    # If we have projects, sort them by last updated time if possible
                    if projects:
                        # Try to sort projects by updated time, if available
                        try:
                            projects.sort(
                                key=lambda p: getattr(p, 'last_update_time', 
                                                     getattr(p, 'updated_at', 
                                                            getattr(p, 'created_at', ''))), 
                                reverse=True
                            )
                        except Exception as sort_e:
                            display_warning(f"Could not sort projects by time: {sort_e}")
                        
                        # Limit the number of projects if not fetching all
                        if not all_projects and len(projects) > max_projects:
                            display_info(f"Limiting to {max_projects} most recent projects out of {len(projects)} total")
                            display_info(f"Use --all-projects to fetch from all projects")
                            projects_to_fetch = projects[:max_projects]
                        else:
                            projects_to_fetch = projects
                            if len(projects) > 3:
                                display_info(f"Fetching from all {len(projects)} projects (this may take a while)")
                    
                except Exception as e:
                    display_warning(f"Error iterating projects: {e}")
                    # Try alternative approach - get runs directly
                    if entity:
                        display_info(f"Trying to get runs directly for entity: {entity_to_use}")
                        try:
                            direct_runs = list(api.runs(f"{entity_to_use}/", per_page=limit))
                            if direct_runs:
                                runs = direct_runs
                                display_success(f"Successfully fetched {len(runs)} runs directly")
                                # Skip the rest of the project-based fetching
                                projects_loaded = False
                            else:
                                display_warning("No runs found when fetching directly")
                        except Exception as direct_e:
                            display_warning(f"Failed to get runs directly: {direct_e}")
                    
                    if not runs:
                        display_error("Could not list projects or get runs directly")
                        return
                
                if projects_loaded:
                    if not projects:
                        display_warning(f"No projects found for entity: {entity_to_use}")
                        return
                        
                    display_info(f"Found {len(projects)} projects for {entity_to_use}")
                    
                    if not projects_to_fetch:
                        projects_to_fetch = projects
                    
                    per_project_limit = max(3, limit // len(projects_to_fetch) + 1)
                    display_info(f"Fetching up to {per_project_limit} runs per project")
                    
                    with Progress(*get_progress_columns()) as progress:
                        task = progress.add_task("[cyan]Fetching runs from projects...", total=len(projects_to_fetch))
                        
                        for project in projects_to_fetch:
                            try:
                                # Get entity and project name
                                entity_name = getattr(project, 'entity', entity_to_use)
                                project_name = getattr(project, 'name', project)
                                
                                # Get runs for this project
                                project_runs = api.runs(f"{entity_name}/{project_name}", per_page=per_project_limit)
                                runs.extend(list(project_runs))
                                progress.update(task, advance=1)
                            except Exception as e:
                                project_name = getattr(project, 'name', str(project))
                                display_warning(f"Error fetching runs for project {project_name}: {e}")
                                progress.update(task, advance=1)
                                continue

                # Sort all runs by created_at (newest first) and limit
                # Define a sorting function that handles missing created_at values
                def sort_key(run):
                    # First try created_at
                    if hasattr(run, 'created_at') and run.created_at:
                        return run.created_at
                    
                    # Then try _created_at
                    if hasattr(run, '_created_at') and run._created_at:
                        return run._created_at
                    
                    # Try other timestamp attributes
                    for attr in ['timestamp', 'updated_at', 'started_at']:
                        if hasattr(run, attr) and getattr(run, attr):
                            return getattr(run, attr)
                    
                    # Return empty string as last resort
                    return ""
                
                # Sort the runs
                runs.sort(key=sort_key, reverse=True)
                
                # Limit the number of runs
                if len(runs) > limit:
                    runs = runs[:limit]
            except Exception as e:
                display_error(f"Error listing projects: {e}")
                return
        
        display_success(f"Found {len(runs)} runs in {time.time() - start_time:.2f}s")
        
        if not runs:
            display_warning("No runs found.")
            return
            
        # Display runs in a table
        table = create_table("Recent Runs", [
            ("ID", "dim"),
            ("Name", "cyan"),
            ("Project", "green"),
            ("Entity", "blue"),
            ("Created", "yellow"),
            ("Status", "magenta")
        ])
        
        # Add each run to the table
        run_map = {}
        for i, run in enumerate(runs, 1):
            try:
                # Safely get run attributes with fallbacks
                run_id = getattr(run, 'id', 'unknown_id')
                run_name = getattr(run, 'name', 'unnamed_run')
                project_name = getattr(run, 'project', 'unknown_project')
                entity_name = getattr(run, 'entity', entity_to_use)
                
                # Format the created_at time
                created_at = getattr(run, 'created_at', None)
                if created_at:
                    try:
                        # Try to treat it as a datetime object
                        if hasattr(created_at, 'tzinfo'):
                            # Handle timezone if present
                            if created_at.tzinfo:
                                created_at = created_at.astimezone(timezone.utc).replace(tzinfo=None)
                            # Format as a readable string
                            created_at_str = created_at.strftime("%Y-%m-%d %H:%M:%S")
                        else:
                            # If it doesn't have tzinfo, it's probably a string
                            created_at_str = str(created_at)
                    except (AttributeError, TypeError):
                        # If any attribute errors occur, fall back to string representation
                        created_at_str = str(created_at)
                else:
                    created_at_str = "Unknown"
                    
                # Get the run status
                status = getattr(run, 'state', None)
                if status is None:
                    # Try alternative attribute names
                    for attr in ['status', '_status', 'run_status']:
                        if hasattr(run, attr):
                            status = getattr(run, attr)
                            break
                
                # If still None, use 'Unknown'
                if status is None:
                    status = "Unknown"
                
                # Add to the table
                table.add_row(
                    str(i),
                    run_name,
                    project_name,
                    entity_name,
                    created_at_str,
                    status
                )
                
                # Store the run for later selection
                run_map[i] = {
                    'id': run_id,
                    'name': run_name,
                    'project': project_name,
                    'entity': entity_name,
                    'url': f"https://wandb.ai/{entity_name}/{project_name}/runs/{run_id}"
                }
            except Exception as e:
                display_warning(f"Error processing run {i}: {e}")
                continue
        
        # Display the table
        console.print(table)
        
        # Allow user to select a run
        selected_run = None
        while True:
            choice = ask_input("Enter run number to fetch (or 'q' to quit)", default="q")
            if choice.lower() == 'q':
                return
            
            try:
                run_num = int(choice)
                if run_num in run_map:
                    selected_run = run_map[run_num]
                    break
                else:
                    display_error(f"Invalid run number: {run_num}. Valid range: 1-{len(run_map)}")
            except ValueError:
                display_error(f"Invalid input: {choice}. Please enter a number or 'q'.")
        
        if selected_run:
            # Fetch the selected run
            display_success(f"Selected run: {selected_run['name']} ({selected_run['project']})")
            fetch_run(wandb_api, selected_run['url'], metrics, force_refresh, select, clean)
    
    except Exception as e:
        display_error(f"Error fetching recent runs: {e}")
        import traceback
        console.print(traceback.format_exc()) 