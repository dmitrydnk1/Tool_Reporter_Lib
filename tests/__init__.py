"""
Tests for Tool Reporter Library
===============================

This package contains unit tests for the Tool Reporter Library, which provides tools for generating HTML reports 
with various content elements such as titles, text, charts, tables, and more. It is designed to verify the 
functionality and robustness of report generation, settings management, and different report components.

---

Example Test Usage
------------------
>>> from tests import TestReportHTML
>>> # Run all tests:
>>> unittest.main()

Modules Tested
--------------
- ReportHTML: Verifies the creation of reports with different elements.
- Reports_Settings: Validates the setting of default report paths and other configurations.

"""

# ============================================================================================
# Meta Information
__version__:      str = '0.0.9'
__version_date__: str = '2024-10-20'
_name_:           str = 'Tests - Tool Reporter Lib'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY ------------------------------------------------------------------------
# v0.0.1 @ 2024-07-13 : Initial Release
# v0.0.2 @ 2024-08-13 : Added unit tests for the Reporter Module
# v0.0.3 @ 2024-08-15 : Updated unit tests for changes in module dependencies
# v0.0.4 @ 2024-08-20 : Improved tests for settings management and HTML generation
# v0.0.9 @ 2024-10-20 : Added tests for CSS cleaning and validation functions
# ============================================================================================

# --- TODO -----------------------------------------------------------------------------------
# - 
# ============================================================================================

# --- Importing Test Modules -----------------------------------------------------------------
import unittest

# --- Import the main modules to be tested --------------------------------------------------
from src.tool_reporter_lib.utils.report_settings import Reports_Settings
from src.tool_reporter_lib import ReportHTML

# --- Importing Test Modules -----------------------------------------------------------------
from .test_report_generator      import TestReportHTML
from .utils.test_report_settings import TestReportsSettings

# ============================================================================================