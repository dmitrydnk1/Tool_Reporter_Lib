"""
Example: for the intial setup of reporter CFG, or later modifications.

The script demonstrate how to set default parameters.
The parameters can be set only once, by running similar scripts, 
and it will saved the CFG in module. In a future use, it will be atomaticly loaded.

Usage
-----
Run the script directly form this folder in a command line.

    python examples/reporter_intial_CFG_setup.py
"""

import tool_reporter_lib

# chck if the package is installed
print(tool_reporter_lib.__version__)

# Get Configuration Object:
from tool_reporter_lib import Reports_Settings

# Set Default Report Path:

# OPTION 1: Set Absolute Path:
Reports_Settings.set_default_report_path('C:/Reports')

# OPTION 2: Set Relative Path:
Reports_Settings.set_default_report_path('Reports')

# Setup Complited !