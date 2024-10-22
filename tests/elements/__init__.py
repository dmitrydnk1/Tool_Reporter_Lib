"""
Tests for Reporter - Report Elements
====================================

This module provides unit tests for various report elements used for generating HTML-based reports,
such as charts, alert boxes, headers, footers, tables, and more. Each test is designed to ensure 
that the `ReportElement` objects are working as intended and can be easily integrated into an HTML report.

Version: 0.0.2
Date: 2024-08-13
"""

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'Tests - Reporter - Report Elements'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY -------------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# =============================================================================================

# --- TODO ------------------------------------------------------------------------------------
# - 
# ---------------------------------------------------------------------------------------------

# --- Importing Test Modules ------------------------------------------------------------------
import unittest

# --- Importing the necessary elements to test ------------------------------------------------
from src.tool_reporter_lib.elements.report_element import ReportElement, ReportElementTypes
from src.tool_reporter_lib.elements import (
    report_element_alert_box,
    report_element_chart,
    report_element_code,
    report_element_footer,
    report_element_header_title,
    report_element_horizontal_line,
    report_element_param_val_table,
    report_element_showhide,
    report_element_space,
    report_element_style,
    report_element_table_df,
    report_element_text,
    report_element_text_console,
    report_element_title,
)

# --- Import each Test class -----------------------------------------------------------------

from .test_report_element_alert_box         import TestReportElementAlertBox
from .test_report_element_chart             import TestGetChartElement
from .test_report_element_code              import TestGetCodeElement
from .test_report_element_footer            import TestReportElementFooter
from .test_report_element_header_title      import TestReportElementHeaderTitle
from .test_report_element_horizontal_line   import TestReportElementHorizontalLine
from .test_report_element_param_val_table   import TestReportElementParamValTable
from .test_report_element_showhide          import TestReportElementShowHide
from .test_report_element_space             import TestReportElementSpace
from .test_report_element_style             import TestReportElementStyle
from .test_report_element_table_df          import TestReportElementTableDF
from .test_report_element_text              import TestReportElementText
from .test_report_element_text_console      import TestReportElementTextConsole
from .test_report_element_title             import TestGetTitleElement

# --------------------------------------------------------------------------------------------