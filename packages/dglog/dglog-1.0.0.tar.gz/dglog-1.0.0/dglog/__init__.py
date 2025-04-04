import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from typing import Optional, Dict, Any


def get_base_dir() -> str:
    """Get current working directory or empty string if unavailable."""
    try:
        return os.getcwd()
    except Exception:
        return ''


def parse_args() -> Dict[str, Any]:
    """
    Parse command line arguments into a dictionary.
    Returns:
        Dict[str, Any]: Dictionary of arguments where keys are parameter names
                       (without leading dashes) and values are argument values.
    """
    args = sys.argv
    args_dict = {}
    i = 0
    while i < len(args):
        arg = args[i]
        if i == 0:
            args_dict['name'] = arg
            i += 1
            continue

        if arg.startswith(('-', '--')):
            key = arg.lstrip('-')
            if i + 1 < len(args) and not args[i + 1].startswith(('-', '--')):
                value = args[i + 1]
                try:
                    args_dict[key] = int(value)
                except ValueError:
                    try:
                        args_dict[key] = float(value)
                    except ValueError:
                        args_dict[key] = value
                i += 2
            else:
                args_dict[key] = True
                i += 1
        else:
            i += 1

    return args_dict


def extract_log_params(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract logging parameters from arguments dictionary.
    Args:
        args: Dictionary of arguments from parse_args()
    Returns:
        Dictionary with log_level, log_name, and log_dir
    """
    log_params = {
        'log_level': args.get('log_level', args.get('ll', 'INFO')).upper(),
        'log_name': args.get('log_name', args.get('ln')),
        'log_dir': args.get('log_dir', args.get('ld', os.path.join(get_base_dir(), 'logs')))
    }
    return log_params


class Logger:
    def __init__(self):
        self.logger: Optional[logging.Logger] = None
        self.log_dir: Optional[str] = None
        self.log_name: Optional[str] = None
        self.formatter = logging.Formatter('%(levelname)-8s [%(asctime)s] %(message)s')
        self._default_logger_name = 'default_logger'

    def _ensure_logger_exists(self) -> None:
        """Ensure logger is initialized."""
        if not self.logger:
            self.get_logger(self._default_logger_name)

    def configure_logger(
            self,
            log_level: str = 'INFO',
            log_name: Optional[str] = None,
            log_dir: str = './logs/',
            when: str = 'midnight',
            interval: int = 1,
            backup_count: int = 7,
            formatter: Optional[logging.Formatter] = None
    ) -> None:
        """
        Configure logger with specified parameters.
        Args:
            log_level: Logging level (e.g., 'INFO', 'DEBUG')
            log_name: Name of log file (None for console logging)
            log_dir: Directory for log files
            when: When to rotate logs ('midnight', 'D', 'H', etc.)
            interval: Rotation interval
            backup_count: Number of backup files to keep
            formatter: Custom log formatter
        """
        self._ensure_logger_exists()

        # Clear existing handlers
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # Set log level
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError(f'Invalid log level: {log_level}')
        self.logger.setLevel(numeric_level)

        # Create and configure handler
        if log_name:
            os.makedirs(log_dir, exist_ok=True)
            handler = TimedRotatingFileHandler(
                filename=os.path.join(log_dir, log_name),
                when=when,
                interval=interval,
                backupCount=backup_count,
                encoding='utf-8'
            )
            self.log_name = log_name
            self.log_dir = log_dir
        else:
            handler = logging.StreamHandler()

        handler.setFormatter(formatter or self.formatter)
        self.logger.addHandler(handler)

    def auto_configure(self) -> None:
        """Auto-configure logger using command line arguments."""
        params = extract_log_params(parse_args())
        self.configure_logger(**params)

    def get_logger(self, name: str) -> logging.Logger:
        """Get or create logger with specified name."""
        self.logger = logging.getLogger(name)
        return self.logger

    def _log(self, level: str, *args, separator: str = ' ') -> None:
        """Internal logging method."""
        self._ensure_logger_exists()
        message = separator.join(str(arg) for arg in args)
        getattr(self.logger, level.lower())(message)

    def debug(self, *args, separator: str = ' ') -> None:
        """Log debug message."""
        self._log('debug', *args, separator=separator)

    # Обратная совместимость
    def log_debug(self, *args, separator: str = ' ') -> None:
        self.debug(*args, separator=separator)

    def info(self, *args, separator: str = ' ') -> None:
        """Log info message."""
        self._log('info', *args, separator=separator)

    def log_info(self, *args, separator: str = ' ') -> None:
        self.info(*args, separator=separator)

    def warning(self, *args, separator: str = ' ') -> None:
        """Log warning message."""
        self._log('warning', *args, separator=separator)

    def log_warn(self, *args, separator: str = ' ') -> None:
        self.warning(*args, separator=separator)

    def error(self, *args, separator: str = ' ') -> None:
        """Log error message."""
        self._log('error', *args, separator=separator)

    def log_err(self, *args, separator: str = ' ') -> None:
        self.error(*args, separator=separator)

    def critical(self, *args, separator: str = ' ') -> None:
        """Log critical message."""
        self._log('critical', *args, separator=separator)

    def log_crit(self, *args, separator: str = ' ') -> None:
        self.critical(*args, separator=separator)

    def exception(self, *args, separator: str = ' ') -> None:
        """Log exception with stack trace."""
        self._ensure_logger_exists()
        message = separator.join(str(arg) for arg in args)
        self.logger.exception(message)


# Global logger instance
_global_logger = Logger()


def get_logger() -> Logger:
    """Get global logger instance."""
    return _global_logger


# Shortcut functions
def log_debug(*args, separator: str = ' ') -> None:
    _global_logger.debug(*args, separator=separator)


def log_info(*args, separator: str = ' ') -> None:
    _global_logger.info(*args, separator=separator)


def log_warning(*args, separator: str = ' ') -> None:
    _global_logger.warning(*args, separator=separator)


def log_error(*args, separator: str = ' ') -> None:
    _global_logger.error(*args, separator=separator)


def log_critical(*args, separator: str = ' ') -> None:
    _global_logger.critical(*args, separator=separator)


def log_exception(*args, separator: str = ' ') -> None:
    _global_logger.exception(*args, separator=separator)


def configure_logger(**kwargs) -> None:
    """Configure global logger."""
    _global_logger.configure_logger(**kwargs)


if __name__ == '__main__':
    # Example usage
    configure_logger(log_level='DEBUG')
    log_info("Logger initialized")
    log_debug("Debug message")
    log_warning("Warning message")
    try:
        1 / 0
    except Exception:
        log_exception("Error occurred")