import os
import wandb
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import re
from PIL import Image
import io
import logging
import json
import time
import concurrent.futures
from functools import lru_cache
from io import StringIO
from .config import CONFIG_FILE

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('wandb_api')

class WandbAPI:
    def __init__(self, data_dir='data'):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.api = None
        self.logged_in = False
        self.config_path = CONFIG_FILE
        self._load_login_state()
        self.cache_dir = self.data_dir / '.cache'
        self.cache_dir.mkdir(exist_ok=True)
        self.max_workers = os.cpu_count() or 4  # Default to 4 if CPU count is None

    def _save_login_state(self):
        """Save login state to config file"""
        try:
            with open(self.config_path, 'w') as f:
                json.dump({"logged_in": self.logged_in}, f)
            logger.debug("Saved login state")
        except Exception as e:
            logger.error(f"Failed to save login state: {e}")

    def _load_login_state(self):
        """Load login state from config file"""
        if not self.config_path.exists():
            return

        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
                self.logged_in = config.get("logged_in", False)
                
            if self.logged_in:
                try:
                    self.api = wandb.Api()
                    logger.info("Restored login state from saved configuration")
                except Exception as e:
                    logger.error(f"Failed to initialize WandB API: {e}")
                    self.logged_in = False
                    self._save_login_state()
        except Exception as e:
            logger.error(f"Failed to load login state: {e}")

    def login(self, api_key=None):
        """Login to WandB with API key"""
        try:
            if api_key:
                wandb.login(key=api_key)
            else:
                wandb.login()
            self.api = wandb.Api()
            self.logged_in = True
            self._save_login_state()
            logger.info("Successfully logged in to WandB")
            return True
        except Exception as e:
            logger.error(f"Failed to log in to WandB: {e}")
            return False

    def logout(self):
        """Logout from WandB"""
        self.logged_in = False
        self.api = None
        self._save_login_state()
        logger.info("Logged out from WandB")
        return True

    def parse_run_url(self, url):
        """Parse WandB run URL to extract entity, project, and run ID"""
        pattern = r'wandb\.ai/([^/]+)/([^/]+)/runs/([^/]+)'
        match = re.search(pattern, url)
        
        if not match:
            logger.error(f"Invalid WandB URL format: {url}")
            return None, None, None
            
        entity, project, run_id = match.groups()
        return entity, project, run_id

    def _get_cache_path(self, run_id):
        """Get cache file path for a run"""
        return self.cache_dir / f"{run_id}.json"

    def _save_to_cache(self, run, run_id):
        """Save run data to cache"""
        cache_path = self._get_cache_path(run_id)
        try:
            # Convert history dataframe to json for caching
            history_df = run.history()
            
            cache_data = {
                "name": run.name,
                "id": run.id,
                "project": run.project,
                "entity": run.entity,
                "created_at": str(run.created_at),
                "config": dict(run.config) if hasattr(run, 'config') else {},
                "history": history_df.to_json(orient='split')
            }
            
            with open(cache_path, 'w') as f:
                json.dump(cache_data, f)
                
            logger.debug(f"Saved run data to cache: {cache_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to save run data to cache: {e}")
            return False

    def _get_from_cache(self, run_id):
        """Get run data from cache"""
        cache_path = self._get_cache_path(run_id)
        
        if not cache_path.exists():
            return None
            
        try:
            with open(cache_path, 'r') as f:
                cache_data = json.load(f)
                
            # Create a simple object to mimic wandb run
            class CachedRun:
                pass
                
            run = CachedRun()
            run.name = cache_data.get("name")
            run.id = cache_data.get("id")
            run.project = cache_data.get("project")
            run.entity = cache_data.get("entity")
            run.created_at = cache_data.get("created_at")
            run.config = cache_data.get("config", {})
            
            # Convert history json back to dataframe
            # Use StringIO to avoid FutureWarning
            history_json = cache_data.get("history")
            run._history_df = pd.read_json(StringIO(history_json), orient='split')
            
            # Add a history method that returns the dataframe
            run.history = lambda: run._history_df
            
            logger.debug(f"Loaded run data from cache: {cache_path}")
            return run
        except Exception as e:
            logger.error(f"Failed to load run data from cache: {e}")
            return None

    def get_run(self, run_url, use_cache=True):
        """Get WandB run from URL with caching"""
        if not self.logged_in:
            logger.error("Not logged in to WandB")
            return None
            
        entity, project, run_id = self.parse_run_url(run_url)
        if not all([entity, project, run_id]):
            return None
        
        # Try to get from cache first
        if use_cache:
            cached_run = self._get_from_cache(run_id)
            if cached_run:
                logger.info(f"Using cached run data for: {cached_run.name}")
                return cached_run
            
        # If not in cache or cache disabled, fetch from API
        try:
            start_time = time.time()
            run = self.api.run(f"{entity}/{project}/{run_id}")
            logger.info(f"Successfully fetched run: {run.name} in {time.time() - start_time:.2f}s")
            
            # Save to cache for future use
            self._save_to_cache(run, run_id)
            
            return run
        except Exception as e:
            logger.error(f"Failed to fetch run: {e}")
            return None

    def get_available_metrics(self, run):
        """Get list of available metrics in the run"""
        try:
            history_df = run.history()
            metrics = history_df.columns.tolist()
            return metrics
        except Exception as e:
            logger.error(f"Failed to get metrics: {e}")
            return []

    def save_run_graph(self, run, metric_name, output_dir=None):
        """Save a graph for a specific metric"""
        if not output_dir:
            output_dir = self.data_dir / run.name
            
        output_dir.mkdir(exist_ok=True, parents=True)
        
        try:
            start_time = time.time()
            history_df = run.history()
            
            if metric_name not in history_df.columns:
                logger.error(f"Metric {metric_name} not found in run data")
                return None
            
            # Log data for debugging
            logger.debug(f"Creating graph for metric: {metric_name}")
            logger.debug(f"Data shape: {history_df[metric_name].shape}")
                
            plt.figure(figsize=(10, 6))
            plt.plot(history_df[metric_name])
            plt.title(f"{metric_name} - {run.name}")
            plt.xlabel('Step')
            plt.ylabel(metric_name)
            plt.grid(True)
            
            # Handle metrics with path-like names (e.g., "train/rewards/metric")
            # Create a safe filename by replacing directory separators
            safe_metric_filename = metric_name.replace('/', '_').replace('\\', '_')
            
            # Save the figure to a file
            image_path = output_dir / f"{safe_metric_filename}.png"
            
            # Ensure parent directory exists
            image_path.parent.mkdir(exist_ok=True, parents=True)
            
            plt.savefig(image_path, dpi=100)  # Lower DPI for faster saving
            plt.close()
            
            logger.info(f"Saved graph to {image_path} in {time.time() - start_time:.2f}s")
            return (image_path, metric_name)  # Return tuple with path and original metric name
        except Exception as e:
            logger.error(f"Failed to save graph for metric '{metric_name}': {e}")
            import traceback
            logger.error(traceback.format_exc())
            return None

    def create_markdown_files(self, run, graph_data, selected_metrics=None):
        """Create markdown files with run information and graphs
        
        Creates two files:
        - metadata.md: Contains all run information and configuration
        - report.md: Contains only the selected graphs for clean reporting
        
        Args:
            run: WandB run object
            graph_data: List of tuples (path, original_metric_name)
            selected_metrics: List of selected metric names
        """
        output_dir = self.data_dir / run.name
        output_dir.mkdir(exist_ok=True, parents=True)
        
        # Create metadata file with all run information
        metadata_path = output_dir / "metadata.md"
        
        try:
            # Create metadata file with run information
            with open(metadata_path, 'w') as f:
                f.write(f"# Run Metadata: {run.name}\n\n")
                f.write(f"## Run Information\n\n")
                f.write(f"- **ID**: {run.id}\n")
                f.write(f"- **Project**: {run.project}\n")
                f.write(f"- **Entity**: {run.entity}\n")
                f.write(f"- **Created**: {run.created_at}\n")
                
                if hasattr(run, 'config') and run.config:
                    f.write(f"\n## Configuration\n\n")
                    for key, value in run.config.items():
                        f.write(f"- **{key}**: {value}\n")
                
                f.write(f"\n## Available Metrics\n\n")
                history_df = run.history()
                for metric in history_df.columns:
                    f.write(f"- {metric}\n")
                
                if selected_metrics:
                    f.write(f"\n## Selected Metrics\n\n")
                    for metric in selected_metrics:
                        f.write(f"- {metric}\n")
            
            logger.info(f"Created metadata file at {metadata_path}")
            
            # Create report file with only selected graphs
            report_path = output_dir / f"{run.name}.md"
            
            with open(report_path, 'w') as f:
                f.write(f"# Run Report: {run.name}\n\n")
                
                if not graph_data:
                    f.write("No graphs were selected for this report.\n\n")
                else:
                    # Sort graph data by original metric name
                    sorted_graph_data = sorted(graph_data, key=lambda x: x[1] if x else "")
                    
                    for path, metric_name in sorted_graph_data:
                        if path and metric_name:
                            # For display in headers, replace slashes with spaces and title-case
                            display_name = metric_name.replace('/', ' → ').replace('_', ' ').title()
                            
                            f.write(f"\n## {display_name}\n\n")
                            
                            # Use just the filename for the image path since it's in the same directory
                            image_filename = path.name
                            f.write(f"![{metric_name}]({image_filename})\n\n")
                
                f.write(f"\n## Notes and Insights\n\n")
                f.write("Add your notes and insights here.\n\n")
                
                f.write(f"\n---\n\n")
                f.write(f"*See [metadata.md](metadata.md) for detailed run information.*\n")
            
            logger.info(f"Created report file at {report_path}")
            return report_path
        except Exception as e:
            logger.error(f"Failed to create markdown files: {e}")
            return None

    def _save_run_graph_wrapper(self, args):
        """Wrapper for save_run_graph to use with concurrent.futures"""
        run, metric = args
        return self.save_run_graph(run, metric)

    def fetch_and_save_run(self, run_url, metrics=None, use_cache=True, selected_metrics=None):
        """Fetch run data and save graphs and markdown using parallel processing
        
        Args:
            run_url: URL of the WandB run
            metrics: List of metrics to generate graphs for (if None, all metrics are used)
            use_cache: Whether to use cached run data
            selected_metrics: List of metrics to include in the report (if None, all generated graphs are included)
        """
        start_time = time.time()
        run = self.get_run(run_url, use_cache=use_cache)
        if not run:
            return None, None
            
        if not metrics:
            available_metrics = self.get_available_metrics(run)
            metrics = available_metrics
        
        # Log metrics and selections for debugging
        logger.info(f"Available metrics: {metrics}")
        logger.info(f"Selected metrics: {selected_metrics}")
        
        # Determine which metrics to generate graphs for
        metrics_to_graph = selected_metrics if selected_metrics else metrics
        
        if not metrics_to_graph:
            logger.warning("No metrics selected for graphing")
            # Create empty report and metadata
            md_path = self.create_markdown_files(run, [], selected_metrics)
            return run.name, md_path
            
        logger.info(f"Generating graphs for {len(metrics_to_graph)} selected metrics: {metrics_to_graph}")
        
        graph_data = []
        
        # Use sequential processing for better error visibility
        for metric in metrics_to_graph:
            logger.info(f"Processing metric: {metric}")
            result = self._save_run_graph_wrapper((run, metric))
            if result:
                logger.info(f"Successfully created graph for: {metric}")
                graph_data.append(result)
            else:
                logger.error(f"Failed to create graph for: {metric}")
        
        logger.info(f"Generated {len(graph_data)} graph files out of {len(metrics_to_graph)} requested")
        
        md_path = self.create_markdown_files(run, graph_data, selected_metrics)
        
        logger.info(f"Total processing time: {time.time() - start_time:.2f}s")
        return run.name, md_path

    def get_recent_runs(self, limit=10):
        """Fetch the user's recent runs across all projects
        
        Args:
            limit: Maximum number of runs to fetch
            
        Returns:
            List of run objects containing name, project, entity, id, and URL
        """
        if not self.logged_in:
            logger.error("Not logged in to WandB")
            return []
            
        try:
            # Get list of projects for the current user
            runs = []
            
            # Get current user's username
            username = self.api.default_entity
            logger.info(f"Fetching runs for user: {username}")
            
            # Collect projects one by one
            projects = []
            try:
                for project in self.api.projects(entity=username):
                    projects.append(project)
            except Exception as e:
                logger.warning(f"Error collecting projects: {e}")
                
            if projects:
                logger.info(f"Found {len(projects)} projects for user {username}")
                
                # Fetch runs from each project, sorted by creation date
                for project in projects:
                    try:
                        # Calculate per_page to distribute limit fairly among projects
                        per_page = max(3, limit // len(projects))
                        
                        project_runs = []
                        for run in self.api.runs(
                            path=f"{project.entity}/{project.name}",
                            order="-created_at",
                            per_page=per_page
                        ):
                            project_runs.append(run)
                            
                        for run in project_runs:
                            runs.append({
                                "name": run.name,
                                "project": run.project,
                                "entity": run.entity,
                                "id": run.id,
                                "url": f"https://wandb.ai/{run.entity}/{run.project}/runs/{run.id}",
                                "created_at": run.created_at,
                                "summary": run.summary._json_dict if hasattr(run.summary, "_json_dict") else {}
                            })
                    except Exception as e:
                        logger.warning(f"Error fetching runs for project {project.name}: {e}")
            
            # Sort all runs by creation date (newest first) and limit to requested number
            runs = sorted(runs, key=lambda x: x.get("created_at", ""), reverse=True)[:limit]
            
            logger.info(f"Fetched {len(runs)} recent runs")
            return runs
        except Exception as e:
            logger.error(f"Failed to fetch recent runs: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return []
