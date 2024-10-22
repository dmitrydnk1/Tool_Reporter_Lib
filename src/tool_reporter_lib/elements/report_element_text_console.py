from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - text console'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_text_console_element(text: str) -> ReportElement:
    """
    Creates a text console element for a report, displaying text in a monospace font
    with preserved whitespace formatting.

    Parameters
    ----------
    text : str
        The console-style text content for the report element.

    Returns
    -------
    ReportElement
        A ReportElement object containing the text in console format.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.TEXT_CONSOLE

    # Set body content with the text styled as monospace and preserving whitespace
    res.body_content = f'''
        <div class="grid_12">
            <div style="font-family: monospace; white-space: pre;">
                <p>{text}</p>
            </div>
        </div>
    '''
    
    return res

# --------------------------------------------------------------------------------------------
