import json
import time
from datetime import datetime
from typing import Dict, List, Optional, Union
import cv2
import numpy as np
from PIL import Image
import base64
from io import BytesIO
import subprocess
import asyncio
import os
from playwright.async_api import Browser, Page, BrowserContext
import logging

from .event_handler import EventHandler
from .element_locator import ElementLocator
from .command_generator import CommandGenerator

logger = logging.getLogger(__name__)

class ScreenRecorder:
    def __init__(self, browser_type: str = 'chrome', driver: Optional[Browser] = None):
        self.browser_type = browser_type
        self.browser = driver
        self.is_recording = False
        self.recording_data = {
            'browser_type': browser_type,
            'start_time': None,
            'end_time': None,
            'commands': [],
            'screenshots': [],
            'elements': [],
            'actions': [],
            'events': []
        }
        self.event_handler = EventHandler()
        self.page: Optional[Page] = None
        self.element_locator = ElementLocator(browser_type=browser_type, driver=driver) if driver else None
        self.command_generator = CommandGenerator()
        self.screen_capture = None
        self.start_time = None

    def get_browser_version(self) -> str:
        """Get the version of the active browser"""
        try:
            if self.browser_type == 'chrome':
                cmd = ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--version']
            elif self.browser_type == 'firefox':
                cmd = ['/Applications/Firefox.app/Contents/MacOS/firefox', '--version']
            else:
                return "Unknown browser"
                
            result = subprocess.run(cmd, capture_output=True, text=True)
            return result.stdout.strip()
        except Exception as e:
            print(f"Error getting browser version: {e}")
            return "Unknown version"

    async def start_recording(self) -> None:
        """Start recording browser actions."""
        if self.is_recording:
            return
            
        self.is_recording = True
        self.recording_data['start_time'] = datetime.now().isoformat()
        
        # Use the existing browser context
        if self.browser and self.browser.contexts:
            self.page = self.browser.contexts[0].pages[0]
            
            # Start event handler
            await self.event_handler.start_listening(self.browser)
            
            # Take initial screenshot
            await self._take_screenshot()
            
            logger.info("Started screen recording")
        else:
            logger.error("No browser context available")
            self.is_recording = False
            raise RuntimeError("No browser context available")

    async def stop_recording(self) -> Dict:
        """Stop recording and return the recording data."""
        if not self.is_recording:
            return self.recording_data
            
        self.is_recording = False
        self.recording_data['end_time'] = datetime.now().isoformat()
        
        # Stop event handler and get events
        if self.event_handler:
            await self.event_handler.stop_listening()
            events = self.event_handler.get_events()
            self.recording_data['events'] = events
            
            # Process events into actions
            for event in events:
                action = self._process_event(event)
                if action:
                    self.recording_data['actions'].append(action)
        
        # Take final screenshot
        await self._take_screenshot()
        
        logger.info("Stopped screen recording")
        return self.recording_data

    def _process_event(self, event: Dict) -> Optional[Dict]:
        """Process a browser event into a recorded action."""
        if not event or 'type' not in event:
            return None

        event_type = event['type']
        detail = event.get('detail', {})
        
        if event_type == 'recorded-load':
            return {
                'type': 'load',
                'timestamp': detail.get('timestamp'),
                'url': detail.get('url'),
                'title': detail.get('title')
            }
        elif event_type == 'recorded-click':
            return {
                'type': 'click',
                'timestamp': detail.get('timestamp'),
                'element': detail.get('element'),
                'coordinates': detail.get('coordinates')
            }
        elif event_type == 'recorded-input':
            return {
                'type': 'input',
                'timestamp': detail.get('timestamp'),
                'element': detail.get('element'),
                'value': detail.get('value')
            }
        elif event_type == 'recorded-keydown':
            return {
                'type': 'keydown',
                'timestamp': detail.get('timestamp'),
                'element': detail.get('element'),
                'key': detail.get('key'),
                'code': detail.get('code')
            }
        
        return None

    async def _take_screenshot(self) -> None:
        """Take a screenshot of the current page."""
        if not self.is_recording or not self.page:
            return
            
        try:
            # Ensure the page has loaded and has dimensions
            await self.page.wait_for_load_state('networkidle')
            
            # Get page dimensions
            dimensions = await self.page.evaluate("""() => {
                return {
                    width: Math.max(document.documentElement.clientWidth, document.body ? document.body.scrollWidth : 0),
                    height: Math.max(document.documentElement.clientHeight, document.body ? document.body.scrollHeight : 0)
                };
            }""")
            
            # Set viewport size if needed
            if dimensions['width'] == 0 or dimensions['height'] == 0:
                await self.page.set_viewport_size({'width': 1280, 'height': 800})
            
            # Create screenshots directory if it doesn't exist
            os.makedirs('screenshots', exist_ok=True)
            
            # Generate screenshot filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"screenshots/screenshot_{timestamp}.png"
            
            # Take screenshot
            await self.page.screenshot(path=screenshot_path, full_page=True)
            
            # Add screenshot to recording data
            self.recording_data['screenshots'].append({
                'timestamp': datetime.now().isoformat(),
                'path': screenshot_path
            })
            
            logger.info(f"Screenshot saved to {screenshot_path}")
            
        except Exception as e:
            logger.error(f"Error taking screenshot: {str(e)}")
            # Don't raise the error, just log it and continue

    def add_command(self, command: Dict) -> None:
        """Add a command to the recording data."""
        if self.is_recording:
            self.recording_data["commands"].append(command)

    def _start_screen_capture(self) -> None:
        """Start capturing screen"""
        self.screen_capture = cv2.VideoCapture(0)  # 0 for default screen
        self.screen_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.screen_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    def _stop_screen_capture(self) -> None:
        """Stop capturing screen"""
        if self.screen_capture:
            self.screen_capture.release()

    def capture_screenshot(self) -> str:
        """Capture current screen and return as base64 string"""
        if not self.screen_capture:
            return ""
            
        ret, frame = self.screen_capture.read()
        if not ret:
            return ""
            
        # Convert frame to PIL Image
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        # Convert to base64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

    async def get_element_location(self, x: int, y: int) -> Optional[Dict]:
        """Get element location information at given coordinates"""
        if not self.element_locator:
            logger.warning("Element locator not initialized")
            return None
        return await self.element_locator.locate_element(x, y) 