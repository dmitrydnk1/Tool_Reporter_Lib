from setuptools import setup, find_packages
import os

# Safely reading the long description from README.md file
long_description = ''
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

# Safely reading dependencies from requirements.txt file
requirements = []
if os.path.exists("requirements.txt"):
    with open("requirements.txt") as req_file:
        requirements = req_file.read().splitlines()

setup(
    name                          = "tool_reporter_lib",                                 # The name of your package
    version                       = "0.0.9",                                             # Version of the package
    author                        = "Dmitry Klimenko",                                   # Author name
    author_email                  = "klimenko.dnk@gmail.com",                            # Author email
    description                   = "A tool for generating HTML reports with Python",    # Short description
    long_description              = long_description,                                    # Long description read from the README.md file
    long_description_content_type = "text/markdown",                                     # Content type of the long description
    url                           = "https://github.com/dmitrydnk1/tool-reporter-lib",   # URL to the project repository
    packages                      = find_packages(where='src'),                          # Automatically find all packages inside src folder
    package_dir                   = {"": "src"},                                         # The root directory of your packages
    classifiers                   = [
        "Programming Language :: Python :: 3",        
        "Operating System :: OS Independent",
    ],
    python_requires      = '>=3.7',      # Minimum Python version required
    install_requires     = requirements, # Reading dependencies from requirements.txt
    include_package_data = True,         # Include files from MANIFEST.in
    project_urls = {  # Additional URLs about the project
        'Source': 'https://github.com/dmitrydnk1/tool-reporter-lib',
    },
)
