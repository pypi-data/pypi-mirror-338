import click

from wandb_logger_app.ui.console import (
    console, create_panel, 
    display_error, display_success, display_info,
    ask_input
)

def login_command(wandb_api, api_key=None):
    console.print(create_panel("[bold cyan]WandB Login[/bold cyan]"))
    
    if wandb_api.logged_in:
        display_info("Already logged in to WandB")
        return
    
    if not api_key:
        display_info("Please provide your WandB API key.")
        display_info("You can find your API key at: https://wandb.ai/settings")
        api_key = ask_input("WandB API Key (press Enter to open browser login)")
        
        if not api_key:
            api_key = None  # Empty string should trigger browser login
    
    if wandb_api.login(api_key):
        display_success("Successfully logged in to WandB")
    else:
        display_error("Failed to log in to WandB. Please check your API key and try again.")

def logout_command(wandb_api):
    console.print(create_panel("[bold cyan]WandB Logout[/bold cyan]"))
    
    if not wandb_api.logged_in:
        display_info("Not currently logged in to WandB")
        return
    
    if wandb_api.logout():
        display_success("Successfully logged out from WandB")
    else:
        display_error("Failed to log out from WandB")

def status_command(wandb_api):
    console.print(create_panel("[bold cyan]WandB Status[/bold cyan]"))
    
    if wandb_api.logged_in:
        try:
            username = wandb_api.api.default_entity
            display_success(f"Logged in as: {username}")
        except Exception:
            display_success("Logged in to WandB")
    else:
        display_info("Not logged in to WandB")
        display_info("Run 'login' to log in to your WandB account") 