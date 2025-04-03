from setuptools import setup, find_packages

setup(
    name="browser_automation_agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "playwright>=1.40.0",
        "langchain-openai>=0.0.5",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "selenium>=4.15.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A browser automation agent that can record and generate Selenium tests",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/browser_automation_agent",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
) 