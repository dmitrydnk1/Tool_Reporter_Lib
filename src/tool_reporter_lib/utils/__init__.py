# ============================================================================================
#                                  Tools - Utils Package
# ============================================================================================

__version__:      str = '0.0.9'
__version_date__: str = '2024-10-20'
_name_:           str = 'Tools - Utilities'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.1 @ 2024-08-13 : Initial Release
# v0.0.2 @ 2024-08-20 : Added report settings and utility functions.
# v0.0.9 @ 2024-10-20 : Updated documentation and added the HTML cleaning function.
#                     : Added function to clean the HTML code for reduced file size.
# --------------------------------------------------------------------------------------------

# --- TODO : ---------------------------------------------------------------------------------
# - 
# ============================================================================================

# --------------------------------------------------------------------------------------------
#                                  IMPORTED MODULES
# --------------------------------------------------------------------------------------------

# Import the core utilities and settings into the utils package.

from .report_settings import Reports_Settings
from .report_utils    import sanitize_filename, update_filename, get_current_datetime, get_clean_HTML_code

# ============================================================================================
#                                PACKAGE DESCRIPTION:
# ============================================================================================

"""
This package provides core utilities and settings management for HTML report generation.

Modules:
--------

1. report_settings.py:
    - Manages various settings for report generation, including file paths, folder paths, 
        and HTML report customization options.

2. report_utils.py:
    - Provides utility functions such as filename sanitization, generating the current date 
        and time, updating filenames, and cleaning HTML code to reduce file size.

Usage:
------

Example to use the report settings:
    from utils import Reports_Settings
    
    # Set the default report folder path
    Reports_Settings.set_default_report_path("C:\\Reports")

Example to use the utilities:
    from utils import sanitize_filename, update_filename, get_clean_HTML_code
    
    # Sanitize a filename
    clean_filename = sanitize_filename('invalid:file?name.html')
    
    # Update a filename with an incremented number
    updated_filename = update_filename('report_(0001)')

    # Clean HTML code
    cleaned_html = get_clean_HTML_code('<html>   <!-- comment --> <body>     <p>Text </p> </body> </html>')
"""

# ============================================================================================
