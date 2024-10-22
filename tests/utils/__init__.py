"""
Tests for Tools - Utils Package
===============================

This package contains unit tests for the core utilities and settings management used for 
HTML report generation in the Tools - Utils package.

Version: 0.0.9
Date: 2024-10-20

Modules Tested:
---------------

1. report_settings.py:
    - Tests the various settings management for report generation, including file paths, 
      folder paths, and HTML report customization options.

2. report_utils.py:
    - Tests utility functions such as filename sanitization, generating the current date 
      and time, updating filenames, and cleaning HTML code to reduce file size.

"""

# ============================================================================================
# Meta Information
__version__:      str = '0.0.9'
__version_date__: str = '2024-10-20'
_name_:           str = 'Tests - Tools - Utilities'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY ------------------------------------------------------------------------
# v0.0.1 @ 2024-08-13 : Initial Release
# v0.0.2 @ 2024-08-20 : Added tests for report settings and utility functions.
# v0.0.9 @ 2024-10-20 : Updated test cases and added tests for the HTML cleaning function.
# ============================================================================================

# --- TODO -----------------------------------------------------------------------------------
# -
# ============================================================================================

# --- Importing Test Modules -----------------------------------------------------------------
import unittest

# --- Import the utilities to be tested from the main utils package. -------------------------
from src.tool_reporter_lib.utils.report_settings import Reports_Settings
from src.tool_reporter_lib.utils.report_utils import (
    sanitize_filename,
    update_filename,
    get_current_datetime,
    get_clean_HTML_code
)

# --- Importing Test Modules -----------------------------------------------------------------
from .test_report_settings import TestReportsSettings
from .test_report_utils import TestReportUtils

# ============================================================================================