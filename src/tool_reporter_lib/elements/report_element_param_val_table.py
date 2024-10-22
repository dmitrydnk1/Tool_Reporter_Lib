from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - param value table'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_param_value_table_element(param_value_table: dict[str, str] | list[tuple[str, str]], 
                                  title            : str = '',
                                  cfg_truncate_len : int = 60,
                                    ) -> ReportElement:
    """
    Creates a ReportElement containing a parameter-value table in div format.

    Parameters
    ----------
    param_value_table : dict[str, str] | list[(str, str)]
        The parameter-value pairs to display in the table.
    title : str, optional
        The title to display above the table, by default ''.
    cfg_truncate_len : int, optional
        The maximum length of the value before truncation, by default 60.

    Returns
    -------
    ReportElement
        A ReportElement object containing the parameter-value table.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.PARAM_VALUE_TABLE
    
    res.body_content = '<div class="grid_12">'
    
    if title:
        res.body_content += f'<h2>{title}</h2>'
    
    res.body_content += '<div class="param-value-element">'
    
    param_val_list = list(param_value_table.items()) if isinstance(param_value_table, dict) else param_value_table
    param_val_list.reverse()  # Reverse the order
    
    for param, val in param_val_list:
        val = str(val)
        
        if len(val) > cfg_truncate_len:
            val = _short_str(val, max_length=cfg_truncate_len)
        
        param_text_class: str = 'param-value-text'
        
        if len(val) > cfg_truncate_len // 2:
            param_text_class += ' param-value-text-long'
        
        res.body_content += f'''
            <div class="param-value-item">
                <div class="param-value-caption">{param}</div>
                <div class="{param_text_class}">{val}</div>
            </div>
        '''
    
    res.body_content += '</div></div>'
    
    return res

# --------------------------------------------------------------------------------------------

def get_param_value_table_element_v2(param_value_table: dict[str, str] | list[tuple[str, str]], 
                                     title            : str = '', 
                                        ) -> ReportElement:
    """
    Creates a ReportElement containing a parameter-value table in table format.

    Parameters
    ----------
    param_value_table : dict[str, str] | list[(str, str)]
        The parameter-value pairs to display in the table.
    title : str, optional
        The title to display above the table, by default ''.

    Returns
    -------
    ReportElement
        A ReportElement object containing the parameter-value table in table format.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.PARAM_VALUE_TABLE_v2
    
    res.body_content = '<div class="grid_12">'
    
    if title:
        res.body_content += f'<h2>{title}</h2>'
    
    param_val_list = list(param_value_table.items()) if isinstance(param_value_table, dict) else param_value_table.copy()
    param_val_list.reverse()
    
    # Start the table with the class 'param-val-style-table' applied
    res.body_content += '<table class="param-val-style-table">'
    
    # Add table head
    res.body_content += '''
        <thead>
            <tr>
                <th>Parameter Name</th>
                <th>Value</th>
            </tr>
        </thead>
        <tbody>
    '''
    
    for param, val in param_val_list:
        val = _short_str(val)  # Truncate or process the string value
        res.body_content += f'''
            <tr>
                <td>{param}</td>
                <td>{val}</td>
            </tr>
        '''
    
    res.body_content += '</tbody></table></div>'
    
    return res

# --------------------------------------------------------------------------------------------
#                                 SUPPORTING FUNCTIONS:
# --------------------------------------------------------------------------------------------

def _short_str(val, max_length: int = 60) -> str:
    """
    Truncates or formats the given value to a shorter form.

    Parameters
    ----------
    val : any
        The value to be shortened or truncated.
    max_length : int, optional
        The maximum length of the string, by default 60.

    Returns
    -------
    str
        The truncated or formatted string.
    """
    
    if isinstance(val, float):
        return _short_float(val)
    
    if isinstance(val, list):
        return _short_repr(val)
    
    return _truncate_long_string(str(val), max_length=max_length)

# --------------------------------------------------------------------------------------------

def _short_repr(arr: list, n: int = 2) -> str:
    """
    Shortens a list to a limited number of elements, showing first `n` and last element.

    Parameters
    ----------
    arr : list
        The list to be shortened.
    n : int, optional
        The number of initial elements to display, by default 2.

    Returns
    -------
    str
        The shortened string representation of the list.
    """
    
    if len(arr) > n + 1:
        return str(arr[:n])[:-1] + ', .., ' + str(arr[-1]) + ']'
    
    return str(arr)

# --------------------------------------------------------------------------------------------

def _short_float(val: float, n: int = 4) -> str:
    """
    Rounds a float value to a given precision.

    Parameters
    ----------
    val : float
        The float value to be rounded.
    n : int, optional
        The number of decimal places to round to, by default 4.

    Returns
    -------
    str
        The rounded float as a string.
    """
    return str(round(val, n))

# --------------------------------------------------------------------------------------------

def _truncate_long_string(string: str, max_length: int = 60) -> str:
    """
    Truncates a string to the given max_length.

    Parameters
    ----------
    string : str
        The string to be truncated.
    max_length : int, optional
        The maximum length of the string, by default 60.

    Returns
    -------
    str
        The truncated string with ellipsis if longer than max_length.
    """
    
    if len(string) <= max_length:
        return string
    
    return string[:max_length] + '...'

# --------------------------------------------------------------------------------------------
