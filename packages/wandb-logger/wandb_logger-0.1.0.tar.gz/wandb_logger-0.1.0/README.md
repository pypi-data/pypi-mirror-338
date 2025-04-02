# WandB Logger

**A sleek CLI tool that transforms how you work with Weights & Biases. Create your training report in a single-line command!**

![GitHub stars](https://img.shields.io/github/stars/SabaPivot/wandb-logger?style=social)
![PyPI version](https://img.shields.io/pypi/v/wandb-logger)
![License](https://img.shields.io/github/license/SabaPivot/wandb-logger-app)

<p align="center">
  <img src="https://your-image-url-here.png" alt="WandB Logger App Demo" width="600">
</p>

WandB Logger App is a sleek command-line tool that transforms how you work with Weights & Biases. Create beautiful, shareable reports of your ML experiments in seconds.

## 🚀 Key Features

WandB Logger offers two powerful ways to quickly access your experiments:

### 🔍 Find Your Experiments Without URLs
No more searching for run URLs or project names! WandB Logger makes finding your experiments effortless:

```bash
# Browse your recent projects
wandb-logger recent

# Browse your recent runs across all projects
wandb-logger recent-runs
```

This dual approach lets you quickly navigate through your work at both the project and individual run level - a huge productivity boost!

## ✨ Features

- 🔐 **Simple Authentication** - Quick login with WandB credentials
- 📈 **Beautiful Visualizations** - Fetch stunning graphs from any WandB run
- 📝 **Markdown Reports** - Generate elegant reports for easy sharing and embedding
- ⚡ **Lightning Fast** - Parallel processing and caching make everything snappy
- 🧠 **Smart Metric Handling** - Intelligently organizes complex metric paths
- 🎯 **Interactive Selection** - Pick exactly which metrics matter to you

## 🚀 Installation

```bash
# Install from PyPI
pip install wandb-logger-app

# Or install from source
git clone https://github.com/yourusername/wandb-logger-app.git
cd wandb-logger-app
pip install -e .
```

## 🏁 Quick Start

```bash
# Login to your WandB account
wandb-logger login

# MAIN WORKFLOWS:

# 1. Browse your recent PROJECTS (find the project you're looking for)
wandb-logger recent

# 2. Browse your recent RUNS (find the specific run you need)
wandb-logger recent-runs

# 3. Once you have a run URL, fetch detailed metrics
wandb-logger fetch https://wandb.ai/username/project/runs/run_id --select
```

## 📖 Commands

### Main Commands

| Command | Description | When to use |
|---------|-------------|-------------|
| `recent` | Browse and select from recent projects | When you remember the project name but not specific runs |
| `recent-runs` | Browse and select from recent runs | When you want to find a specific run without knowing its URL |
| `fetch URL` | Fetch details for a specific run URL | When you already have the run URL and want to analyze specific metrics |

### Options and Filters

| Command | Key Options |
|---------|-------------|
| `recent` | `--limit` (default: 10)<br>`--select` (interactive selection) |
| `recent-runs` | `--project` (filter by project)<br>`--entity` (filter by username/org)<br>`--max-projects` (default: 3)<br>`--all-projects` (fetch from all projects) |
| `fetch URL` | `--select` (enabled by default)<br>`--all` (fetch all metrics without selection)<br>`--metrics` (specify comma-separated metrics)<br>`--force-refresh` (bypass cache) |
| `metrics URL` | `--force-refresh` (bypass cache) |
| `cache` | `--clear` (free disk space) |

## 🎨 Interactive Metric Selection

The `fetch` command now defaults to interactive selection mode:

1. **Default Mode** (interactive selection):
```bash
# Opens an interactive menu to choose specific metrics
wandb-logger fetch https://wandb.ai/username/project/runs/run_id
```

2. **All Metrics Mode** (with `--all`):
```bash
# Fetches and plots ALL available metrics
wandb-logger fetch https://wandb.ai/username/project/runs/run_id --all
```

Select exactly what you want in your reports:

```
Available metrics:
1. [X] train/loss
2. [X] train/accuracy
3. [ ] validation/loss
4. [ ] validation/accuracy

Command (Type number to toggle, 'a'=all, 'n'=none, 'done'=finish):
```

## 📋 Example Workflows

### Tracking a Training Run

```bash
# Login first
wandb-logger login

# Fetch your latest run and create a report
wandb-logger recent --limit 1 --select
```

### Creating a Project Report

```bash
# Fetch multiple specific runs
wandb-logger fetch https://wandb.ai/username/project/runs/run_1
wandb-logger fetch https://wandb.ai/username/project/runs/run_2

# List your saved reports
wandb-logger list
```

## 🔍 Report Outputs

For each run, you'll get:

- **`<run_name>.md`**: Clean report with selected metrics and graphs
- **`metadata.md`**: Detailed configuration and all run information
- **Graph PNGs**: Individual visualizations for each metric

## 🚀 Performance Features

- **⚡ Caching**: Blazing fast repeated access to run data
- **⚙️ Parallel Processing**: Generates multiple graphs simultaneously
- **📊 Optimized Visualizations**: Beautiful graphs with minimal code
- **🧠 Smart Organization**: Automatic categorization of complex metrics

## 🛠️ Requirements

- Python 3.8+
- WandB account

## ⭐ Support

Like this project? Please give it a star on GitHub to show your support and help others discover it!