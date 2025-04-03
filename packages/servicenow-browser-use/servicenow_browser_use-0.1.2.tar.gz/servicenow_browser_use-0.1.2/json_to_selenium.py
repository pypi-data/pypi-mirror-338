import json
import os
from datetime import datetime

def get_element_selector(element_info):
    """Get the best selector for an element based on available information."""
    if not element_info:
        return None
        
    # If shadow DOM path is available, use it
    if element_info.get('shadowPath'):
        shadow_selectors = []
        for path in element_info['shadowPath']:
            host = path['host']
            selector = host['tagName'].lower()
            if host['id']:
                selector += f"#{host['id']}"
            elif host['className']:
                selector += f".{host['className'].replace(' ', '.')}"
            shadow_selectors.append(selector)
        return f"findElementWithShadowDOM(\"{' >>> '.join(shadow_selectors)}\")"
        
    # If XPath is available, use it
    elif element_info.get('xpath'):
        return f"By.xpath(\"{element_info['xpath']}\")"
        
    # Fallback to tag name
    else:
        return f"By.tagName(\"{element_info['tagName']}\")"

def process_action(action):
    """Process a single action into Selenium commands."""
    commands = []
    
    action_type = action.get('type')
    element_info = action.get('element')
    
    if action_type == 'navigate':
        url = action.get('url')
        if url:
            commands.append(f"driver.get(\"{url}\");")
            commands.append("Thread.sleep(1000);")  # Wait for page load
            
    elif action_type == 'click':
        if element_info:
            selector = get_element_selector(element_info)
            if selector:
                commands.append(f"WebElement element = driver.findElement({selector});")
                commands.append("waitForElementToBeClickable(element);")
                commands.append("scrollToElement(element);")
                commands.append("element.click();")
                commands.append("Thread.sleep(1000);")
            
    elif action_type == 'type':
        if element_info:
            selector = get_element_selector(element_info)
            text = action.get('text', '')
            if selector:
                commands.append(f"WebElement element = driver.findElement({selector});")
                commands.append("waitForElementToBeClickable(element);")
                commands.append("scrollToElement(element);")
                commands.append("element.clear();")
                commands.append(f"element.sendKeys(\"{text}\");")
                commands.append("Thread.sleep(500);")
                
    elif action_type == 'send_keys':
        keys = action.get('keys')
        if keys:
            commands.append(f"actions.sendKeys(Keys.{keys.upper()}).perform();")
            commands.append("Thread.sleep(500);")
            
    elif action_type == 'switch_tab':
        page_id = action.get('page_id')
        if page_id is not None:
            commands.append(f"ArrayList<String> tabs = new ArrayList<>(driver.getWindowHandles());")
            commands.append(f"driver.switchTo().window(tabs.get({page_id}));")
            commands.append("Thread.sleep(1000);")
            
    return commands

def generate_selenium_code(recording_file):
    """Generate Selenium Java code from the recording file."""
    with open(recording_file, 'r') as f:
        data = json.load(f)
    
    # Extract actions
    actions = data.get('actions', [])
    
    # Generate commands for each action
    all_commands = []
    for action in actions:
        commands = process_action(action)
        all_commands.extend(commands)
    
    # Generate the Java code
    java_code = f"""package com.selenium.test;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;
import java.time.Duration;
import org.testng.annotations.*;
import java.util.ArrayList;

public class SeleniumTest_{datetime.now().strftime('%Y%m%d')} {{
    private static WebDriver driver;
    private static WebDriverWait wait;
    private static Actions actions;
    private static JavascriptExecutor js;

    @BeforeClass
    public static void setup() {{
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        options.addArguments("--disable-web-security");
        options.addArguments("--disable-site-isolation-trials");
        driver = new ChromeDriver(options);
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
        actions = new Actions(driver);
        js = (JavascriptExecutor) driver;
    }}

    @AfterClass
    public static void tearDown() {{
        if (driver != null) {{
            driver.quit();
        }}
    }}

    private static WebElement findElementWithShadowDOM(String shadowPath) {{
        String[] selectors = shadowPath.split(" >>> ");
        WebElement element = null;
        
        for (String selector : selectors) {{
            if (element == null) {{
                element = driver.findElement(By.cssSelector(selector));
            }} else {{
                element = (WebElement) js.executeScript("return arguments[0].shadowRoot", element);
                element = element.findElement(By.cssSelector(selector));
            }}
        }}
        return element;
    }}

    private static void waitForElementToBeClickable(WebElement element) {{
        wait.until(ExpectedConditions.elementToBeClickable(element));
    }}

    private static void scrollToElement(WebElement element) {{
        js.executeScript("arguments[0].scrollIntoView(true);", element);
    }}

    @Test
    public void runTest() {{
        try {{
            {chr(10).join(all_commands)}
        }} catch (Exception e) {{
            e.printStackTrace();
        }}
    }}
}}"""
    
    # Create java directory if it doesn't exist
    os.makedirs("java", exist_ok=True)
    
    # Save the Java code
    output_file = f"java/SeleniumTest_{datetime.now().strftime('%Y%m%d')}.java"
    with open(output_file, 'w') as f:
        f.write(java_code)
    
    print(f"Generated Selenium test: {output_file}")

if __name__ == "__main__":
    # Find the most recent recording file
    recording_files = [f for f in os.listdir("output") if f.startswith("agent_recording_") and f.endswith(".json")]
    if not recording_files:
        print("No recording files found in output directory")
        exit(1)
    
    latest_recording = max(recording_files, key=lambda x: os.path.getctime(os.path.join("output", x)))
    generate_selenium_code(os.path.join("output", latest_recording))
