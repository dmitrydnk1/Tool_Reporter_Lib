from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - footer'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_footer_element() -> ReportElement:
    """
    Generates a ReportElement representing a footer element for the report.

    Returns
    -------
    ReportElement
        A ReportElement object of type FOOTER, containing HTML closing tags for the layout.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.FOOTER
    
    # Footer closing tags
    res.body_content = '''
        </div>
        </div>        
    '''
    
    return res

# --------------------------------------------------------------------------------------------
