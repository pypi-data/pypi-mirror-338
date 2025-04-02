from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn, SpinnerColumn
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

console = Console()

def get_progress_columns():
    return [
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn()
    ]

def create_table(title=None, columns=None):
    table = Table(title=title)
    if columns:
        for col_name, style in columns:
            table.add_column(col_name, style=style)
    return table

def create_panel(text, title=None):
    return Panel(text, title=title)

def display_error(message):
    console.print(f"[bold red]{message}[/bold red]")

def display_success(message):
    console.print(f"[bold green]{message}[/bold green]")

def display_info(message):
    console.print(f"[cyan]{message}[/cyan]")

def display_warning(message):
    console.print(f"[yellow]{message}[/yellow]")

def ask_confirmation(message, default=False):
    return Confirm.ask(message, default=default)

def ask_input(message, default=None):
    return Prompt.ask(message, default=default) 