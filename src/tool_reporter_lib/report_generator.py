# ============================================================================================
#                   Reporter - ReportHTML Class for generating HTML reports
# ============================================================================================

__version__:      str = '0.0.9'
__version_date__: str = '2024-10-20'
_name_:           str = 'Report HTML Generator'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.4 @ 2024-08-20 : Improved Annotations and Documentation
# v0.0.6 @ 2024-08-21 : Refactored Code, Updated Elements and Settings
# v0.0.9 @ 2024-10-20 : Enhanced Documentation, Added Code Improvements
# --------------------------------------------------------------------------------------------

# --- TODO : ---------------------------------------------------------------------------------
# - Check methods add_plot and add_chart for possible parametwers redundancy.
#                  Maybe no need to transfer plot objecct, 
#                  but call it directely from library to get the plot.
# --------------------------------------------------------------------------------------------

import os
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd

from typing import Optional

from .utils.report_settings import Reports_Settings
from .utils.report_utils import sanitize_filename, update_filename, get_current_datetime
from .report_favicon import _get_base64_favicon
from .elements import (
    ReportElement,     
    get_alert_box_element, 
    get_chart_element,
    get_code_element,
    get_footer_element,
    get_header_title,
    get_horizontal_line_element,
    get_param_value_table_element,
    get_param_value_table_element_v2,
    get_showhide_region_open_element,
    get_showhide_region_close_element,
    get_space_element,
    get_style_element,
    get_table_dataframe_element,
    get_text_element,
    get_text_console_element,
    get_title_element,      )
    
# --- CONSTANTS: -----------------------------------------------------------------------------

_DEFAULT_REPORT_TITLE: str = 'Report'

# --- JAVASCRIPT FUNCTIONS: ------------------------------------------------------------------

_TOGGLE_CONTENT_SCRIPT: str = """
function toggleContent(regionId, btn, regionName) {
    var content = document.getElementById(regionId);
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        btn.innerHTML = '▼ Hide ' + regionName;
    } else {
        content.style.display = "none";
        btn.innerHTML = '▶ Show ' + regionName;
    }
}
"""

# --- HTML ELEMENTS: -------------------------------------------------------------------------

_HIGHLIGHT_JS_CDN: str = '''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/styles/vs.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/highlight.min.js"></script>
<script>hljs.highlightAll();</script>
'''

# --------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------
#
#                                   REPORT HTML CLASS:
#
# ------------------------------------------------------------------------------------------------

class ReportHTML():
    """
    A class to generate HTML reports, including elements like titles, text, charts, and tables.

    Attributes
    ----------
    title : str
        The title of the report.
    sub_title : str
        The subtitle of the report.
    file_name : str
        The name of the report file (without extension).
    folder_path : str
        The directory path where the report will be saved.
    elements_list : list[ReportElement]
        List of elements that will be included in the report.
    bottom_elements_list : list[ReportElement]
        List of elements that will be added at the bottom of the report.
    use_open_saved_file : bool
        Whether to automatically open the saved HTML file after saving.
    use_title_background : bool
        Whether to use background image in the report title.

    Methods
    -------
    save():
        Saves the report to an HTML file. Updates the filename if it already exists.
    save_to_file():
        Saves the report to an HTML file. Updates the filename if it already exists.
    update_header_title(title = 'My Title', subtitle = 'My Sub Title', use_title_background = True):
        Updates the report's header title and subtitle.    
    add_horizontal_line():
        Adds a horizontal line to the report.
    add_space():
        Adds a space element to the report.
    add_title(title = 'My Title', h_level = 2, use_center = False):
        Adds a title element to the report.
    add_text(text = 'My Text'):
        Adds a text element to the report. Suppoer Multi-line text.
    add_text_console(text = 'My Console Text'):
        Adds text to the report in console style.
    add_chart(chart_plt, use_fullwidth = False, height = None, width = None):
        Adds a chart to the report.
    add_plot(plot_plt, use_fullwidth = False, height = None, width = None):
        Adds a plot to the report.
    add_dataframe_table(df, highlight_columns = [], round = -1, color_map_name = 'viridis', used_part_of_color = 0.8):
        Adds a dataframe table to the report.
    add_df_table(df, highlight_columns = [], round = -1):
        Adds a dataframe table to the report.
    add_param_value_table(pv_data, title = '', use_big_table = False):
        Adds a parameter-value table to the report.
    add_param_value_table_big(pv_data, title = '', use_big_table = True):
        Adds a parameter-value table with big style to the report.
    add_code(func, title = None):
        Adds code to the report.
    add_alert_box(text, alert_type = 'i', emoji = ''):
        Adds an alert box to the report.
    add_showhide_region_open(title, title_suffix = '', region_name = None):
        Adds a show/hide region open to the report.
    add_showhide_region_close():
        Adds a show/hide region close to the report.
    move_element_to_bottom():
        Moves the last added element to the bottom of the report.
    
    Example
    -------
    >>> from tool_reporter import ReportHTML
    >>> report = ReportHTML()
    >>> report.add_title('My Title', h_level = 2, use_center = True)
    >>> report.add_text('This is some text for the report.')
    >>> report.add_chart(plt, use_fullwidth = False, height = 400, width = 800)
    >>> report.add_dataframe_table(df, highlight_columns = ['A'], round = 2, color_map_name = 'coolwarm', used_part_of_color = 0.4)
    >>> report.save()    
    """

    _show_hide_region_id_counter: int = 0

    # --------------------------------------------------------------------------------------------
    @staticmethod
    def _get_show_hide_region_id() -> str:
        """
        Generates a unique ID for a show/hide region in the report.

        Returns
        -------
        str: The generated region ID.
        """
        ReportHTML._show_hide_region_id_counter += 1
        return f'show_hide_region_{ReportHTML._show_hide_region_id_counter}'

    # --------------------------------------------------------------------------------------------
    def __init__(   self,
                    title               : Optional[str]  = None,
                    sub_title           : Optional[str]  = None,
                    file_name           : Optional[str]  = None,
                    use_title_background: bool           = True,
                    open_saved_file     : Optional[bool] = None,
                        ) -> None:
        """
        Initializes a ReportHTML object.

        Parameters
        ----------
        title : str, optional
            The report title (default is `None`).            
                if `None` will be used default title, like `'Report'`.
        sub_title : str, optional
            The report subtitle (default is `None`).            
                if `None` will be used current date time.
                e.g. `'2024-08-13 12:34:56'`.
        file_name : str, optional
            The report filename (default is `None`).                
                if `None` will be generated from title.            
                if filename already exists, will be added a number to the end.            
                e.g. `'my_report'`, `'my_report_1'`, `'my_report_2'`, etc.
        use_title_background : bool, optional
            Use background image in the title (default is `True`).
        open_saved_file : bool, optional
            Automatically open the saved report file (default is `Reports_Settings.use_open_saved_file`).
        """
        self._USE_TRANSPARENT_PLOTS: bool = True

        self.folder_path: str = Reports_Settings._folder_path
        if Reports_Settings.custom_folder_path is not None:
            self.folder_path = Reports_Settings.custom_folder_path

        self.report_file_name     : str  = file_name or title or Reports_Settings._report_file_name
        self.file_format          : str  = Reports_Settings._file_format

        self.title                : str  = title or _DEFAULT_REPORT_TITLE
        self.sub_title            : str  = sub_title or get_current_datetime()
        self.use_custom_sub_title : bool = bool(sub_title)

        self._file_name           : str  = sanitize_filename(self.report_file_name)
        self._file_path           : str  = os.path.join(self.folder_path, f"{self._file_name}{self.file_format}")

        self.use_open_saved_file  : bool = open_saved_file if open_saved_file is not None else Reports_Settings.use_open_saved_file
        self.use_title_background : bool = use_title_background

        self.elements_list        : list[ReportElement] = []
        self.bottom_elements_list : list[ReportElement] = []

        self._initialize()

    # --------------------------------------------------------------------------------------------
    
    def __str__(self) -> str:
        """
        Returns a string representation of the report, including its attributes and elements.

        Returns
        -------
        str: The string representation of the report.
        """
        
        _lwidth: int = 25
        _line:   str = '-' * 40             
        res:     str = ''
        
        res += 'ReportHTML: \n'
        res += _line + '\n'
        res += f'+ {str("Folder Path").ljust(_lwidth)}: {self.folder_path} \n'
        res += f'+ {str("Report File Name").ljust(_lwidth)}: {self.report_file_name} \n'
        res += f'+ {str("File Name").ljust(_lwidth)}: {self._file_name} \n'
        res += f'+ {str("File Format").ljust(_lwidth)}: {self.file_format} \n'
        res += f'+ {str("Title").ljust(_lwidth)}: {self.title} \n'
        res += f'+ {str("File Path").ljust(_lwidth)}: {self._file_path} \n'
        res += f'+ {str("Use Open Saved File").ljust(_lwidth)}: {self.use_open_saved_file} \n'
        res += f'+ {str("Use Title Background").ljust(_lwidth)}: {self.use_title_background} \n'
        res += f'+ {str("Elements Count").ljust(_lwidth)}: {len(self.elements_list)} \n'
        
        for element in self.elements_list:
            res += f'\t + {element.type} \n'
            pass
                
        res += _line + '\n'
        
        return res

    # --------------------------------------------------------------------------------------------
    
    def __repr__(self) -> str:
        return self.__str__()

    # --------------------------------------------------------------------------------------------
    
    def _initialize(self) -> None:
        """
        Initializes the report by adding default elements like style and header title.
        """
        self.elements_list = []
        self.elements_list.append(get_style_element())

        element_header_title = get_header_title(
                                title                = self.title,
                                subtitle             = self.sub_title,
                                use_background_image = self.use_title_background, )
        
        self.elements_list.append(element_header_title)

    # --------------------------------------------------------------------------------------------
    
    def save_to_file(self)-> None:
        """
        Saves the report to an HTML file. Updates the filename if it already exists.
        """
        # Check if the folder exists:
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
            pass
        
        self._file_name = self.report_file_name
        self._file_name = sanitize_filename(self._file_name)
        # self._file_name = self._sanitize_filename(self._file_name)
        
        # Construct the full file path
        self._file_path = os.path.join(self.folder_path, self._file_name + self.file_format)        
        
        # if file exists, then update the filename, and save the file.        
        while os.path.exists(self._file_path):
            # self._file_name = self._update_filename(self._file_name)
            self._file_name = update_filename(self._file_name)
            self._file_path = os.path.join(self.folder_path, self._file_name + self.file_format)
            pass
        
        # UPDATING SUBTITLE FOR DEFAULT SETTINGS WITH FILENAME:        
        if self.use_custom_sub_title == False:
            self.sub_title = self.sub_title + f'<p><p>{self._file_name}'
            self.update_header_title(subtitle = self.sub_title)            
            pass
        
        html_content: str = self._get_html_str()
                
        # Save the HTML content to the file
        with open(self._file_path, 'w', encoding = "utf-8") as file:
            file.write(html_content)

        # Optionally open the file after saving
        if self.use_open_saved_file:
            webbrowser.open_new_tab(self._file_path)        
        
        pass
        
    # --------------------------------------------------------------------------------------------
    def save(self) -> None:
        """
        Saves the report to an HTML file.
        """
        self.save_to_file()

    # --------------------------------------------------------------------------------------------
    def update_header_title(self, 
                            title                : Optional[str]  = None,
                            subtitle             : Optional[str]  = None,
                            use_title_background : Optional[bool] = None,
                                ) -> None:
        """
        Updates the report's header title and subtitle.

        Parameters
        ----------
        title : str, optional
            The new title for the report.
        subtitle : str, optional
            The new subtitle for the report.
        use_title_background : bool, optional
            Whether to use background image for the title.
        
        Example
        -------
        >>> report.update_header_title( title                = 'My New Title', 
                                        subtitle             = 'My New Sub Title', 
                                        use_title_background = True, )
        """
        if title is not None:
            self.title = title
        
        if subtitle is not None:
            self.sub_title = subtitle
        
        if use_title_background is not None:
            self.use_title_background = use_title_background

        header_element = get_header_title(  title    = self.title, 
                                            subtitle = self.sub_title, 
                                            use_background_image = self.use_title_background)
        
        self.elements_list[1] = header_element

    # --------------------------------------------------------------------------------------------
    
    def add_horizontal_line(self) -> None:
        """
        Adds a horizontal line to the report.
        """
        self.elements_list.append(get_horizontal_line_element())

    # --------------------------------------------------------------------------------------------
    
    def add_space(self) -> None:
        """
        Adds a space element to the report.
        """
        self.elements_list.append(get_space_element())

    # --------------------------------------------------------------------------------------------
    
    def add_title(  self, 
                    title     : str,
                    h_level   : int  = 1,
                    use_center: bool = False,
                        ) -> None:
        """
        Adds a title to the report.

        Parameters
        ----------
        title : str
            The title text.
        h_level : int, optional
            The heading level, can be 1, 2, 3 (default is `1`).
        use_center : bool, optional
            Whether to center the title (default is `False`).

        Example
        -------
        >>> report.add_title(title = 'My Title', h_level = 2, use_center = True)
        """
        self.elements_list.append(get_title_element(title, 
                                                    h_level    = h_level, 
                                                    use_center = use_center))

    # --------------------------------------------------------------------------------------------
    
    def add_text(self, text: str) -> None:
        """
        Adds a text element to the report.

        Parameters
        ----------
        text : str
            The text content to add to the report.

        Example
        -------
        >>> report.add_text(text = 'My Text')
        >>> long_text : str = \''' My Long Text 
                            My Long Text not over yet.
                            My long tex is still going on. \'''
        >>> report.add_text(text = long_text)
        """
        self.elements_list.append(get_text_element(text))

    # --------------------------------------------------------------------------------------------
    
    def add_text_console(self, text: str) -> None:
        """
        Adds text to the report in console style.

        Parameters
        ----------
        text : str
            The text content to add in console style.

        Example
        -------
        >>> report.add_text_console(text = 'My console text')
        >>> long_text = '''My Long Text
                        My Long Text not over yet.
                        My long text is still going on.'''
        >>> report.add_text_console(text = long_text)
        """
        self.elements_list.append(get_text_console_element(text))

    # --------------------------------------------------------------------------------------------
    
    def add_chart(  self, 
                    chart_plt     : plt.Figure,
                    use_fullwidth : bool          = False,
                    height        : Optional[int] = None,
                    width         : Optional[int] = None,
                        ) -> None:
        """
        Adds a chart to the report.

        Parameters
        ----------
        chart_plt : matplotlib.pyplot.Figure
            The matplotlib chart to add.
        use_fullwidth : bool, optional
            Whether to use full width for the chart (default is `False`).            
                🔛 if `False`, reccommended plot `width` <= 1170 px.
        height : int, optional
            The height of the chart in pixels (default is `None`).
        width : int, optional
            The width of the chart in pixels (default is `None`).
            

        Example
        -------
        >>> plt.figure(figsize = (4, 11.7), dpi = 100, tight_layout = True)
        >>> plt.plot([1, 2, 3, 4])
        >>> plt.ylabel('Some numbers')
        >>> report.add_chart(chart_plt        = plt,
                                use_fullwidth = False,
                                heigth        = 400,
                                width         = 1170)
        """
        use_transparent_plots: bool = self._USE_TRANSPARENT_PLOTS
        
        self.elements_list.append(get_chart_element(chart_plt, 
                                                    use_fullwidth         = use_fullwidth, 
                                                    heigth                = height, 
                                                    width                 = width, 
                                                    use_transparent_plots = use_transparent_plots, ))

    # --------------------------------------------------------------------------------------------
    
    def add_plot(   self, 
                    plot_plt      : plt.Figure,
                    use_fullwidth : bool          = False,
                    height        : Optional[int] = None,
                    width         : Optional[int] = None,
                        ) -> None:
        """
        Adds a plot to the report.

        Parameters
        ----------
        plot_plt : matplotlib.pyplot.Figure
            The matplotlib plot to add.
        use_fullwidth : bool, optional
            Whether to use full width for the plot (default is `False`).            
                🔛 if `False`, reccommended plot `width` <= 1170 px.
        height : int, optional
            The height of the plot in pixels (default is `None`).
        width : int, optional
            The width of the plot in pixels (default is `None`).

        Example
        -------
        >>> import matplotlib.pyplot as plt
        >>> plt.figure(figsize = (4, 11.7), dpi = 100, tight_layout = True)
        >>> plt.plot([1, 2, 3, 4])
        >>> plt.ylabel('Some numbers')
        >>> report.add_plot(plot_plt      = plt, 
                            use_fullwidth = False,
                            height        = 400,
                            width         = 1170)        
        """
        self.add_chart(plot_plt, use_fullwidth, height, width)

    # --------------------------------------------------------------------------------------------
    
    def add_dataframe_table(self, 
                            df:                 pd.DataFrame, 
                            highlight_columns:  list[str] = [], 
                            round:              int       = -1, 
                            color_map_name:     str       = Reports_Settings.df_heatmap_colormap_name,
                            used_part_of_color: float     = Reports_Settings.df_heatmap_used_clr_pcnt,
                                ) -> None:
        """
        Adds a dataframe table to the report from a pandas DataFrame.

        Parameters
        ----------
        df : pd.DataFrame
            The pandas DataFrame to add as a table.
        highlight_columns : list of str, optional
            List of column names to highlight values in the table by heatmap (default is `[]`).
        round : int, optional
            Round the values in the table to the given number of digits after the decimal point (default is `-1`).
        color_map_name : str, optional
            Name of the color map to use for the heatmap (default is `Reports_Settings.df_heatmap_colormap_name`).
        used_part_of_color : float, optional
            Part of the color map to use for the heatmap, should be between 0.05 and 1.0 (default is `Reports_Settings.df_heatmap_used_clr_pcnt`).

        Example
        -------
        >>> import pandas as pd
        >>> df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
        >>> report.add_dataframe_table( df,
                                        highlight_columns  = ['A'],
                                        round              = 2,
                                        color_map_name     = 'coolwarm',
                                        used_part_of_color = 0.4)        
        """
        self.elements_list.append(get_table_dataframe_element(  df, 
                                                                highlight_columns, 
                                                                round, 
                                                                color_map_name,
                                                                used_part_of_color,
                                                                Reports_Settings.df_heatmap_nan_color,
                                                                Reports_Settings.df_min_col_amount_for_full_width))

    # --------------------------------------------------------------------------------------------    
    
    def add_df_table(   self, 
                        df               : pd.DataFrame,
                        highlight_columns: list[str] = [],
                        round            : int       = -1,
                            ) -> None:
        """
        Adds a dataframe table to the report from a pandas DataFrame.

        Parameters
        ----------
        df : pd.DataFrame
            The pandas DataFrame to add as a table.
        highlight_columns : list of str, optional
            List of columns to highlight values in the table by heatmap (default is `[]`).
        round : int, optional
            Round the values in the table to the given number of digits after the decimal point (default is `-1`).

        Example
        -------
        >>> import pandas as pd
        >>> df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
        >>> report.add_df_table(df,
                                highlight_columns = ['A'],
                                round             = 2)        
        """
        self.add_dataframe_table(df, highlight_columns, round)

    # --------------------------------------------------------------------------------------------
    
    def add_param_value_table(  self, 
                                pv_data      : dict[str, str] | list[tuple[str, str]],
                                title        : str  = '',
                                use_big_table: bool = False,
                                    ) -> None:
        """
        Adds a parameter-value table to the report.

        Parameters
        ----------
        pv_data : dict[str, str] | list[(str, str)]
            Dictionary or list of parameter names and values.
        title : str, optional
            Title of the parameter-value table (default is `''`).
        use_big_table : bool, optional
            Whether to use big table style (default is `False`).

        Example
        -------
        >>> pv_data: dict = {'Param1': 'Value1', 'Param2': 'Value2'}
        >>> report.add_param_value_table(   pv_data, 
                                            title         = 'My Param Value Table', 
                                            use_big_table = False, )        
        """
        if use_big_table:
            self.elements_list.append(get_param_value_table_element_v2(pv_data, title))
        else:
            self.elements_list.append(get_param_value_table_element(pv_data, 
                                                                    title, 
                                                                    Reports_Settings.param_value_table_truncate_length))

    # --------------------------------------------------------------------------------------------
    
    def add_param_value_table_big(  self, 
                                    pv_data:       dict[str, str] | list[tuple[str, str]], 
                                    title:         str  = '', 
                                    use_big_table: bool = True, 
                                            ) -> None:
        """
        Adds a parameter-value table with big style to the report.

        Parameters
        ----------
        pv_data : dict[str, str] | list[(str, str)]
            Dictionary or list of parameter names and values.
        title : str, optional
            Title of the parameter-value table (default is `''`).
        use_big_table : bool, optional
            Whether to use big table style (default is `True`).

        Example
        -------
        >>> pv_data: dict = {'Param1': 'Value1', 'Param2': 'Value2'}
        >>> report.add_param_value_table_big(   pv_data,
                                                title         = 'My Param Value Table', 
                                                use_big_table = True, )
        """
        self.add_param_value_table(pv_data, title, use_big_table)

    # --------------------------------------------------------------------------------------------
    
    def add_code(   self, 
                    func, 
                    title: Optional[str] = None, 
                        ) -> None:
        """
        Adds code to the report.

        Parameters
        ----------
        func : function
            The function whose code is to be added to the report.
        title : str, optional
            Title of the code block (default is `None`).

        Example
        -------
        >>> def my_func():
        ...     print('Hello World!')
        >>> report.add_code(my_func, title = 'My Code Block') 
        """
        import inspect        
        
        f_name = func.__name__
        f_code = inspect.getsource(func)
        
        if title is not None:
            self.add_title(title)            
        
        self.elements_list.append(get_code_element(f_code))

    # --------------------------------------------------------------------------------------------
    
    def add_alert_box(  self, 
                        text:       str, 
                        alert_type: str = 'i', 
                        emoji:      str = '', 
                            ) -> None:
        """
        Adds an alert box to the report.

        Parameters
        ----------
        text : str
            Text to display in the alert box.
        alert_type : str, optional
            Type of the alert box (default is `'i'`).
            - 'i' - info
            - 'w' - warning
            - 'n' - note
            - 'e' - error
        emoji : str, optional
            Emoji to display in the alert box (default is `''`).
            If None, no emoji will be displayed according to alert type.

        Example
        -------
        >>> report.add_alert_box(   text       = 'My Alert Box Text',
                                    alert_type = 'i',
                                    emoji      = '', )
        """
        self.elements_list.append(get_alert_box_element(text, alert_type, emoji))

    # --------------------------------------------------------------------------------------------
    
    def add_showhide_region_open(   self, 
                                    title       : str,
                                    title_suffix: str = '',
                                    region_name : Optional[str] = None,
                                        ) -> None:
        """
        Adds a show/hide region open to the report.

        ⚠️ WARNING: At the end of the region, you must add show/hide region close.

        Parameters
        ----------
        title : str
            Title of the region.
        title_suffix : str, optional
            Title suffix for the region (default is `''`).
            Final title will be: `title_suffix + title`.
        region_name : str, optional
            Name of the region (default is `None`).
            If None, the region name will be generated automatically.

        Example
        -------
        >>> report.add_showhide_region_open(title        = 'My Show Hide Region',
                                            title_suffix = '',
                                            region_name  = None)
        >>> report.add_text('My Text')
        >>> report.add_showhide_region_close()
        """
        if region_name is None:
            region_name = self._get_show_hide_region_id()
        
        title_upd: str = title_suffix + title
        
        self.elements_list.append(get_showhide_region_open_element(title_upd, region_name))

    # --------------------------------------------------------------------------------------------
    
    def add_showhide_region_close(self) -> None:
        """
        Adds a show/hide region close to the report.
        """
        self.elements_list.append(get_showhide_region_close_element())

    # --------------------------------------------------------------------------------------------
    
    def move_element_to_bottom(self) -> None:
        """
        Moves the last added element to the bottom of the report.

        Example
        -------
        >>> report.add_text('My Text')
        >>> report.move_element_to_bottom()
        """
        if len(self.elements_list) > 0:
            self.bottom_elements_list.append(self.elements_list.pop())
    
    # --------------------------------------------------------------------------------------------
    #                                         PRIVATE METHODS:
    # --------------------------------------------------------------------------------------------
    
    def _get_html_str(self) -> str:
        """
        Returns the html string for the report.
        """
        
        # adding bottom elements to the report:
        self._adding_bottom_elements_to_report()
        
        # Adding final element:
        self.elements_list.append(get_footer_element())        
        
        favicon_base64: str = _get_base64_favicon()
        
        res: str = '<!DOCTYPE html> \n'
        res     += '<html lang="en"> \n'
        res     += '<head> \n'
        res     += '<meta charset="UTF-8"> \n'
        res     += f'<link rel="icon" type="image/png" href="{favicon_base64}"/>'
        res     += f'''<title>
                    {self.title}                
                    </title> \n'''
                
        # Code Highlighting:
        res     += _HIGHLIGHT_JS_CDN                
        res     += '<style> \n'
        
        for element in self.elements_list:
            res += element.get_style_str()
            pass
        
        res += '</style> \n'        
        res += '</head> \n'
        res += '<body> \n'
        
        for element in self.elements_list:
            res += element.get_body_str()
            pass        

        res += f'''<script>{_TOGGLE_CONTENT_SCRIPT}</script>'''
        res += '</body> \n'
        res += '</html> \n'
        
        return res
    
    # --------------------------------------------------------------------------------------------

    def _adding_bottom_elements_to_report(self) -> None:
        """
        Adding bottom elements to the report.
        """
        while len(self.bottom_elements_list) > 0:
            self.elements_list.append(self.bottom_elements_list.pop(0))
            pass

        pass
    
    # --------------------------------------------------------------------------------------------