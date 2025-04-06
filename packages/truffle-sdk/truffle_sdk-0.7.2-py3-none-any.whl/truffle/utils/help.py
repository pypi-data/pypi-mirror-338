"""
CLI Help Menu System

This module manages the display of help information in the Truffle CLI:
- Beautiful command documentation
- Consistent styling with logger
- Clear examples and options
"""

from .logger import log, Colors
from .formatter import Formatter

class HelpMenu:
    """Manages help menu display and formatting."""
    
    def __init__(self):
        self.fmt = Formatter()
    
    def show_help(self):
        """Display the main help menu."""
        # Display the Truffle banner
        print(self.fmt.truffle_banner())
        
        # Commands section
        log.main("Commands:")
        
        # Init command
        log.detail(self.fmt.command_box("init [name]", "Create a new project"))
        log.detail("  Options:")
        log.detail(f"    {self.fmt.option('-d, --description TEXT', 'What your project does')}")
        log.detail("  Examples:")
        log.detail(f"    {self.fmt.example('truffle init', 'Create on desktop')}")
        log.detail(f"    {self.fmt.example('truffle init my-app', 'Create named project')}")
        log.detail(f"    {self.fmt.example('truffle init -d "My app"', 'Add description')}")
        
        # Build command
        log.detail(self.fmt.command_box("build", "Prepare your project"))
        log.detail("  Examples:")
        log.detail(f"    {self.fmt.example('truffle build', 'Build current project')}")
        
        # Upload command
        log.detail(self.fmt.command_box("upload", "Share your project"))
        log.detail("  Examples:")
        log.detail(f"    {self.fmt.example('truffle upload', 'Upload built project')}")
        
        # Help command
        log.detail(self.fmt.command_box("--help", "Show this help message")) 