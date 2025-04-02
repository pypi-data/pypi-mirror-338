import os
from pathlib import Path

# Application paths
BASE_DIR = Path(__file__).parent
USER_HOME = Path.home() / '.wandb-logger'  # Store data in user's home directory
DATA_DIR = Path(__file__).parent / 'data'  # Store data in package directory
CONFIG_FILE = USER_HOME / '.wandb_config.json'
CACHE_DIR = DATA_DIR / '.cache'

# Ensure directories exist
for directory in [USER_HOME, DATA_DIR, CACHE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Performance settings
MAX_WORKERS = os.cpu_count() or 4  # Default to 4 if CPU count is None

# Display settings
DEFAULT_LIMIT = 10  # Default number of recent runs to show 