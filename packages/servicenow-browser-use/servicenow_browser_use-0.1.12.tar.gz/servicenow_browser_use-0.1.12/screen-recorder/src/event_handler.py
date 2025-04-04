import asyncio
from typing import Dict, List, Optional, Callable, Awaitable, Any, cast
from playwright.async_api import Browser, Page, ConsoleMessage, BrowserContext, ElementHandle, JSHandle
from datetime import datetime
import json
import logging

logger = logging.getLogger(__name__)

class EventHandler:
    def __init__(self):
        self.events: List[Dict] = []
        self.is_listening = False

    async def start_listening(self, browser: Browser) -> None:
        """Start listening for browser events."""
        self.is_listening = True
        self.events = []
        logger.info("Started listening for events")
        
        # Add event listeners to all pages in the default context
        context = browser.contexts[0]
        pages = context.pages
        for page in pages:
            await self._add_page_listeners(page)
            logger.info(f"Added listeners to page: {page.url}")
            
        # Listen for new pages
        async def handle_new_page(page: Page) -> None:
            await self._add_page_listeners(page)
            logger.info(f"Added listeners to new page: {page.url}")
            
        context.on("page", handle_new_page)

    async def stop_listening(self) -> None:
        """Stop listening for browser events."""
        self.is_listening = False
        logger.info(f"Stopped listening for events. Total events captured: {len(self.events)}")

    async def _add_page_listeners(self, page: Page) -> None:
        """Add event listeners to a page."""
        # Add JavaScript event listeners as early as possible
        await page.add_init_script("""() => {
            console.log('__pw_init', 'Event listeners initialized');
            
            // Function to add event listeners to a document
            function addEventListeners(doc) {
                // Click listener
                doc.addEventListener('click', (event) => {
                    const element = event.target;
                    const rect = element.getBoundingClientRect();
                    
                    // Get XPath
                    function getXPath(element) {
                        if (element.id) {
                            return "//*[@id='" + element.id + "']";
                        }
                        
                        if (element == document.body) {
                            return '/html/body';
                        }
                        
                        let path = '';
                        while (element && element.nodeType === 1) {
                            let index = 1;
                            let sibling = element.previousSibling;
                            while (sibling) {
                                if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {
                                    index++;
                                }
                                sibling = sibling.previousSibling;
                            }
                            const tagName = element.tagName.toLowerCase();
                            path = '/' + tagName + '[' + index + ']' + path;
                            element = element.parentNode;
                        }
                        return path;
                    }
                    
                    // Get Shadow DOM path
                    function getShadowPath(element) {
                        let path = [];
                        let current = element;
                        
                        while (current) {
                            if (current.shadowRoot) {
                                path.unshift({
                                    host: {
                                        tagName: current.tagName,
                                        id: current.id,
                                        className: current.className
                                    },
                                    shadowRoot: true
                                });
                            }
                            current = current.parentNode;
                        }
                        
                        return path;
                    }
                    
                    window.dispatchEvent(new CustomEvent('recorded-click', {
                        detail: {
                            type: 'click',
                            timestamp: new Date().toISOString(),
                            element: {
                                tagName: element.tagName.toLowerCase(),
                                id: element.id || '',
                                type: element.type || '',
                                value: element.value || '',
                                text: element.textContent?.trim() || '',
                                xpath: getXPath(element),
                                shadowPath: getShadowPath(element)
                            },
                            coordinates: {
                                x: event.clientX,
                                y: event.clientY
                            }
                        }
                    }));
                });

                // Input event listener
                doc.addEventListener('input', (event) => {
                    const element = event.target;
                    
                    // Get XPath
                    function getXPath(element) {
                        if (element.id) {
                            return "//*[@id='" + element.id + "']";
                        }
                        
                        if (element == document.body) {
                            return '/html/body';
                        }
                        
                        let path = '';
                        while (element && element.nodeType === 1) {
                            let index = 1;
                            let sibling = element.previousSibling;
                            while (sibling) {
                                if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {
                                    index++;
                                }
                                sibling = sibling.previousSibling;
                            }
                            const tagName = element.tagName.toLowerCase();
                            path = '/' + tagName + '[' + index + ']' + path;
                            element = element.parentNode;
                        }
                        return path;
                    }
                    
                    // Get Shadow DOM path
                    function getShadowPath(element) {
                        let path = [];
                        let current = element;
                        
                        while (current) {
                            if (current.shadowRoot) {
                                path.unshift({
                                    host: {
                                        tagName: current.tagName,
                                        id: current.id,
                                        className: current.className
                                    },
                                    shadowRoot: true
                                });
                            }
                            current = current.parentNode;
                        }
                        
                        return path;
                    }
                    
                    window.dispatchEvent(new CustomEvent('recorded-input', {
                        detail: {
                            type: 'input',
                            timestamp: new Date().toISOString(),
                            element: {
                                tagName: element.tagName.toLowerCase(),
                                id: element.id || '',
                                type: element.type || '',
                                name: element.name || '',
                                xpath: getXPath(element),
                                shadowPath: getShadowPath(element)
                            },
                            value: element.value
                        }
                    }));
                });

                // Keydown event listener
                doc.addEventListener('keydown', (event) => {
                    const element = event.target;
                    window.dispatchEvent(new CustomEvent('__pw_action', {
                        detail: {
                            type: 'keydown',
                            timestamp: new Date().toISOString(),
                            element: {
                                tagName: element.tagName.toLowerCase(),
                                id: element.id || '',
                                type: element.type || ''
                            },
                            key: event.key,
                            code: event.code
                        }
                    }));
                });

                // Form submission listener
                doc.addEventListener('submit', (event) => {
                    const form = event.target;
                    const formData = new FormData(form);
                    const formValues = {};
                    for (let [key, value] of formData.entries()) {
                        formValues[key] = value;
                    }
                    
                    window.dispatchEvent(new CustomEvent('__pw_action', {
                        detail: {
                            type: 'submit',
                            timestamp: new Date().toISOString(),
                            element: {
                                tagName: form.tagName.toLowerCase(),
                                id: form.id || '',
                                action: form.action || '',
                                method: form.method || ''
                            },
                            formData: formValues
                        }
                    }));
                });

                // Focus/blur listeners
                doc.addEventListener('focus', (event) => {
                    const element = event.target;
                    window.dispatchEvent(new CustomEvent('__pw_action', {
                        detail: {
                            type: 'focus',
                            timestamp: new Date().toISOString(),
                            element: {
                                tagName: element.tagName.toLowerCase(),
                                id: element.id || '',
                                type: element.type || ''
                            }
                        }
                    }));
                });

                doc.addEventListener('blur', (event) => {
                    const element = event.target;
                    window.dispatchEvent(new CustomEvent('__pw_action', {
                        detail: {
                            type: 'blur',
                            timestamp: new Date().toISOString(),
                            element: {
                                tagName: element.tagName.toLowerCase(),
                                id: element.id || '',
                                type: element.type || ''
                            }
                        }
                    }));
                });
            }
            
            // Add listeners to the main document
            addEventListeners(document);
            
            // Add listeners to all frames
            document.querySelectorAll('iframe').forEach(frame => {
                try {
                    addEventListeners(frame.contentDocument);
                } catch (e) {
                    console.log('__pw_error', 'Could not add listeners to frame:', e);
                }
            });
        }""")
        
        # Add event listeners for custom events
        await page.evaluate("""() => {
            window.addEventListener('recorded-click', (event) => {
                console.log('__pw_click', JSON.stringify(event.detail));
            });
            
            window.addEventListener('recorded-input', (event) => {
                console.log('__pw_input', JSON.stringify(event.detail));
            });
        }""")
        
        # Handle console messages to capture events
        page.on('console', self._handle_console)

    async def _add_frame_listeners(self, frame) -> None:
        """Add event listeners to a frame."""
        try:
            await frame.evaluate("""() => {
                console.log('__pw_init', 'Event listeners initialized in frame');
                
                // Click listener
                document.addEventListener('click', (event) => {
                    const element = event.target;
                    const rect = element.getBoundingClientRect();
                    
                    // Get XPath
                    function getXPath(element) {
                        if (element.id) {
                            return "//*[@id='" + element.id + "']";
                        }
                        
                        if (element == document.body) {
                            return '/html/body';
                        }
                        
                        let path = '';
                        while (element && element.nodeType === 1) {
                            let index = 1;
                            let sibling = element.previousSibling;
                            while (sibling) {
                                if (sibling.nodeType === 1 && sibling.tagName === element.tagName) {
                                    index++;
                                }
                                sibling = sibling.previousSibling;
                            }
                            const tagName = element.tagName.toLowerCase();
                            path = '/' + tagName + '[' + index + ']' + path;
                            element = element.parentNode;
                        }
                        return path;
                    }
                    
                    // Get Shadow DOM path
                    function getShadowPath(element) {
                        let path = [];
                        let current = element;
                        
                        while (current) {
                            if (current.shadowRoot) {
                                path.unshift({
                                    host: {
                                        tagName: current.tagName,
                                        id: current.id,
                                        className: current.className
                                    },
                                    shadowRoot: true
                                });
                            }
                            current = current.parentNode;
                        }
                        
                        return path;
                    }
                    
                    const elementInfo = {
                        tagName: element.tagName,
                        id: element.id,
                        className: element.className,
                        name: element.name,
                        type: element.type,
                        value: element.value || '',
                        href: element.href,
                        src: element.src,
                        role: element.getAttribute('role'),
                        'aria-label': element.getAttribute('aria-label'),
                        xpath: getXPath(element),
                        shadowPath: getShadowPath(element),
                        rect: {
                            x: rect.x,
                            y: rect.y,
                            width: rect.width,
                            height: rect.height
                        }
                    };
                    
                    console.log('__pw_click', JSON.stringify({
                        x: event.clientX,
                        y: event.clientY,
                        element: elementInfo,
                        timestamp: new Date().toISOString()
                    }));
                }, true);
                
                // Input listener with shadow DOM support
                function handleInput(event) {
                    const element = event.target;
                    const rect = element.getBoundingClientRect();
                    
                    const elementInfo = {
                        tagName: element.tagName,
                        id: element.id,
                        className: element.className,
                        name: element.name,
                        type: element.type,
                        value: element.value || '',
                        href: element.href,
                        src: element.src,
                        role: element.getAttribute('role'),
                        'aria-label': element.getAttribute('aria-label'),
                        xpath: getXPath(element),
                        shadowPath: getShadowPath(element),
                        rect: {
                            x: rect.x,
                            y: rect.y,
                            width: rect.width,
                            height: rect.height
                        }
                    };
                    
                    console.log('__pw_input', JSON.stringify({
                        value: element.value || '',
                        element: elementInfo,
                        timestamp: new Date().toISOString()
                    }));
                }
                
                // Add input listeners for both regular and shadow DOM elements
                document.addEventListener('input', handleInput, true);
                document.addEventListener('change', handleInput, true);
                
                // Add listeners to all shadow roots
                function addShadowRootListeners(root) {
                    root.querySelectorAll('*').forEach(element => {
                        if (element.shadowRoot) {
                            element.shadowRoot.addEventListener('input', handleInput, true);
                            element.shadowRoot.addEventListener('change', handleInput, true);
                            addShadowRootListeners(element.shadowRoot);
                        }
                    });
                }
                
                // Start observing shadow roots
                const shadowObserver = new MutationObserver((mutations) => {
                    mutations.forEach((mutation) => {
                        mutation.addedNodes.forEach((node) => {
                            if (node.nodeType === 1) { // Element node
                                if (node.shadowRoot) {
                                    node.shadowRoot.addEventListener('input', handleInput, true);
                                    node.shadowRoot.addEventListener('change', handleInput, true);
                                    addShadowRootListeners(node.shadowRoot);
                                }
                            }
                        });
                    });
                });
                
                shadowObserver.observe(document.body, {
                    childList: true,
                    subtree: true
                });
                
                // Initial scan for shadow roots
                addShadowRootListeners(document);
            }""")
            logger.info(f"Added event listeners to frame: {frame.url}")
        except Exception as e:
            logger.error(f"Error adding listeners to frame: {e}")

    async def _handle_load(self, page: Page) -> None:
        """Handle load events."""
        if not self.is_listening:
            return
            
        event = {
            "type": "recorded-load",
            "detail": {
                "url": page.url,
                "title": await page.title(),
                "timestamp": datetime.now().isoformat()
            }
        }
        self.events.append(event)
        logger.info(f"Recorded page load event: {page.url}")

    async def _handle_console(self, msg: ConsoleMessage) -> None:
        """Handle console messages to capture events."""
        if not self.is_listening:
            return
            
        try:
            if msg.type == 'log':
                text = msg.text
                if text.startswith('__pw_click'):
                    event_data = json.loads(text.replace('__pw_click ', ''))
                    event = {
                        'type': 'recorded-click',
                        'detail': event_data
                    }
                    self.events.append(event)
                    logger.info(f"Captured click event at coordinates: ({event_data.get('coordinates', {}).get('x')}, {event_data.get('coordinates', {}).get('y')})")
                    if event_data.get('element'):
                        element = event_data['element']
                        logger.info(f"  Element: {element.get('tagName')}, XPath: {element.get('xpath')}, ShadowPath: {element.get('shadowPath')}")
                elif text.startswith('__pw_input'):
                    event_data = json.loads(text.replace('__pw_input ', ''))
                    event = {
                        'type': 'recorded-input',
                        'detail': event_data
                    }
                    self.events.append(event)
                    logger.info(f"Captured input event with value: {event_data.get('value')}")
                    if event_data.get('element'):
                        element = event_data['element']
                        logger.info(f"  Element: {element.get('tagName')}, XPath: {element.get('xpath')}, ShadowPath: {element.get('shadowPath')}")
        except Exception as e:
            logger.error(f"Error handling console message: {str(e)}")

    def get_events(self) -> List[Dict]:
        """Get all recorded events."""
        logger.info(f"Returning {len(self.events)} recorded events")
        return self.events 