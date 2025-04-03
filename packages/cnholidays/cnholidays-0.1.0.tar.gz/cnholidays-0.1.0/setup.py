"""
cnholidays packaging script
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cnholidays",
    version="0.1.0",
    author="Python Developer",
    author_email="author@example.com",
    description="Chinese holiday and workday determination library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cnholidays",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/cnholidays/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Natural Language :: English",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "holidays>=0.25",
    ],
) 