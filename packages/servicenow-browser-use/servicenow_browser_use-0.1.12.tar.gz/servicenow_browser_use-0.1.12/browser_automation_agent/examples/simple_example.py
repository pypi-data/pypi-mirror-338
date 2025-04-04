import asyncio
import os
from dotenv import load_dotenv
from pydantic import SecretStr
from langchain_openai import AzureChatOpenAI
from browser_automation_agent import Agent, BrowserConfig, BrowserContextConfig

async def main():
    # Load environment variables
    load_dotenv()
    
    # Configure browser
    config = BrowserConfig(
        chrome_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # Adjust path as needed
        disable_security=True,
        extra_chromium_args=[
            '--remote-debugging-port=9222',
            '--disable-web-security',
            '--no-sandbox'
        ],
        new_context_config=BrowserContextConfig(
            save_recording_path='output',
            browser_window_size={'width': 1280, 'height': 720},
            wait_for_network_idle_page_load_time=2.0,
            minimum_wait_page_load_time=1.0
        )
    )
    
    # Initialize LLM
    llm = AzureChatOpenAI(
        model="gpt-4",
        api_version="2024-10-21",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=SecretStr(os.getenv("AZURE_OPENAI_KEY")),
    )
    
    # Create agent
    agent = Agent(
        task="login with username: admin, password: admin",
        llm=llm,
        browser_config=config
    )
    
    # Run agent
    result = await agent.run()
    print("Task completed:", result)

if __name__ == "__main__":
    asyncio.run(main()) 