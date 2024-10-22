import pandas as pd
from .report_element import ReportElement, ReportElementTypes
from .value_to_color import value_to_color

# ============================================================================================
# Meta Information
__version__:      str = '0.0.7'
__version_date__: str = '2024-09-18'
_name_:           str = 'report element - table dataframe'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.7 @ 2024-09-18 : Updated heatmap spectrum color use,
#                       for better visibility with heatmap_used_clr_pcnt = 0.6
# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_table_dataframe_element(    df: pd.DataFrame, 
                                    highlight_columns = [],
                                    round                 : int   = -1,
                                    heatmap_colormap_name : str   = 'coolwarm',
                                    heatmap_used_clr_pcnt : float = 0.6,
                                    heatmap_nan_color     : str   = '#ff0000',
                                    df_min_col_amount_for_full_width: int  = 8,
                                        ) -> ReportElement:
    """
    Generates a ReportElement containing an HTML table based on a DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to display in the report.
    highlight_columns : list[str], optional
        Columns to apply a heatmap style, by default an empty list.
    round : int, optional
        Number of decimal places to round the values, by default -1 (no rounding).
    heatmap_colormap_name : str, optional
        Name of the colormap for heatmap highlighting, by default 'coolwarm'.
    heatmap_used_clr_pcnt : float, optional
        Percentage of the colormap spectrum to use for heatmap, by default 0.6.
    heatmap_nan_color : str, optional
        Color for NaN values in the heatmap, by default '#ff0000'.
    df_min_col_amount_for_full_width : int, optional
        Minimum number of columns required for full-width table layout, by default 8.
    
    Returns
    -------
    ReportElement
        A ReportElement object containing the DataFrame as an HTML table.
    """
    
    res      = ReportElement()
    res.type = ReportElementTypes.DFTABLE
    
    # Adding Scroller:    
    # get columns amount:
    columns_amount = len(df.iloc[0].values)
    
    if columns_amount < df_min_col_amount_for_full_width:
        res.body_content += '<div class=\"grid_12\">'
    
    res.body_content += '<div class=\"table-scroll-wrapper\">'
    
    # Calculate min and max values for highlighted columns
    min_max_values = {col: (df[col].min(), df[col].max()) for col in highlight_columns if col in df.columns}

    if round >= 0:
        df = df.copy()
        df = df.round(round)
        pass
    
    # Apply the styling using pandas Styler
    styler = df.style.apply(_style_dataframe, 
                            highlight_columns     = highlight_columns, 
                            min_max_values        = min_max_values, 
                            axis                  = None, 
                            heatmap_colormap_name = heatmap_colormap_name,
                            heatmap_nan_color     = heatmap_nan_color,
                            heatmap_used_clr_pcnt = heatmap_used_clr_pcnt, )
    
    # Float Rounding Formating:
    if round >= 0:
        # Set the float format for HTML display
        format_temp = '{:.' + str(round) + 'f}'        
        
        styler = styler.format( format_temp, 
                                na_rep = "-", 
                                subset = pd.IndexSlice[:, df.select_dtypes(include = ['float64', 'float32']).columns])
    
    # Set the class for the table
    styler.set_table_attributes('class="minimalistic-style-table"')
    
    # Convert to HTML
    html_table = styler.to_html(escape = False, border = 0)

    
    res.body_content += html_table
    
    if columns_amount < df_min_col_amount_for_full_width:
        res.body_content += '</div>'
    
    res.body_content += '</div>'
    
    return res

# --------------------------------------------------------------------------------------------
#                              STYLING FUNCTION:
# --------------------------------------------------------------------------------------------

def _style_dataframe(   
                        df                    : pd.DataFrame,
                        highlight_columns     : list[str],
                        min_max_values, 
                        heatmap_colormap_name : str   = 'coolwarm',
                        heatmap_nan_color     : str   = '#ff0000',
                        heatmap_used_clr_pcnt : float = 0.6,
                            ) -> pd.DataFrame:
    """
    Styles a DataFrame for highlighting columns with heatmap colors.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to style.
    highlight_columns : list[str]
        The columns to apply the heatmap to.
    min_max_values : dict
        A dictionary mapping columns to their min and max values for heatmap scaling.
    heatmap_colormap_name : str, optional
        Name of the colormap for heatmap, by default 'coolwarm'.
    heatmap_nan_color : str, optional
        Color to apply to NaN values, by default '#ff0000'.
    heatmap_used_clr_pcnt : float, optional
        Percentage of the colormap spectrum to use for the heatmap, by default 0.6.

    Returns
    -------
    pd.DataFrame
        The DataFrame with styles applied for HTML rendering.
    """
    
    styles = pd.DataFrame(  '', 
                            index   = df.index, 
                            columns = df.columns)
    
    for col in highlight_columns:
        
        if col in df.columns:
            # Check if min >= max then skip:
            if min_max_values[col][0] >= min_max_values[col][1]:
                continue
            
            color: str = df[col].apply(value_to_color, args = ( min_max_values[col][0], 
                                                                min_max_values[col][1], 
                                                                heatmap_colormap_name,
                                                                heatmap_nan_color, 
                                                                heatmap_used_clr_pcnt,))
            
            styles[col] = 'background-color: ' + color
            pass
        pass
    
    return styles

# --------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------
#                                  TESTING FUNCTION:
# --------------------------------------------------------------------------------------------

def test_get_table_dataframe_element():
    """
    Test the get_table_dataframe_element function with a sample DataFrame.
    """
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2.5, 3.5, 4.5, 5.5, 6.5]
    }
    
    df = pd.DataFrame(data)
    
    # Highlight column 'C' with heatmap
    report_element = get_table_dataframe_element(df, highlight_columns = ['C'], round = 1)
    
    # Check if the resulting object is of type ReportElement
    assert isinstance(report_element, ReportElement), "Output is not a ReportElement."
    
    # Check if the type is correctly set
    assert report_element.type == ReportElementTypes.DFTABLE, "Element type is not set to DFTABLE."
    
    # Check if the body content contains the DataFrame HTML
    assert "<table" in report_element.body_content, "HTML table not found in body content."
    
    # Print results for manual inspection
    print("Test Passed!")
    print(report_element.body_content)

# Run the test
if __name__ == "__main__":
    test_get_table_dataframe_element()

# --------------------------------------------------------------------------------------------