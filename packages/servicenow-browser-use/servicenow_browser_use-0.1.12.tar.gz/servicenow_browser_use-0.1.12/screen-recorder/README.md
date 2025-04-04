# Screen Recorder

A Python-based screen recorder that captures user interactions and generates Selenium IDE-compatible test files, with full support for shadow DOM elements.

## Features

- Records mouse movements, clicks, and scrolling
- Captures keyboard input
- Generates Selenium IDE-compatible JSON output
- Supports shadow DOM elements
- Includes element location information
- Provides multiple locator strategies
- Debounces events to reduce noise
- Captures screenshots

## Requirements

- Python 3.7+
- Chrome browser installed
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd screen-recorder
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the example script:
```bash
python src/example.py
```

2. Wait for the 3-second countdown
3. Perform the actions you want to record
4. Press Ctrl+C to stop recording
5. The recorded test will be saved to `recorded_test.json`

## Shadow DOM Support

The recorder automatically detects and handles shadow DOM elements:

1. **Detection**: Uses JavaScript to identify elements within shadow roots
2. **Locator Generation**: Creates XPath locators that work with shadow DOM
3. **Alternative Locators**: Provides multiple locator strategies for better reliability
4. **Shadow Root Path**: Includes shadow root information in element paths

Example of a shadow DOM element locator:
```json
{
  "command": "click",
  "target": "shadow=//*[@id='shadow-host']/div[1]/button",
  "targets": [
    "id=shadow-host",
    "css=.shadow-container",
    "shadow=//*[@id='shadow-host']/div[1]/button"
  ]
}
```

## Output Format

The generated JSON file follows the Selenium IDE format:

```json
{
  "id": "recording_20240315_123456",
  "version": "1.0",
  "name": "Recorded Test",
  "url": "screen_recording",
  "tests": [
    {
      "id": "test_1",
      "name": "Screen Recording Test",
      "commands": [
        {
          "id": "command_1",
          "comment": "",
          "command": "click",
          "target": "shadow=//*[@id='shadow-host']/div[1]/button",
          "targets": [
            "id=shadow-host",
            "css=.shadow-container",
            "shadow=//*[@id='shadow-host']/div[1]/button"
          ],
          "value": "",
          "time": 1.234
        }
      ]
    }
  ],
  "urls": [],
  "plugins": [],
  "variables": {},
  "suites": [
    {
      "id": "suite_1",
      "name": "Default Suite",
      "persistSession": false,
      "parallel": false,
      "timeout": 300,
      "tests": ["test_1"]
    }
  ]
}
```

## Project Structure

- `src/recorder.py`: Main screen recording functionality
- `src/event_handler.py`: Handles mouse and keyboard events
- `src/element_locator.py`: Locates elements, including shadow DOM
- `src/command_generator.py`: Converts events to Selenium IDE commands
- `src/example.py`: Example usage of the recorder

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 