from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="anime-info-cli",
    version="2.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
        "termcolor"
    ],
    entry_points={
        "console_scripts": [
            "anime-info=anime_info.main:cli_entry_point",
        ]
    },
    author="Moritz Maier",
    author_email="moritzmaier353@gmail.com",
    description="A simple CLI application to fetch information such as title, genre, or ranking for any anime.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deinusername/anime-info-cli",  # Dein GitHub-Link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

