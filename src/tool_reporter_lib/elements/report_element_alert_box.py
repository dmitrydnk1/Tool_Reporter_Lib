from .report_element import ReportElement, ReportElementTypes
from typing import Optional

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - alert_box'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================


# --- CONSTANTS: EMOJI -----------------------------------------------------------------------

INFO_EMOJI:    str = 'ℹ️'
WARNING_EMOJI: str = '⚠️'
NOTE_EMOJI:    str = ''
ERROR_EMOJI:   str = '❌'


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_alert_box_element(
                            text       : str,
                            alert_type : str = 'info',
                            emoji      : Optional[str] = None,                            
                                ) -> ReportElement:
    """
    Creates and returns a ReportElement containing an alert box with optional emoji.

    Parameters
    ----------
    text : str
        The alert message text to be displayed inside the alert box.
    alert_type : str, optional
        The type of alert ('info', 'warning', 'note', 'error'), by default 'info'.
    emoji : str, optional
        Custom emoji to use in the alert box. If None, a default emoji is selected based on the alert_type.

    Returns
    -------
    ReportElement
        A ReportElement object of type ALERT_BOX, containing an HTML alert box with the message and emoji.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.ALERT_BOX
    
    alert_type_res = _get_alert_type(alert_type)
    
    if emoji is None:
        emoji = _get_alert_box_emoji(alert_type_res)
    
    # Body content for the alert box
    res.body_content = f'''
        <div class="grid_12">
            <div class="alert-box {alert_type_res}-box">
                <span class="emoji">{emoji}</span>
                <span class="text">{text}</span>
            </div>
        </div>
    '''
    
    return res


# --------------------------------------------------------------------------------------------
#                                 SUPPORTING FUNCTIONS:
# --------------------------------------------------------------------------------------------

def _get_alert_type(alert_type: str) -> str:
    """
    Returns the standardized alert type based on input string.
    
    Parameters
    ----------
    alert_type : str
        The input alert type string (can be shorthand or full).

    Returns
    -------
    str
        The standardized alert type ('info', 'warning', 'note', 'error').
    """
    if alert_type in ['i', 'info']:
        return 'info'
    if alert_type in ['w', 'warning']:
        return 'warning'
    if alert_type in ['n', 'note']:
        return 'note'
    if alert_type in ['e', 'error']:
        return 'error'
    
    return 'info'

# --------------------------------------------------------------------------------------------

def _get_alert_box_emoji(alert_type: str) -> str:
    """
    Returns the default emoji corresponding to the alert type.
    
    Parameters
    ----------
    alert_type : str
        The alert type ('info', 'warning', 'note', 'error').

    Returns
    -------
    str
        The emoji corresponding to the alert type.
    """
    if alert_type == 'info':
        return INFO_EMOJI
    if alert_type == 'warning':
        return WARNING_EMOJI
    if alert_type == 'note':
        return NOTE_EMOJI
    if alert_type == 'error':
        return ERROR_EMOJI

    return INFO_EMOJI

# --------------------------------------------------------------------------------------------
