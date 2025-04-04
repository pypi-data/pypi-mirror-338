# DivineGift Logger

A flexible and configurable logging package for Python applications with file rotation and command-line configuration support.

## Features

- ✅ Easy configuration via code or command-line arguments
- ✅ File rotation with customizable intervals
- ✅ Both file and console logging support
- ✅ Thread-safe implementation
- ✅ Type hints for better IDE support
- ✅ Exception logging with stack traces

## Installation

```bash
pip install dglog
```

## Basic Usage

### Simple console logging

```python
from dglog import get_logger

logger = get_logger()
logger.info("Application started")
logger.warning("This is a warning")
```

### Configure logger programmatically

```python
from dglog import configure_logger

# Configure with daily file rotation
configure_logger(
    log_level="DEBUG",
    log_name="app.log",
    log_dir="./logs",
    when="D",
    backup_count=14
)

log_info("This will be logged to file")
```

### Command-line configuration

Run your script with logging parameters:

```bash
python your_script.py --log_level DEBUG --log_name app.log --log_dir ./logs
```

The logger will automatically pick up these parameters.

## API Reference

### Core Functions

| Function | Description |
|----------|-------------|
| `get_logger()` | Returns the global logger instance |
| `configure_logger(**kwargs)` | Configures the global logger |
| `log_debug(*args, separator=" ")` | Logs debug message |
| `log_info(*args, separator=" ")` | Logs info message |
| `log_warning(*args, separator=" ")` | Logs warning message |
| `log_error(*args, separator=" ")` | Logs error message |
| `log_critical(*args, separator=" ")` | Logs critical message |
| `log_exception(*args, separator=" ")` | Logs exception with stack trace |

### Logger Class Methods

```python
logger = get_logger()

# Configuration
logger.configure_logger(
    log_level="INFO",          # Logging level
    log_name=None,             # File name (None for console)
    log_dir="./logs",          # Log directory
    when="midnight",          # Rotation interval
    interval=1,               # Rotation frequency
    backup_count=7,           # Number of backups
    formatter=None            # Custom formatter
)

# Logging methods
logger.debug("Debug message")
logger.info("Information")
logger.warning("Warning message")
logger.error("Error occurred")
logger.critical("Critical failure")
logger.exception("Exception occurred")  # With stack trace
```

## Advanced Examples

### Custom Formatter

```python
from logging import Formatter

custom_format = Formatter('%(name)s - %(levelname)s - %(message)s')
configure_logger(log_level="DEBUG", formatter=custom_format)
```

### Exception Handling

```python
try:
    1 / 0
except Exception:
    log_exception("Division failed")
    # Output includes the stack trace
```

### Multiple Arguments

```python
log_info("User", "logged in", "from IP", "192.168.1.1", separator=" | ")
# Output: User | logged in | from IP | 192.168.1.1
```

### Dynamic Configuration

```python
import sys
from dglog import get_logger

logger = get_logger()

if '--debug' in sys.argv:
    logger.configure_logger(log_level="DEBUG")
else:
    logger.configure_logger(log_level="INFO")
```

## Configuration Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| log_level | "INFO" | Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL) |
| log_name | None | Log file name (None for console logging) |
| log_dir | "./logs" | Directory for log files |
| when | "midnight" | Rotation interval ('S', 'M', 'H', 'D', 'midnight', etc.) |
| interval | 1 | Rotation frequency |
| backup_count | 7 | Number of backup files to keep |
| formatter | Default format | Custom log message formatter |

## Best Practices

1. **Early Configuration**: Configure the logger at the start of your application
2. **Proper Log Levels**: Use appropriate levels for different situations
3. **Structured Data**: Include context in your log messages
4. **Exception Handling**: Always use `log_exception()` for errors
5. **Rotation Policy**: Choose appropriate rotation settings based on your needs

## License

MIT License - Free for commercial and personal use.