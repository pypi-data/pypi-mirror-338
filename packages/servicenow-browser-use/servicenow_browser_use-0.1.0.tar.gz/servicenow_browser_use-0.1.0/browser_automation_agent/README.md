# Browser Automation Agent

A powerful browser automation library that can record browser interactions and generate Selenium test code using AI.

## Features

- Browser interaction recording
- AI-powered task execution
- Selenium test code generation
- Shadow DOM support
- Network request monitoring
- Customizable browser configurations

## Installation

```bash
pip install browser-automation-agent
```

## Quick Start

```python
import asyncio
from browser_automation_agent import Agent, BrowserConfig
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from pydantic import SecretStr
import os

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
        ]
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
```

## Configuration

The library supports various configuration options through `BrowserConfig`:

- `chrome_instance_path`: Path to Chrome executable
- `disable_security`: Disable security features for testing
- `extra_chromium_args`: Additional Chrome arguments
- `save_recording_path`: Directory to save browser recordings
- `browser_window_size`: Browser window dimensions
- `wait_for_network_idle_page_load_time`: Time to wait for network idle
- `minimum_wait_page_load_time`: Minimum page load wait time

## Environment Variables

Required environment variables:
- `AZURE_OPENAI_ENDPOINT`: Azure OpenAI endpoint URL
- `AZURE_OPENAI_KEY`: Azure OpenAI API key

## License

MIT License 