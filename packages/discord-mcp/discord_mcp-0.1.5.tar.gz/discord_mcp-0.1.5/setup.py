#!/usr/bin/env python3
"""
Setup script for Discord MCP Server package
"""

from setuptools import setup, find_packages
import os
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Package requirements
requirements = [
    "mcp[cli]>=0.1.0",
    "bm25s>=0.2.10",
    "numpy>=1.24.0",
    "tqdm>=4.66.1",
    "requests>=2.31.0",
    "pytz>=2023.3",
    "flask>=2.3.0",
    "python-dotenv>=1.0.0",
]

# Package data files to include
package_data = {
    "discord_mcp": [
        "static/css/*.css",
        "templates/*.html",
    ],
}

# Entry points for command-line scripts
entry_points = {
    "console_scripts": [
        "discord-mcp=discord_mcp_server:main_cli",
        "discord-webui=discord_webui:main_cli",
    ],
}

setup(
    name="discord-mcp",
    version="0.1.0",
    description="Discord Message Context Provider for Claude",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Louis DiLello",
    author_email="discord-mcp@example.com",  # Replace with actual email
    url="https://github.com/LouD82/discord-mcp",
    py_modules=[
        "discord_mcp_server", 
        "discord_webui", 
        "discord_exporter", 
        "db_service",
        "bm25s",
        "remote_client",
    ],
    packages=find_packages(),
    package_data=package_data,
    install_requires=requirements,
    entry_points=entry_points,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Topic :: Communications :: Chat",
        "Topic :: Utilities",
    ],
    python_requires=">=3.10",
)