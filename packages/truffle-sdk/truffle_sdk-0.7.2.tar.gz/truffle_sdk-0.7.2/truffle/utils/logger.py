"""
CLI Logging System

This module implements a rich console logging system for the Truffle CLI:
- Provides color-coded output
- Implements structured logging
- Supports progress tracking and metrics display
- Handles formatting with details
"""

from dataclasses import dataclass
from typing import Optional, Dict, List, Union, TypedDict
import sys

__all__ = ['Colors', 'Symbols', 'Logger', 'log']

class DetailDict(TypedDict, total=False):
    """Type definition for detail dictionaries with optional dim-gray values."""
    key: str
    value: str
    dim_value: str

@dataclass
class Colors:
    """ANSI color codes for terminal output."""
    __slots__ = []
   
    MAIN: str = "\033[38;2;95;173;235m"      # #5FADEB - Primary actions/success
    SECONDARY: str = "\033[38;2;74;155;217m"  # #4A9BD9 - Info/progress
    WHITE: str = "\033[38;2;255;255;255m"     # #FFFFFF - Standard output
    LIGHT_GRAY: str = "\033[38;2;204;204;204m"# #CCCCCC - Secondary info
    DIM_GRAY: str = "\033[38;2;128;128;128m"  # #808080 - Technical details
    ERROR: str = "\033[38;2;255;59;48m"       # #FF3B30 - Errors
    WARNING: str = "\033[38;2;255;149;0m"     # #FF9500 - Warnings
    RESET: str = "\033[0m"

    # Background colors for blocks
    ERROR_BG: str = "\033[48;2;255;59;48;0.1m"
    WARNING_BG: str = "\033[48;2;255;149;0;0.1m"

@dataclass
class Symbols:
    """Unicode symbols for consistent logging."""
    __slots__ = []
   
    # Status indicators
    SUCCESS: str = "✓"
    ERROR: str = "✗"
    WARNING: str = "!"
    CHECK: str = "✓"
    ARROW: str = "→"
   
    # File operations
    FILE_CREATED: str = "+"
    FILE_MODIFIED: str = "•"
    FILE_DELETED: str = "-"
   
    # Command
    CMD_PREFIX: str = "$"

class Logger:
    """
    Beautiful CLI logger with Truffle-specific styling.
   
    Features:
    - Color-coded output
    - Indentation and grouping
    - Version and metric formatting
    - Chainable methods
    """
   
    def __init__(self) -> None:
        self._indent_level: int = 0
        self._indent_size: int = 2
        self._indent_cache: Dict[int, str] = {}
   
    def _indent(self) -> str:
        """Generate indentation string based on current level."""
        if self._indent_level not in self._indent_cache:
            self._indent_cache[self._indent_level] = " " * (self._indent_level * self._indent_size)
        return self._indent_cache[self._indent_level]
   
    def _format_version(self, version: str) -> str:
        """Format version string to vX.Y.Z format."""
        return f"v{version}" if not version.startswith('v') else version
   
    def _format(self,
                color: str,
                message: str,
                prefix: str = "",
                suffix: str = "",
                version: Optional[str] = None,
                metric: Optional[str] = None,
                end: str = "\n") -> 'Logger':
        """Format and print a log message with consistent styling."""
        indent = self._indent()
        prefix = f"{prefix} " if prefix else ""
        parts: List[str] = [f"{color}{indent}{prefix}{message}{Colors.RESET}"]
       
        if suffix:
            parts.append(suffix)
        if version:
            parts.append(f"{Colors.DIM_GRAY} {self._format_version(version)}{Colors.RESET}")
        if metric:
            parts.append(f"{Colors.DIM_GRAY}{metric}{Colors.RESET}")
           
        print(" ".join(parts), end=end, file=sys.stderr)
        return self
   
    def cmd(self, command: str, args: Optional[str] = None) -> 'Logger':
        """Format command input styling."""
        parts: List[str] = [f"{Colors.MAIN}{Symbols.CMD_PREFIX} {command}{Colors.RESET}"]
        if args:
            parts.append(f"{Colors.WHITE}{args}{Colors.RESET}")
        print(" ".join(parts), file=sys.stderr)
        return self
   
    def main(self, message: str, version: Optional[str] = None) -> 'Logger':
        """Log main/primary actions in blue."""
        return self._format(Colors.MAIN, message, version=version)
   
    def build(self, message: str, version: Optional[str] = None) -> 'Logger':
        """Log build messages in secondary blue."""
        return self._format(Colors.SECONDARY, message, version=version)
   
    def detail(self, message: str, metric: Optional[str] = None, dim_suffix: Optional[str] = None) -> 'Logger':
        """Log additional details in light gray."""
        msg = message
        if dim_suffix:
            msg = f"{message} ({dim_suffix})"
        return self._format(Colors.LIGHT_GRAY, msg, metric=metric)
   
    def success(self, message: str) -> 'Logger':
        """Log success messages in main blue with checkmark."""
        return self._format(Colors.MAIN, f"{Symbols.SUCCESS} {message}")
   
    def prompt(self, label: str, value: str = "", end: str = "\n") -> 'Logger':
        """Format input prompt styling."""
        return self._format(
            Colors.MAIN,
            f"{Symbols.ARROW} {label}:",
            suffix=f" {Colors.WHITE}{value}{Colors.RESET}" if value else "",
            end=end
        )
   
    def created_file(self, path: str) -> 'Logger':
        """Log file creation indicator."""
        return self._format(Colors.MAIN, f"{Symbols.FILE_CREATED} {path}")
   
    def modified_file(self, path: str) -> 'Logger':
        """Log file modification indicator."""
        return self._format(Colors.MAIN, f"{Symbols.FILE_MODIFIED} {path}")
   
    def deleted_file(self, path: str) -> 'Logger':
        """Log file deletion indicator."""
        return self._format(Colors.MAIN, f"{Symbols.FILE_DELETED} {path}")
   
    def check(self, item: str, version: Optional[str] = None) -> 'Logger':
        """Log validation checkmark with optional version."""
        return self._format(Colors.MAIN, f"{Symbols.CHECK} {item}", version=version)
   
    def metric(self, value: Union[str, int, float], context: Optional[str] = None) -> 'Logger':
        """Log metric display with optional context in light gray."""
        msg = str(value)
        if context:
            msg = f"{msg} {context}"
        return self.detail(msg)  # Just use detail's light gray color

    def error(self, message: str) -> 'Logger':
        """Log error messages in red with error symbol."""
        return self._format(Colors.ERROR, f"{Symbols.ERROR} {message}")

    def warning(self, message: str) -> 'Logger':
        """Log warning messages in orange with warning symbol."""
        return self._format(Colors.WARNING, f"{Symbols.WARNING} {message}")

    def group(self, message: str) -> 'Logger':
        """Create a new log group with increased indentation."""
        self._format(Colors.MAIN, message)
        self._indent_level += 1
        return self

    def end_group(self) -> 'Logger':
        """End the current log group and decrease indentation."""
        if self._indent_level > 0:
            self._indent_level -= 1
        return self

    def __enter__(self) -> 'Logger':
        """Context manager entry - no-op since indentation is handled by group()."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit - decrease indentation level."""
        self.end_group()

# Global logger instance
log = Logger() 