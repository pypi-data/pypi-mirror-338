import os
import subprocess
import platform
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('utils')

def get_editor():
    """Get the default text editor for the operating system"""
    if platform.system() == 'Windows':
        return os.environ.get('EDITOR', 'notepad.exe')
    elif platform.system() == 'Darwin':  # macOS
        return os.environ.get('EDITOR', 'open -a TextEdit')
    else:  # Linux and others
        return os.environ.get('EDITOR', 'nano')

def open_file_in_editor(file_path):
    """Open a file in the default text editor"""
    if not file_path.exists():
        logger.error(f"File {file_path} does not exist")
        return False
        
    editor = get_editor()
    try:
        if platform.system() == 'Windows':
            os.startfile(file_path)
        elif platform.system() == 'Darwin':  # macOS
            subprocess.run(['open', '-a', 'TextEdit', file_path])
        else:  # Linux and others
            subprocess.run([editor, file_path])
        logger.info(f"Opened {file_path} in {editor}")
        return True
    except Exception as e:
        logger.error(f"Failed to open file in editor: {e}")
        return False

def list_saved_runs(data_dir):
    """List all saved runs in the data directory"""
    data_dir = Path(data_dir)
    if not data_dir.exists():
        logger.warning(f"Data directory {data_dir} does not exist")
        return []
        
    runs = [d for d in data_dir.iterdir() if d.is_dir()]
    return runs

def get_markdown_file_for_run(data_dir, run_name):
    """Get the markdown file for a specific run"""
    data_dir = Path(data_dir)
    run_dir = data_dir / run_name
    
    if not run_dir.exists():
        logger.error(f"Run directory {run_dir} does not exist")
        return None
        
    md_files = list(run_dir.glob(f"{run_name}.md"))
    if not md_files:
        logger.error(f"No markdown file found for run {run_name}")
        return None
        
    return md_files[0]

def format_run_info(run_dir):
    """Format run information for display"""
    run_name = run_dir.name
    md_file = get_markdown_file_for_run(run_dir.parent, run_name)
    
    if md_file and md_file.exists():
        return f"{run_name} (Has markdown: Yes)"
    else:
        return f"{run_name} (Has markdown: No)"
