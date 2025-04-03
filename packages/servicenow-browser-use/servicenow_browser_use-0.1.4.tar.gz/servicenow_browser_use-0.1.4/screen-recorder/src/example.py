from .recorder import ScreenRecorder
import json
import time
import os
import psutil
import logging
import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def detect_browser():
    """Detect if Chrome or Chromium is installed"""
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    chromium_path = "/Applications/Chromium.app/Contents/MacOS/Chromium"
    
    if os.path.exists(chrome_path):
        return "chrome", chrome_path
    elif os.path.exists(chromium_path):
        return "chromium", chromium_path
    else:
        return None, None

def initialize_driver(browser_type, browser_path):
    """Initialize WebDriver with proper options"""
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = browser_path
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://www.google.com')
        return driver
    except Exception as e:
        logging.error(f"Error initializing {browser_type} WebDriver: {e}")
        return None

def main():
    # Create output directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Detect browser
    browser_type, browser_path = detect_browser()
    if not browser_type:
        logging.error("Neither Chrome nor Chromium found!")
        return
    
    # Initialize WebDriver
    logging.info(f"Initializing {browser_type} WebDriver...")
    driver = initialize_driver(browser_type, browser_path)
    if not driver:
        logging.error(f"Failed to initialize {browser_type} WebDriver!")
        return
    
    logging.info(f"{browser_type} WebDriver initialized successfully")
    
    # Initialize recorder with detected browser and WebDriver
    recorder = ScreenRecorder(browser_type=browser_type, driver=driver)

    try:
        print(f"Starting recording in 3 seconds... (Active browser: {browser_type})")
        time.sleep(3)
        
        # Start recording
        recorder.start_recording()
        print("Recording started! Press Ctrl+C to stop.")
        print(f"Recording actions for: {browser_type}")
        
        # Keep the script running
        while True:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nStopping recording...")
        recording_data = recorder.stop_recording()
        
        # Add browser information to recording data
        recording_data.update({
            "browser": browser_type,
            "browser_version": recorder.get_browser_version(),
            "recording_timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # Save to file with timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"recording_{browser_type}_{timestamp}.json")
        with open(output_file, "w") as f:
            json.dump(recording_data, f, indent=2)
            
        print(f"Recording saved to {output_file}")
        print(f"Browser: {browser_type}")
        print(f"Total actions recorded: {len(recording_data.get('tests', [{}])[0].get('commands', []))}")
        
        # Close the browser
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    main() 