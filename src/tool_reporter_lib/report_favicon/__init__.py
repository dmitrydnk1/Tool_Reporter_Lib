"""
report_favicon
--------------

This module provides the functionality to retrieve a base64-encoded favicon for use in HTML reports.
The favicon can be read from an external file or, if the file is not found, a small fallback 1x1 transparent PNG will be used.

Version History:
- v0.0.2 @ 2024-08-13 : Initial Release

Modules:
--------
- fav_icon : Contains the function `_get_base64_favicon()` that retrieves the base64-encoded favicon.

"""

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report favicon'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================

# --- TODO: ----------------------------------------------------------------------------------
# Future improvements can be listed here.
# ============================================================================================

# Import the function to retrieve the base64 favicon.
from .fav_icon import _get_base64_favicon

# ============================================================================================