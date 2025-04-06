import os
import time
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest
from typer.testing import CliRunner
from pyautoscreenshot.main import take_screenshot, app


@pytest.fixture
def mock_datetime():
    with patch('main.datetime') as mock_dt:
        mock_dt.now.return_value.strftime.return_value = "20250404_120000"
        yield mock_dt


@pytest.fixture
def mock_pyautogui():
    with patch('main.pyautogui') as mock_pag:
        mock_screenshot = MagicMock()
        mock_pag.screenshot.return_value = mock_screenshot
        yield mock_pag


@pytest.fixture
def mock_logger():
    with patch('main.logger') as mock_log:
        yield mock_log


@pytest.fixture
def runner():
    return CliRunner()


def test_take_screenshot(tmp_path, mock_datetime, mock_pyautogui, mock_logger):
    # Test taking a screenshot
    result = take_screenshot(tmp_path, "test")
    
    # Check if pyautogui.screenshot was called
    mock_pyautogui.screenshot.assert_called_once()
    
    # Check if the screenshot was saved
    mock_pyautogui.screenshot.return_value.save.assert_called_once()
    
    # Check if the correct filename was used
    expected_path = tmp_path / "test_20250404_120000.png"
    assert result == str(expected_path)
    
    # Check if logger was called
    mock_logger.debug.assert_called_once()


def test_command_with_custom_options(tmp_path, mock_datetime, mock_pyautogui, mock_logger, runner):
    # Mock time.sleep to raise KeyboardInterrupt after first iteration
    def mock_sleep(seconds):
        raise KeyboardInterrupt()

    with patch('main.time.sleep', side_effect=mock_sleep):
        # Test with custom options
        with runner.isolated_filesystem():
            output_dir = str(Path('./test_screenshots'))
            result = runner.invoke(
                app, 
                ['--output', output_dir, '--prefix', 'test', '--interval', '5']
            )
            
            # Check exit code
            assert result.exit_code == 0
            
            # Check output contains expected messages
            assert "Running screenshot capture:" in result.stdout
            assert f"Output directory: {Path(output_dir)}" in result.stdout
            assert "Filename prefix: test" in result.stdout
            assert "Capture interval: 5 seconds" in result.stdout
            assert "Screenshot saved:" in result.stdout
            assert "Screenshot capture stopped by user." in result.stdout
            
            # Verify screenshot function was called
            mock_pyautogui.screenshot.assert_called_once()


def test_command_default_options(tmp_path, mock_datetime, mock_pyautogui, mock_logger, runner):
    # Mock time.sleep to raise KeyboardInterrupt after first iteration
    def mock_sleep(seconds):
        raise KeyboardInterrupt()

    with patch('main.time.sleep', side_effect=mock_sleep):
        # Test with default options
        with runner.isolated_filesystem():
            result = runner.invoke(app)
            
            # Check exit code
            assert result.exit_code == 0
            
            # Check output contains expected messages with default values
            assert "Running screenshot capture:" in result.stdout
            # Use Path object to match the normalized path in output
            assert f"Output directory: {Path('./screenshots')}" in result.stdout
            assert "Filename prefix: screenshot" in result.stdout
            assert "Capture interval: 10 seconds" in result.stdout
            
            # Verify screenshot function was called
            mock_pyautogui.screenshot.assert_called_once()