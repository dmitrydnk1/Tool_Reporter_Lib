import io
import base64
import matplotlib.pyplot as plt
from typing import Optional
from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'report element - chart'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================

# --- TODO : ---------------------------------------------------------------------------------
# - Check maybe not necessary transfer of plt object, just call it from matplotlib.pyplot
# --------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------

def get_chart_element(  
                        chart_plt            : plt.Figure,
                        use_fullwidth        : bool          = False,
                        heigth               : Optional[int] = None,
                        width                : Optional[int] = None,
                        use_transparent_plots: bool          = True,
                            ) -> ReportElement:
    """
    Creates and returns a ReportElement containing a chart image encoded in base64.

    Parameters
    ----------
    chart_plt : matplotlib.pyplot.Figure
        A Matplotlib plot object to be rendered into an image.
    use_fullwidth : bool, optional
        If True, the chart will use the full width of the report, by default False.
    height : int, optional
        The height of the chart image, by default None (auto).
    width : int, optional
        The width of the chart image, by default None (auto).
    use_transparent_plots : bool, optional
        If True, the background of the plot will be transparent, by default True.

    Returns
    -------
    ReportElement
        A ReportElement object of type CHART, containing an HTML image tag for the chart.
    """
        
    res      = ReportElement()
    res.type = ReportElementTypes.CHART
    
    # Transforming the chart to BASE64 image:
    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    chart_plt.savefig(buf, format = 'png', transparent = use_transparent_plots)
    buf.seek(0)

    # Encode the buffer to a base64 string
    base64_string = base64.b64encode(buf.read()).decode('utf-8')

    # Close the buffer
    buf.close()
    
    if heigth is None:
        heigth_str = '\"\"'        
    else:
        heigth_str = '\"' + str(int(heigth)) + '\"'
        pass
    
    if width is None:
        width_str = '\"\"'
    else:
        width_str = '\"' + str(int(width)) + '\"'
        pass
    
    if use_fullwidth == False:
        res.body_content = f'''
            <div class=\"grid_12\">
            <div class=\"graph\">
            <div style=\"align=center; float:center;\">            
            <img align=\"center\" src=\"data:image/png;base64,{base64_string}\" width={width_str} height={heigth_str} alt=\"\" class="graph-item" />            
            </div>
            </div>
            </div>
        '''
    else:
        res.body_content = f'''            
            <div class=\"graph\">
            <div style=\"align=center; float:center;\">            
            <img align=\"center\" src=\"data:image/png;base64,{base64_string}\" width={width_str} height={heigth_str} alt=\"\" class="graph-item" />            
            </div>
            </div>            
        '''
        pass
    
    return res

# --------------------------------------------------------------------------------------------