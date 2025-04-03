# Synthra Logger

A simple and customizable Python logging module that uses color formatting and timestamps. Ideal for creating console logs with different severity levels like info, debug, fail, and more. It also includes a method for capturing user input with a timestamp.

## Features

- **Color-coded log levels**: Includes support for `INFO`, `DEBUG`, `FAIL`, `WARN`, `SUCCESS`, and more.
- **Timestamped logs**: Each log entry is prefixed with the current time for easy tracking.
- **Thread-safe**: Uses a `Lock` to ensure logs are printed correctly in multi-threaded applications.
- **User input capture**: The logger can also capture and display user input with a timestamp.

## Installation

To install the `synthra` logger, you can either install it via pip from a local directory or from PyPI if you decide to upload it.

### Local Installation

1. Clone the repository or download the source code.
2. Navigate to the root directory of the project (where `setup.py` is located).
3. Run the following command to install the logger package:

```bash
pip install -e .
