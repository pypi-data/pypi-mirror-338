from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="servicenow-browser-use",
    version="0.1.0",
    author="Joshita Das",
    author_email="joshita.das@servicenow.com",
    description="A browser automation library specifically designed for ServiceNow applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joshita-das/servicenow-browser-use",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "playwright>=1.40.0",
        "langchain-openai>=0.0.5",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "selenium>=4.15.0",
    ],
    include_package_data=True,
    package_data={
        "servicenow_browser_use": ["dom/*.js"],
    },
) 