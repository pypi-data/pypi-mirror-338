from typing import Dict, List, Optional
import time

class CommandGenerator:
    def __init__(self):
        self.commands: List[Dict] = []
        self.current_test: Optional[Dict] = None
        self.start_time: Optional[float] = None

    def start_test(self, name: str = "Recorded Test") -> None:
        """Start a new test recording"""
        self.current_test = {
            "id": str(time.time()),
            "version": "2.0",
            "name": name,
            "url": "about:blank",
            "tests": [],
            "urls": [],
            "plugins": []
        }
        self.start_time = time.time()

    def process_events(self, events: List[Dict]) -> None:
        """Process recorded events and convert them to commands"""
        if not self.current_test:
            self.start_test()

        for event in events:
            command = self._event_to_command(event)
            if command:
                self.commands.append(command)

    def _event_to_command(self, event: Dict) -> Optional[Dict]:
        """Convert an event to a Selenium IDE command"""
        event_type = event.get("type")
        timestamp = event.get("timestamp", 0)
        
        if not self.start_time:
            return None

        # Calculate command timing
        command_time = timestamp - self.start_time

        if event_type == "mouse_click":
            # Get element location information
            element_info = event.get("element_info", {})
            xpath = element_info.get("xpath", "")
            is_shadow = element_info.get("is_shadow", False)
            attributes = element_info.get("attributes", {})
            shadow_info = element_info.get("shadow_info", {})
            
            # Build target with shadow DOM support
            target = self._build_target(xpath, is_shadow, attributes, shadow_info)
            
            return {
                "id": str(time.time()),
                "comment": "",
                "command": "click",
                "target": target,
                "targets": self._generate_alternative_targets(attributes, shadow_info),
                "value": "",
                "time": command_time
            }
        elif event_type == "key_press":
            # Get element location information
            element_info = event.get("element_info", {})
            xpath = element_info.get("xpath", "")
            is_shadow = element_info.get("is_shadow", False)
            attributes = element_info.get("attributes", {})
            shadow_info = element_info.get("shadow_info", {})
            
            # Build target with shadow DOM support
            target = self._build_target(xpath, is_shadow, attributes, shadow_info)
            
            return {
                "id": str(time.time()),
                "comment": "",
                "command": "type",
                "target": target,
                "targets": self._generate_alternative_targets(attributes, shadow_info),
                "value": event["key"],
                "time": command_time
            }
        elif event_type == "mouse_move":
            # Get element location information
            element_info = event.get("element_info", {})
            xpath = element_info.get("xpath", "")
            is_shadow = element_info.get("is_shadow", False)
            attributes = element_info.get("attributes", {})
            shadow_info = element_info.get("shadow_info", {})
            
            # Build target with shadow DOM support
            target = self._build_target(xpath, is_shadow, attributes, shadow_info)
            
            return {
                "id": str(time.time()),
                "comment": "",
                "command": "mouseMove",
                "target": target,
                "targets": self._generate_alternative_targets(attributes, shadow_info),
                "value": "",
                "time": command_time
            }
        elif event_type == "mouse_scroll":
            # Get element location information
            element_info = event.get("element_info", {})
            xpath = element_info.get("xpath", "")
            is_shadow = element_info.get("is_shadow", False)
            attributes = element_info.get("attributes", {})
            shadow_info = element_info.get("shadow_info", {})
            
            # Build target with shadow DOM support
            target = self._build_target(xpath, is_shadow, attributes, shadow_info)
            
            return {
                "id": str(time.time()),
                "comment": "",
                "command": "mouseWheel",
                "target": target,
                "targets": self._generate_alternative_targets(attributes, shadow_info),
                "value": str(event["dy"]),
                "time": command_time
            }

        return None

    def _build_target(self, xpath: str, is_shadow: bool, attributes: Dict, shadow_info: Dict) -> str:
        """Build target string with shadow DOM support"""
        if is_shadow and shadow_info:
            # For shadow DOM elements, include the shadow root path
            shadow_root_path = shadow_info.get("shadow_root_path", "")
            if shadow_root_path:
                return f"shadow={shadow_root_path}/{xpath}"
            else:
                return f"shadow={xpath}"
        else:
            # For regular elements, use standard XPath
            return xpath

    def _generate_alternative_targets(self, attributes: Dict, shadow_info: Dict) -> List[str]:
        """Generate alternative target locators based on element attributes"""
        targets = []
        
        # Add ID-based target if available
        if "id" in attributes:
            targets.append(f"id={attributes['id']}")
            
        # Add name-based target if available
        if "name" in attributes:
            targets.append(f"name={attributes['name']}")
            
        # Add class-based target if available
        if "class" in attributes:
            targets.append(f"css=.{attributes['class'].replace(' ', '.')}")
            
        # Add type-based target if available
        if "type" in attributes:
            targets.append(f"css=[type='{attributes['type']}']")
            
        # Add role-based target if available
        if "role" in attributes:
            targets.append(f"css=[role='{attributes['role']}']")
            
        # Add aria-label-based target if available
        if "aria-label" in attributes:
            targets.append(f"css=[aria-label='{attributes['aria-label']}']")
            
        # Add shadow DOM specific targets if available
        if shadow_info:
            shadow_host = shadow_info.get("shadow_host", {})
            if "id" in shadow_host:
                targets.append(f"shadow=//*[@id='{shadow_host['id']}']/{attributes.get('xpath', '')}")
            if "class" in shadow_host:
                targets.append(f"shadow=//*[contains(@class, '{shadow_host['class']}')]/{attributes.get('xpath', '')}")
            
        return targets

    def generate_output(self) -> Dict:
        """Generate the final output in Selenium IDE format"""
        if not self.current_test:
            return {}

        self.current_test["tests"] = [{
            "id": str(time.time()),
            "name": self.current_test["name"],
            "commands": self.commands
        }]

        return self.current_test

    def clear(self) -> None:
        """Clear all recorded commands and reset the generator"""
        self.commands = []
        self.current_test = None
        self.start_time = None 