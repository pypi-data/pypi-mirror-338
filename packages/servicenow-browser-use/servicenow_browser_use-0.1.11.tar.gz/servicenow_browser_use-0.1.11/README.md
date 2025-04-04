# ServiceNow Browser Use

A Python library for browser automation specifically designed for ServiceNow applications.

## Installation

```bash
pip install servicenow-browser-use
```

## Usage

```python
from servicenow_browser_use import Agent, BrowserConfig
from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure browser
config = BrowserConfig(
    chrome_instance_path="/path/to/chrome",
    disable_security=True
)

# Initialize LLM
llm = AzureChatOpenAI(
    model="gpt-4",
    api_version="2024-10-21",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY")
)

# Create agent
agent = Agent(
    task="your task here",
    llm=llm,
    browser=config
)

# Run agent
result = await agent.run()
```

## Features

- Browser automation using Playwright
- Integration with Azure OpenAI for natural language task processing
- Support for ServiceNow-specific interactions
- Shadow DOM support
- Recording and playback capabilities

## License

MIT License

```bibtex
@software{browser_use2024,
  author = {Müller, Magnus and Žunič, Gregor},
  title = {Browser Use: Enable AI to control your browser},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/browser-use/browser-use}
}
```

---

