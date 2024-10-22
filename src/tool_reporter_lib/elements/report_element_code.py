from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - code'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_code_element(code: str) -> ReportElement:
    """
    Creates and returns a ReportElement for displaying code in a formatted block.

    Parameters
    ----------
    code : str
        The code to display inside the report.

    Returns
    -------
    ReportElement
        A ReportElement object of type CODE, containing HTML for a code block.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.CODE
    
    # Creating HTML structure for displaying code in a preformatted block
    res.body_content = f'''<div class="grid_12">
            <pre><code class="python">{code}</code></pre>
        </div>'''
    
    return res

# --------------------------------------------------------------------------------------------
