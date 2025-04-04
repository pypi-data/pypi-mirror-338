import os
from typing import Dict, List, Optional, Union, cast
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from playwright.async_api import Browser, Page, ElementHandle, BrowserContext
import time

class ElementLocator:
    def __init__(self, browser_type: str, driver: Union[WebDriver, Browser]):
        self.browser_type = browser_type
        self.driver = driver
        self.is_playwright = isinstance(driver, Browser)
        self.js_utils = self._load_js_utils()

    def _load_js_utils(self) -> str:
        """Load JavaScript utility functions from file"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        js_file = os.path.join(current_dir, "js_utils.js")
        with open(js_file, "r") as f:
            return f.read()

    async def locate_element(self, x: int, y: int) -> Optional[Dict]:
        """Get element location information at given coordinates"""
        if self.is_playwright:
            return await self._locate_element_playwright(x, y)
        else:
            return self._locate_element_selenium(x, y)

    async def _locate_element_playwright(self, x: int, y: int) -> Optional[Dict]:
        """Get element location information using Playwright"""
        try:
            # Get the current page
            browser = cast(Browser, self.driver)
            context = browser.contexts[0]
            page = context.pages[0]
            
            # Add JavaScript utilities
            await page.add_init_script(self.js_utils)
            
            # Get element at coordinates
            element = await page.evaluate("(x, y) => document.elementFromPoint(x, y)", x, y)
            
            if not element:
                return None
                
            # Get element details
            element_info = await page.evaluate("""(element) => {
                const rect = element.getBoundingClientRect();
                return {
                    tagName: element.tagName,
                    id: element.id,
                    className: element.className,
                    xpath: getXPath(element),
                    css: getCssPath(element),
                    rect: {
                        x: rect.x,
                        y: rect.y,
                        width: rect.width,
                        height: rect.height
                    }
                };
            }""", element)
            
            return element_info
            
        except Exception as e:
            print(f"Error locating element with Playwright: {e}")
            return None

    def _locate_element_selenium(self, x: int, y: int) -> Optional[Dict]:
        """Get element location information using Selenium"""
        try:
            # Add JavaScript utilities
            driver = cast(WebDriver, self.driver)
            driver.execute_script(self.js_utils)
            
            # Get element at coordinates using JavaScript
            element = driver.execute_script("""
                return document.elementFromPoint(arguments[0], arguments[1]);
            """, x, y)
            
            if not element:
                return None
                
            # Get element details
            element_info = driver.execute_script("""
                const element = arguments[0];
                const rect = element.getBoundingClientRect();
                return {
                    tagName: element.tagName,
                    id: element.id,
                    className: element.className,
                    xpath: getXPath(element),
                    css: getCssPath(element),
                    rect: {
                        x: rect.x,
                        y: rect.y,
                        width: rect.width,
                        height: rect.height
                    }
                };
            """, element)
            
            return element_info
            
        except Exception as e:
            print(f"Error locating element with Selenium: {e}")
            return None

    def _get_xpath_script(self) -> str:
        """Get the JavaScript function to generate XPath"""
        return r"""
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
        """

    def _get_css_script(self) -> str:
        """Get the JavaScript function to generate CSS selector"""
        return r"""
            function getCssPath(element) {
                if (element.id) {
                    return '#' + element.id;
                }
                
                let path = '';
                while (element && element.nodeType === 1) {
                    let selector = element.tagName.toLowerCase();
                    if (element.id) {
                        selector += '#' + element.id;
                    } else if (element.className) {
                        selector += '.' + element.className.split(' ').join('.');
                    }
                    path = selector + (path ? ' > ' + path : '');
                    element = element.parentNode;
                }
                return path;
            }
        """

    def _generate_xpath(self, element: Dict) -> str:
        """Generate XPath for an element"""
        try:
            tag_name = element.get('tagName', '').lower()
            attributes = element.get('attributes', {})
            
            # Try to create a unique XPath using id or other attributes
            if attributes.get('id'):
                return f"//{tag_name}[@id='{attributes['id']}']"
            elif attributes.get('name'):
                return f"//{tag_name}[@name='{attributes['name']}']"
            elif attributes.get('class'):
                return f"//{tag_name}[@class='{attributes['class']}']"
            else:
                return f"//{tag_name}"
                
        except Exception as e:
            print(f"Error generating XPath: {str(e)}")
            return ""

    def _get_shadow_root_path(self, element: Dict) -> str:
        """Generate a path to the shadow root"""
        try:
            shadow_host = element.get('shadowHost', {})
            tag_name = shadow_host.get('tagName', '').lower()
            attributes = shadow_host.get('attributes', {})
            
            # Try to create a unique XPath for the shadow host
            if attributes.get('id'):
                return f"//{tag_name}[@id='{attributes['id']}']"
            elif attributes.get('class'):
                return f"//{tag_name}[@class='{attributes['class']}']"
            else:
                return f"//{tag_name}"
                
        except Exception as e:
            print(f"Error getting shadow root path: {str(e)}")
            return ""

    def find_element_by_xpath(self, xpath: str) -> Optional[Dict]:
        """Find element by XPath, including shadow DOM elements"""
        try:
            # First try to find element directly
            element = self.driver.find_element(By.XPATH, xpath)
            if element:
                return {
                    'element': element,
                    'is_shadow': False
                }

            # If not found, try to find in shadow DOM
            shadow_elements = self.driver.execute_script("""
                function findElementInShadowDOM(xpath) {
                    let elements = [];
                    function searchShadowRoot(root) {
                        let element = root.querySelector(xpath);
                        if (element) {
                            elements.push({
                                element: element,
                                shadowRoot: root,
                                shadowHost: root.host
                            });
                        }
                        root.querySelectorAll('*').forEach(el => {
                            if (el.shadowRoot) {
                                searchShadowRoot(el.shadowRoot);
                            }
                        });
                    }
                    searchShadowRoot(document);
                    return elements;
                }
                return findElementInShadowDOM(arguments[0]);
            """, xpath)

            if shadow_elements and len(shadow_elements) > 0:
                return {
                    'element': shadow_elements[0]['element'],
                    'shadow_root': shadow_elements[0]['shadowRoot'],
                    'shadow_host': shadow_elements[0]['shadowHost'],
                    'is_shadow': True
                }

            return None

        except Exception as e:
            print(f"Error finding element by XPath: {str(e)}")
            return None

    def close(self):
        """Close the WebDriver"""
        if self.driver:
            self.driver.quit()
            self.driver = None 