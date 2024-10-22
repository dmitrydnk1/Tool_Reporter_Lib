from .report_element import ReportElement, ReportElementTypes
from .report_style import get_css_content

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - style'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_style_element() -> ReportElement:
    """
    Creates and returns a ReportElement containing the CSS styles for the report.

    This function loads the CSS content using `get_css_content()` from the `report_style` module,
    which retrieves and cleans the CSS content from the external CSS file.

    Returns
    -------
    ReportElement
        A ReportElement object of type STYLE, containing the cleaned CSS styles.
    
    Raises
    ------
    FileNotFoundError
        If the CSS file cannot be found.
    """
    res      = ReportElement()
    res.type = ReportElementTypes.STYLE
    
    # Load the CSS content from the file using the get_css_content function
    res.style_content = get_css_content()

    return res

# --------------------------------------------------------------------------------------------
