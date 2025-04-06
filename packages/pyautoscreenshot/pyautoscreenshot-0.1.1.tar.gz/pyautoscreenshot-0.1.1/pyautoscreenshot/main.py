# requires-python = ">=3.9"
# dependencies = [
#     "pyautogui",
#     "pillow",
#     "typer",
# ]

import os
import time
import threading
from datetime import datetime
from pathlib import Path
from typing import Optional

import pyautogui
import typer
from loguru import logger

app = typer.Typer(help="Auto Screen Print - Capture screenshots at regular intervals")

# Global variables to control screenshot capture
capturing = False
capture_thread = None


def take_screenshot(output_path: Path, prefix: str) -> str:
    """Take a screenshot and save it with timestamp"""
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{current_time}.png"
    filepath = output_path / filename
    
    # Ensure the directory exists
    os.makedirs(output_path, exist_ok=True)
    
    # Capture the screen
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    logger.debug(f"Screenshot saved: {filepath}")


    return str(filepath)

@app.command()
def run(
    output_path: str = typer.Option("./screenshots", "--output", "-o", help="Directory to save screenshots"),
    prefix: str = typer.Option("screenshot", "--prefix", "-p", help="Prefix for screenshot filenames"),
    interval: int = typer.Option(10, "--interval", "-i", help="Capture interval in seconds")
):
    """Run screenshot capture with specified options"""
    output_dir = Path(output_path)
    
    typer.echo(f"Running screenshot capture:")
    typer.echo(f"  Output directory: {output_dir}")
    typer.echo(f"  Filename prefix: {prefix}")
    typer.echo(f"  Capture interval: {interval} seconds")
    
    try:
        while True:
            filepath = take_screenshot(output_dir, prefix)
            typer.echo(f"Screenshot saved: {filepath}")
            time.sleep(interval)
    except KeyboardInterrupt:
        typer.echo("Screenshot capture stopped by user.")


def main():
    app()


if __name__ == "__main__":
    main()