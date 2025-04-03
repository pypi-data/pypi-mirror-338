#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="terminal-llm-assistant",
    version="0.1.0",
    author="Angelo Vicente Filho",
    author_email="angelo.vicente@veolia.com",
    description="Assistente de terminal que integra com a API do Google Gemini",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/terminal-llm-assistant",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "python-dotenv>=1.0.0",
        "requests>=2.25.0",
        "litellm>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "terminal-llm=terminal_llm_assistant.cli:main",
            "ai=terminal_llm_assistant.cli:ask",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Particular License",
        "Operating System :: OS Linux",
    ],
)
