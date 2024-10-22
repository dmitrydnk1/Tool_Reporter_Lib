from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - space'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_space_element() -> ReportElement:
    """
    Creates and returns a ReportElement to add empty space to the report.

    Returns
    -------
    ReportElement
        A ReportElement object of type SPACE, containing an empty paragraph element.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.SPACE
    
    # Body content is a simple empty paragraph for spacing
    res.body_content = '''        
        <p></p>
    '''
    
    return res

# --------------------------------------------------------------------------------------------
