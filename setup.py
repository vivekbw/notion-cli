"""
This module enables notion_cli to be interfaced with from the terminal similar to other CLI's

Typical usage example (from terminal):
    $ python3 notion_cli send 'Vivek' 'Christopher' 'Hello Chris!' '2024-08-18T09:00:00'
    $ python3 notion_cli read 'Christopher'
    $ python3 notion_cli search "Hello"
    $ python3 notion_cli clear
"""
from setuptools import setup, find_packages

setup(
    name="notion_cli",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "notion-client>=0.7.0",
        "click>=8.0.1",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        'console_scripts': [
            'notion_cli=notion_cli.cli:cli',
        ],
    },
)
