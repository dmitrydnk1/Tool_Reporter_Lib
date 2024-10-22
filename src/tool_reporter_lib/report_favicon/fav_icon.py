import os

# ============================================================================================

__version__:      str = "0.0.2"
__version_date__: str = "2024-08-13"
_name_:           str = "report favicon"
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: --------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release

# --- CONSTANTS: --------------------------------------------------------------------
# The file is assumed to be in the same folder as this Python file.
FAVICON_BASE64_PATH     = os.path.join(os.path.dirname(__file__), 'fav_icon_base64.txt')
# Fallback favicon: a 1x1 transparent PNG base64 string, which is very small and won't cause errors
FALLBACK_FAVICON_BASE64 = (
    'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wcA'
    'AwAB/By8kUAAAAAASUVORK5CYII=')  

# ============================================================================================

def _get_base64_favicon() -> str:
    """
    Loads the base64 favicon string from the external file located in the same folder as this Python file.
    If the file is not found, returns the fallback base64 favicon string (1x1 transparent PNG).

    Returns
    -------
    str
        The base64-encoded favicon string or fallback favicon string (1x1 transparent PNG).
    """
    try:
        with open(FAVICON_BASE64_PATH, 'r') as file:
            favicon_base64 = file.read().strip()
        return favicon_base64
    except FileNotFoundError:
        return FALLBACK_FAVICON_BASE64

# ============================================================================================
