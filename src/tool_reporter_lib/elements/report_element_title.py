from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - title'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_title_element(  title      : str,
                        h_level    : int  = 1,
                        use_center : bool = False,
                            ) -> ReportElement: 
    """
    Creates a title element for a report.

    Parameters
    ----------
    title : str
        The text to be used as the title.
    h_level : int, optional
        The heading level (1 to 3), by default 1.
    use_center : bool, optional
        If True, centers the title, by default False.

    Returns
    -------
    ReportElement
        A ReportElement object with the title content.
    """

    # Create a new ReportElement of type TITLE
    res      = ReportElement()
    res.type = ReportElementTypes.TITLE

    # Ensure heading level is between 1 and 3
    h_level     = max(1, min(3, h_level))
    h_tag_title = f'<h{h_level}>{title}</h{h_level}>'

    # Generate body content based on the centering option
    if use_center:
        res.body_content = f'''
            <div class="grid_12">
                <div id="center">
                    <div align="center">
                        {h_tag_title}
                    </div>
                </div>        
            </div>
        '''
    else:
        res.body_content = f'''
            <div class="grid_12">
                {h_tag_title}
            </div>
        '''

    return res

# --------------------------------------------------------------------------------------------
