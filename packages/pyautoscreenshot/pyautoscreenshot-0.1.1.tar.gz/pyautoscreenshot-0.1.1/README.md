# pyautoscreenshot

> 🖼️ A Python utility for automatically capturing and saving screenshots at regular intervals

[![PyPI version](https://badge.fury.io/py/pyautoscreenshot.svg)](https://badge.fury.io/py/pyautoscreenshot)
[![Python Support](https://img.shields.io/pypi/pyversions/pyautoscreenshot.svg)](https://pypi.org/project/pyautoscreenshot/)
[![License](https://img.shields.io/github/license/fxyzbtc/pyautoscreenshot.svg)](LICENSE)

## ✨ Features

- 📸 Capture screenshots at customizable intervals
- 🕒 Automatic timestamp-based filenames
- 📁 Configurable output directory
- 🏷️ Custom filename prefixes
- 🖼️ High-quality PNG format
- 🚀 Simple CLI interface

## 📦 Installation

### Using pip
```bash
pip install pyautoscreenshot
```

### Using uv (Recommended)
[uv](https://github.com/astral-sh/uv) is a blazing-fast Python package installer:

```bash
# Install uv
pip install uv

# Install pyautoscreenshot using uv
uv pip install pyautoscreenshot
```

## 🚀 Quick Start

### Command Line Usage
```bash
# Basic usage (default: 10-second interval)
pyautoscreenshot

# Custom output directory
pyautoscreenshot --output D:/screenshots

# Custom prefix and interval
pyautoscreenshot --prefix workscreen --interval 5
```

### Python Module Usage
```bash
python -m pyautoscreenshot [options]
```

### In Your Code
```python
from pyautoscreenshot import take_screenshot

# Take a single screenshot
filepath = take_screenshot("./screenshots", "custom")
print(f"Screenshot saved to: {filepath}")
```

## 🎛️ Configuration Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--output` | `-o` | Output directory | `./screenshots` |
| `--prefix` | `-p` | Filename prefix | `screenshot` |
| `--interval` | `-i` | Capture interval (seconds) | `10` |

## 🛠️ Development

### Setup Development Environment

1. Clone the repository
```bash
git clone https://github.com/fxyzbtc/pyautoscreenshot.git
cd pyautoscreenshot
```

2. Create and activate virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. Install development dependencies
```bash
uv pip install -e ".[dev]"
```

### Running Tests
```bash
pytest
```

### Code Style
```bash
# Format code
black .

# Sort imports
isort .
```

## 📝 Example Output

Screenshots are saved with the following naming pattern:
```
{prefix}_{YYYYMMDD}_{HHMMSS}.png
```

Example:
```
screenshot_20250404_153022.png
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PyAutoGUI](https://github.com/asweigart/pyautogui) for screenshot capabilities
- [Typer](https://github.com/tiangolo/typer) for the CLI interface
- [Loguru](https://github.com/Delgan/loguru) for logging

## 📞 Support

- 📫 Report issues on [GitHub Issues](https://github.com/fxyzbtc/pyautoscreenshot/issues)
- 💬 Ask questions in [Discussions](https://github.com/fxyzbtc/pyautoscreenshot/discussions)
- 📚 Read the [documentation](https://github.com/fxyzbtc/pyautoscreenshot/wiki)

---
Made with ❤️ using Python