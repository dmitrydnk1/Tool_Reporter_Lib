from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - show/hide region'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================

# --- TODO : ---------------------------------------------------------------------------------
# TODO: `use_hide` functionality is not implemented yet, needs fixing.
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_showhide_region_open_element(
                                    title      : str,
                                    region_name: str,
                                    use_hide   : bool = True,  # NOT WORKING YET
                                        ) -> ReportElement:
    """
    Creates and returns an opening section for a show/hide region in the report.

    Parameters
    ----------
    title : str
        The title to display on the toggle button.
    region_name : str
        The name (ID) of the region to show/hide.
    use_hide : bool, optional
        Determines if the region starts hidden, by default True (not working yet).

    Returns
    -------
    ReportElement
        A ReportElement object of type SHOWHIDE_REGION_OPEN, containing the HTML for the toggle button and start of the region.
    """
    
    res = ReportElement()
    res.type = ReportElementTypes.SHOWHIDE_REGION_OPEN

    # TODO: Fix `use_hide` functionality
    res.body_content = f'''
        <button class="toggle-button" onclick="toggleContent('{region_name}', this, '{title}')">▶ Show {title}</button>        
        <div class="content_show_hide" id="{region_name}">
        '''

    return res

# --------------------------------------------------------------------------------------------

def get_showhide_region_close_element() -> ReportElement:
    """
    Creates and returns a closing section for a show/hide region in the report.

    Returns
    -------
    ReportElement
        A ReportElement object of type SHOWHIDE_REGION_CLOSE, containing the closing HTML for the region.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.SHOWHIDE_REGION_CLOSE

    res.body_content = '''
        </div>
        '''
    
    return res

# --------------------------------------------------------------------------------------------
