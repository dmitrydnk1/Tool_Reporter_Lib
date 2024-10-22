from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - text'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_text_element(text: str) -> ReportElement:
    """
    Creates a text element for a report.

    Parameters
    ----------
    text : str
        The text content for the report element.

    Returns
    -------
    ReportElement
        A ReportElement object containing the provided text.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.TEXT

    # Set body content with the text enclosed in a div and p tag with preserved white-space
    res.body_content = f'''
        <div class="grid_12">
            <div style="white-space: pre;">
                <p>{text}</p>
            </div>
        </div>
    '''
    
    return res

# --------------------------------------------------------------------------------------------
