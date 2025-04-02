"""
@author: Ranuja Pinnaduwage

This file is part of pyprofilerai, a Python package that combines profiling 
with AI-based performance optimization suggestions.

Description:
This file implements the setup of the python package.

Based on Python's cProfile module for performance analysis and utilizes Google Gemini.  
Copyright (C) 2025 Ranuja Pinnaduwage  
Licensed under the MIT License.  

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:  

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
"""

from setuptools import setup, find_packages

setup(
    name="pyprofilerai",  # Package name
    version="0.1.0",  # Version number
    author="Ranuja Pinnaduwage",
    author_email="Ranuja.Pinnaduwage@gmail.com",
    description="A python profiling tool with AI-based suggestions for performance optimization",  # Package description
    long_description=open('README.md').read(),  # Read long description from README file
    long_description_content_type="text/markdown",  # Markdown format for README
    url="https://github.com/Ranuja01/pyprofilerai",
    packages=find_packages(where="src"),  # Locate all packages under src/
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Use MIT License
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Specify Python version requirement
    install_requires=[  # Dependencies
        "google-genai",
    ],
    include_package_data=True,  # Ensure non-Python files (like README.md) are included
    zip_safe=False,  # Indicate if the package can be reliably used as a .egg file
    # entry_points={  # Optional: define entry points if you want to add CLI commands
    #     "console_scripts": [
    #         "pyprofilerai=pyprofilerai.cli:main",  # If you define a command-line tool
    #     ],
    # },
)
