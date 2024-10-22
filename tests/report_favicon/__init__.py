"""
Tests for report_favicon
------------------------

This module provides unit tests for the functionality that retrieves a base64-encoded favicon 
for use in HTML reports. The favicon is read from an external file or, if the file is not found, 
a small fallback 1x1 transparent PNG is used.

Version History:
- v0.0.2 @ 2024-08-13 : Initial Release

Modules Tested:
---------------
- fav_icon : Tests the function `_get_base64_favicon()` for correctness and fallback behavior.

"""

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'Tests - report favicon'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY ------------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================

# --- TODO -----------------------------------------------------------------------------------
# -
# ============================================================================================

# --- Importing Test Modules -----------------------------------------------------------------
import unittest

# --- Import the function to be tested from the main module. ---------------------------------
from src.tool_reporter_lib.report_favicon.fav_icon import _get_base64_favicon

# --- Import each Test class -----------------------------------------------------------------
from .test_fav_icon import TestFavIcon

# ============================================================================================