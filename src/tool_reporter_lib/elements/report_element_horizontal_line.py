from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - horizontal_line'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_horizontal_line_element() -> ReportElement:
    """
    Creates and returns a ReportElement representing a horizontal line.

    The horizontal line will take up the full width of the container.

    Returns
    -------
    ReportElement
        A ReportElement object of type HORIZONTAL_LINE, containing an HTML horizontal line.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.HORIZONTAL_LINE
    
    res.body_content = '''
        <div class="grid_12">
            <hr width="100%">
        </div>
    '''
    
    return res

# --------------------------------------------------------------------------------------------
