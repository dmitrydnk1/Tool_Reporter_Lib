# ============================================================================================
#                                   Tool Reporter Library
# ============================================================================================

"""
Tool Reporter Library

This library provides tools for generating HTML reports with various content elements such as
titles, text, charts, tables, and more. It is designed for documenting the results of data 
analysis, machine learning models, or any project that requires a structured presentation 
of information.

---

Example Usage
-------------
>>> from tool_reporter_lib import ReportHTML
>>> # Create a Report:
>>> report = ReportHTML('My Report')
>>> report.add_title('My Report')
>>> report.add_text('This is a sample report.')
>>> report.save()

Set Parameters
--------------
>>> from tool_reporter_lib import Reports_Settings
>>> Reports_Settings.set_default_report_path('C:/Reports') # and others availablle settings

"""

# ============================================================================================
# Library Version Information
# ============================================================================================

_name_:           str = 'Tool Reporter Lib'
__version__:      str = '0.0.9'
__version_date__: str = '2024-10-20'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.1 @ 2024-07-13   : Initial Release
# v0.0.2 @ 2024-08-13   : Added Class Extension Module
#                       : Added Plotting Module
#                       : Added Reporter Module
#                       : Added ChatBot Message Module
# v0.0.3 @ 2024-08-15   : Replaced Class Extension Module to a separate package
#                       : Updated sub-modules dependencies.
# v0.0.4 @ 2024-08-20   : Updated Annotations and Documentation
# v0.0.5 @ 2024-08-21   : Updated visual styles for compatibility with JupyterLab
# v0.0.6 @ 2024-08-21   : Updated Report Style and Elements
#                       : Replaced header images with random generated backgrounds
#                       : Restructured package to remove unnecessary images
# v0.0.7 @ 2024-09-18   : Improved df heatmap color range for better visibility
#                       : Updated documentation with more examples and use-cases
# v0.0.9 @ 2024-10-20   : Enhanced Report Style Loader to clean and validate CSS content
#                       : Added CSS cleaning and validation functions
#                       : Separated CSS file path retrieval from content loading
# ============================================================================================

# ============================================================================================
#
#           Initialize the Report Settings:
#
# ============================================================================================

from .utils.report_settings import Reports_Settings
Reports_Settings.activate_default_report_path()   # Set Default Report Path from the Settings.

# ============================================================================================
#
#                   Import Reporter Module:
#
# ============================================================================================

from .report_generator import ReportHTML

# ============================================================================================
