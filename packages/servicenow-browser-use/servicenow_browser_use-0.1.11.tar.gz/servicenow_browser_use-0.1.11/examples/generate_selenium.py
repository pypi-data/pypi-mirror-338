import os
import json
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import re

def generate_selenium_code(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        # Extract relevant information from JSON
        actions = data.get('actions', [])
        browser_type = data.get('browser_type', 'chrome')
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Generate Java code
        java_code = create_selenium_code(actions, browser_type)
        
        # Create output directory if it doesn't exist
        java_output_dir = "selenium_tests"
        if not os.path.exists(java_output_dir):
            os.makedirs(java_output_dir)

        # Save Java code
        java_file = os.path.join(java_output_dir, f"SeleniumTest_{timestamp}.java")
        with open(java_file, 'w') as f:
            f.write(java_code)

        print(f"Generated Selenium test: {java_file}")
        return java_file

    except Exception as e:
        print(f"Error processing {json_file}: {str(e)}")
        return None

def create_selenium_code(actions, browser_type):
    # Generate Java class name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    class_name = f"SeleniumTest_{timestamp}"

    # Start with imports and class declaration
    code = [
        "package selenium_tests;",
        "",
        "import org.openqa.selenium.By;",
        "import org.openqa.selenium.WebDriver;",
        "import org.openqa.selenium.WebElement;",
        "import org.openqa.selenium.chrome.ChromeDriver;",
        "import org.openqa.selenium.chrome.ChromeOptions;",
        "import org.openqa.selenium.support.ui.ExpectedConditions;",
        "import org.openqa.selenium.support.ui.WebDriverWait;",
        "import java.time.Duration;",
        "",
        f"public class {class_name} {{",
        "    private WebDriver driver;",
        "    private WebDriverWait wait;",
        "",
        "    public void setUp() {",
        "        ChromeOptions options = new ChromeOptions();",
        "        options.addArguments(\"--remote-debugging-port=9222\");",
        "        options.addArguments(\"--disable-web-security\");",
        "        options.addArguments(\"--disable-site-isolation-trials\");",
        "        options.addArguments(\"--disable-features=IsolateOrigins,site-per-process\");",
        "        driver = new ChromeDriver(options);",
        "        wait = new WebDriverWait(driver, Duration.ofSeconds(10));",
        "    }",
        "",
        "    public void tearDown() {",
        "        if (driver != null) {",
        "            driver.quit();",
        "        }",
        "    }",
        "",
        "    public void runTest() {",
        "        try {",
        "            setUp();",
    ]

    # Add test steps based on actions
    for action in actions:
        if action['type'] == 'load':
            code.append(f"            driver.get(\"{action['url']}\");")
            code.append(f"            wait.until(ExpectedConditions.titleContains(\"{action['title']}\"));")
        elif action['type'] == 'click':
            element = action['element']
            if element.get('xpath'):
                code.append(f"            WebElement element = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(\"{element['xpath']}\")));")
                code.append("            element.click();")
            elif element.get('id'):
                code.append(f"            WebElement element = wait.until(ExpectedConditions.elementToBeClickable(By.id(\"{element['id']}\")));")
                code.append("            element.click();")
            elif element.get('className'):
                code.append(f"            WebElement element = wait.until(ExpectedConditions.elementToBeClickable(By.className(\"{element['className']}\")));")
                code.append("            element.click();")

    # Add main method
    code.extend([
        "        } catch (Exception e) {",
        "            e.printStackTrace();",
        "        } finally {",
        "            tearDown();",
        "        }",
        "    }",
        "",
        "    public static void main(String[] args) {",
        f"        {class_name} test = new {class_name}();",
        "        test.runTest();",
        "    }",
        "}"
    ])

    return "\n".join(code)

class JsonHandler(FileSystemEventHandler):
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.processed_files = set()

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.json') and event.src_path not in self.processed_files:
            self.processed_files.add(event.src_path)
            generate_selenium_code(event.src_path)

def main():
    # Set up the observer
    output_dir = "output"
    event_handler = JsonHandler(output_dir)
    observer = Observer()
    observer.schedule(event_handler, output_dir, recursive=False)
    
    # Start the observer
    observer.start()
    print(f"Monitoring {output_dir} for new JSON files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopping file monitoring...")
    observer.join()

if __name__ == "__main__":
    main() 