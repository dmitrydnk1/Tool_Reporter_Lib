"""
Reporter - Report Elements
==========================

This module provides various report elements for generating HTML-based reports, 
such as charts, alert boxes, headers, footers, tables, and more. Each element is 
designed as a `ReportElement` object, which can be easily integrated into an HTML report.

Version: 0.0.2
Date: 2024-08-13
"""

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'Reporter - Report Elements'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY ------------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================

# --- TODO -----------------------------------------------------------------------------------
# Future Improvements:
# - Add support for additional chart types (e.g., 2D Heatmaps plots).
# - Add Chart Elemnts, to resize for optimal for report plot image, if restricted.
# - Add elements, for 2 Cloumns, with large side with Images, or content, 
#               while Smaller column with some list of parameters table.

# --------------------------------------------------------------------------------------------



# --- Report Element Base Classes ------------------------------------------------------------
from .report_element import ReportElement, ReportElementTypes


# ============================================================================================
#                                  REPORT ELEMENTS
# ============================================================================================
"""
List of available report element functions, each generating a different component of the report.
"""

from .report_element_alert_box         import get_alert_box_element
from .report_element_chart             import get_chart_element
from .report_element_code              import get_code_element
from .report_element_footer            import get_footer_element
from .report_element_header_title      import get_header_title
from .report_element_horizontal_line   import get_horizontal_line_element
from .report_element_param_val_table   import get_param_value_table_element, get_param_value_table_element_v2
from .report_element_showhide          import get_showhide_region_open_element, get_showhide_region_close_element
from .report_element_space             import get_space_element
from .report_element_style             import get_style_element
from .report_element_table_df          import get_table_dataframe_element
from .report_element_text              import get_text_element
from .report_element_text_console      import get_text_console_element
from .report_element_title             import get_title_element

# --------------------------------------------------------------------------------------------
"""
Usage:

Each of the above functions returns a `ReportElement` object, which can be used to generate
HTML content. For example, to add a chart to your report:

    from elements import get_chart_element
    import matplotlib.pyplot as plt

    # Create a Matplotlib figure
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])

    # Generate a report element for the chart
    chart_element = get_chart_element(fig)

    # Use this chart_element in your report structure
"""


# ============================================================================================
