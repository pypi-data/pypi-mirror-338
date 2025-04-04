from .browser.browser import Browser
from .browser.context import BrowserContextConfig
from .browser.streamlined_recorder import StreamlinedRecorder
from .agent.service import Agent
from .browser.browser_controller import BrowserController

__version__ = "0.1.0"

__all__ = [
    "Browser",
    "BrowserContextConfig",
    "StreamlinedRecorder",
    "Agent",
    "BrowserController",
] 