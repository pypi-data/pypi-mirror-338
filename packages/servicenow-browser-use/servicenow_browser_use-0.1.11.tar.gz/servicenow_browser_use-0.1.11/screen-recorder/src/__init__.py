"""
Screen Recorder - A tool for recording user interactions and generating Selenium IDE-compatible test files.
"""

from .recorder import ScreenRecorder
from .event_handler import EventHandler
from .element_locator import ElementLocator
from .command_generator import CommandGenerator

__all__ = ['ScreenRecorder', 'EventHandler', 'ElementLocator', 'CommandGenerator']

"""
Screen recorder package
""" 