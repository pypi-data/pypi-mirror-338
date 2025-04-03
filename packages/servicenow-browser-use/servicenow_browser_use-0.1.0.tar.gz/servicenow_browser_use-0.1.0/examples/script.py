import sys
import asyncio
from langchain_openai import AzureChatOpenAI
from servicenow_browser_use import Agent
from dotenv import load_dotenv
from pydantic import SecretStr
from servicenow_browser_use import BrowserConfig
from servicenow_browser_use.browser.browser import Browser
from servicenow_browser_use.browser.context import BrowserContextConfig
from servicenow_browser_use.browser.streamlined_recorder import StreamlinedRecorder
import os
import logging
import subprocess
from datetime import datetime
import time
import requests
import importlib.util

logger = logging.getLogger(__name__)

def wait_for_chrome_debugger(port=9222, max_retries=10, retry_interval=1):
    """Wait for Chrome debugger to be available on the specified port."""
    for i in range(max_retries):
        try:
            response = requests.get(f"http://localhost:{port}/json/version")
            if response.status_code == 200:
                logger.info("Chrome debugger is available")
                return True
        except requests.exceptions.ConnectionError:
            logger.debug(f"Chrome debugger not available yet (attempt {i+1}/{max_retries})")
            time.sleep(retry_interval)
    return False

def run_selenium_generator():
    """Run the Selenium code generator after recording is complete."""
    try:
        # Import the generator module directly
        from generate_selenium_from_recording import generate_selenium_code
        
        # Find the most recent streamlined recording file
        recording_files = [f for f in os.listdir("output") if f.startswith("streamlined_recording_") and f.endswith(".json")]
        if not recording_files:
            logger.error("No streamlined recording files found in output directory")
            return
            
        latest_recording = max(recording_files, key=lambda x: os.path.getctime(os.path.join("output", x)))
        java_file = generate_selenium_code(os.path.join("output", latest_recording))
        
        if java_file:
            logger.info(f"Successfully generated Selenium test code at: {java_file}")
        else:
            logger.error("Failed to generate Selenium test code")
    except Exception as e:
        logger.error(f"Error running Selenium generator: {str(e)}")

async def main(task, llm_model):
    # Create output directory if it doesn't exist
    os.makedirs("output", exist_ok=True)
    os.makedirs("logs/conversation", exist_ok=True)  # Create conversation logs directory
    
    # Clean up any existing Chrome instances
    subprocess.run(["pkill", "Chrome"], capture_output=True)
    await asyncio.sleep(2)  # Wait for processes to clean up
    
    config = BrowserConfig(
        chrome_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        disable_security=True,  # Required for shadow DOM support
        extra_chromium_args=[
            '--remote-debugging-port=9222',
            '--disable-web-security',
            '--disable-site-isolation-trials',
            '--enable-logging',
            '--v=1',
            '--no-sandbox',
            '--disable-dev-shm-usage'
        ],
        new_context_config=BrowserContextConfig(
            save_recording_path='output',  # Enable recording
            browser_window_size={'width': 1280, 'height': 720},
            wait_for_network_idle_page_load_time=2.0,  # Increase wait time for network idle
            minimum_wait_page_load_time=1.0  # Increase minimum wait time
        )
    )

    # Initialize browser
    browser = Browser(config=config)
    
    try:
        # Initialize the browser and get the Playwright browser instance
        playwright_browser = await browser.get_playwright_browser()
        if not playwright_browser:
            raise Exception("Failed to initialize browser")
        
        # Wait for browser to initialize
        await asyncio.sleep(3)  # Give Chrome more time to start up
        
        # Wait for Chrome debugger to be available
        logger.info("Waiting for Chrome debugger to be available...")
        if not wait_for_chrome_debugger(retry_interval=2):
            raise Exception("Chrome debugger not available after maximum retries")
        
        llm = AzureChatOpenAI(
            model=llm_model,
            api_version="2024-10-21",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
            api_key=SecretStr(os.getenv("AZURE_OPENAI_KEY", "")),
        )
        
        # Initialize agent with browser
        agent = Agent(
            task=task,
            llm=llm,
            browser=browser,  # Pass the browser instance to the agent
            save_conversation_path="logs/conversation",
        )

        # Run the agent and get results
        result = await agent.run()
        
        # Process results
        if result:
            print("Task completed successfully!")
            print("Final state:", result)
            
            # Run the Selenium code generator
            logger.info("Generating Selenium test code...")
            run_selenium_generator()
        else:
            print("Task failed or returned no results")
            
    except Exception as e:
        logger.error(f"Error during agent execution: {str(e)}")
        raise
    finally:
        # Close the browser
        try:
            if browser:
                await browser.close()
        except Exception as e:
            logger.error(f"Error closing browser: {str(e)}")
        
        # Finally clean up Chrome processes
        try:
            subprocess.run(["pkill", "Chrome"], capture_output=True)
        except Exception as e:
            logger.error(f"Error during Chrome cleanup: {str(e)}")

if __name__ == "__main__":
    load_dotenv()
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Get ServiceNow URL from environment variables
    servicenow_url = os.getenv('SERVICENOW_URL')
    if not servicenow_url:
        raise ValueError("SERVICENOW_URL not found in environment variables")
    
    task = f"Open {servicenow_url}, then login with username: admin, password: admin, click on 'New' button and check if 'Flow' tab is present"
    llm_model = "gpt-4o"
    asyncio.run(main(task, llm_model))
