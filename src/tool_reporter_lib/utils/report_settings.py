# ============================================================================================
#                                  Reporter - Reporter Settings
# ============================================================================================

__version__:      str = '0.0.6'
__version_date__: str = '2024-08-21'
_name_:           str = 'Reporter - Reporter Settings'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.4 @ 2024-08-20 : Added annotations and improved documentation.
# v0.0.6 @ 2024-08-21 : Updated heatmap settings and introduced header title background options.
# --------------------------------------------------------------------------------------------

# --- TODO : ---------------------------------------------------------------------------------
# - Add functionality for default color schemes in tables and plots.
# - Handle various plot sizes and dynamic headers more efficiently.
# ============================================================================================

import keyring
from typing import Optional

# ============================================================================================
#                                REPORT SETTINGS CLASS
# ============================================================================================

class Reports_Settings:
    """
    Manages the report settings such as file paths, folder paths, visualization options, 
    and report metadata. Provides options for setting default folder paths, file names, 
    and visualization-related configurations.
    
    Attributes
    ----------
    _folder_path : str
        The folder path where reports will be saved.
    _report_file_name : str
        The name of the report file.
    _file_format : str
        The file format for the reports, default is '.html'.
    custom_folder_path : Optional[str]
        A custom folder path for saving reports, if set.
    param_value_table_truncate_length : int
        Length to truncate values in parameter-value tables.
    df_heatmap_nan_color : str
        Default color for NaN values in heatmaps.
    df_heatmap_colormap_name : str
        The colormap name used in heatmaps.
    df_heatmap_used_clr_pcnt : float
        Percentage of the colormap to be used in heatmaps.
    df_min_col_amount_for_full_width : int
        Minimum column amount required for full-width tables.
    use_open_saved_file : bool
        Boolean flag to determine if the report file should be automatically opened after being saved.
    use_header_title_on_background : bool
        Boolean flag to determine if the header title should be displayed on a background.

    Static Methods
    --------------
    set_default_report_path(folder_path: str) -> None
        Set the default folder path for saving reports.
    get_default_report_path() -> str
        Retrieve the default report folder path from the system keyring.
    activate_default_report_path() -> None
        Activate and set the default folder path for reports from the system keyring.
    reset_default_report_path() -> None
        Reset the default report folder path by removing it from the system keyring.
    set_folder_path(folder_path: str) -> None
        Set a custom folder path for saving reports.
    set_file_name(file_name: str) -> None
        Set the file name for reports.
    disable_open_saved_file() -> None
        Disable the automatic opening of saved report files.
    enable_open_saved_file() -> None
        Enable the automatic opening of saved report files.
    disable_header_title_on_background() -> None
        Disable the use of a background for the report header title.
    enable_header_title_on_background() -> None
        Enable the use of a background for the report header title.
    info() -> None
        Print the current configuration of report settings.
    """
    
    # Default report settings
    _folder_path      : str = 'Reports\\'
    _report_file_name : str = 'report'
    _file_format      : str = '.html'

    # Keyring service details for storing report folder path
    __SERVICE_NAME      : str = 'info_tool_lib'
    __REPORTS_FOLDER_KEY: str = 'reports_folder_keyring'

    # Visualization configurations
    custom_folder_path               : Optional[str] = None
    param_value_table_truncate_length: int           = 60
    df_heatmap_nan_color             : str           = '#ff0000'
    df_heatmap_colormap_name         : str           = 'coolwarm'
    df_heatmap_used_clr_pcnt         : float         = 0.6
    df_min_col_amount_for_full_width : int           = 8

    # Boolean settings for report behavior
    use_open_saved_file           : bool = True
    use_header_title_on_background: bool = True

    # --------------------------------------------------------------------------------------------
    #                                PATH SETTING METHODS
    # --------------------------------------------------------------------------------------------

    @staticmethod
    def set_default_report_path(folder_path: str) -> None:
        """
        Set the default folder path for saving reports. This path is stored using `keyring`.
        
        Parameters
        ----------
        folder_path : str
            The folder path to be set as the default report saving path.
        """
        if not folder_path.endswith('\\'):
            folder_path += '\\'
        Reports_Settings._folder_path = folder_path
        keyring.set_password(Reports_Settings.__SERVICE_NAME, Reports_Settings.__REPORTS_FOLDER_KEY, folder_path)

    # --------------------------------------------------------------------------------------------

    @staticmethod
    def get_default_report_path() -> str:
        """
        Get the default folder path for saving reports, retrieved from the system keyring.
        
        Returns
        -------
        str
            The default folder path, or an empty string if not set.
        """
        folder_path = keyring.get_password(Reports_Settings.__SERVICE_NAME, Reports_Settings.__REPORTS_FOLDER_KEY)
        return folder_path if folder_path is not None else ''

    # --------------------------------------------------------------------------------------------

    @staticmethod
    def activate_default_report_path() -> None:
        """
        Activate the default folder path by setting it from the value stored in the system keyring.
        """
        try:
            new_path = Reports_Settings.get_default_report_path()
            if new_path:
                Reports_Settings._folder_path = new_path
        except Exception as e:
            print(f"Error activating default report path: {e}")

    # --------------------------------------------------------------------------------------------

    @staticmethod
    def reset_default_report_path() -> None:
        """
        Reset the default folder path by removing it from the system keyring.
        """
        keyring.delete_password(Reports_Settings.__SERVICE_NAME, Reports_Settings.__REPORTS_FOLDER_KEY)

    # --------------------------------------------------------------------------------------------

    @staticmethod
    def set_folder_path(folder_path: str) -> None:
        """
        Set a custom folder path for saving reports.
        
        Parameters
        ----------
        folder_path : str
            The folder path to be used for saving reports.
        """
        Reports_Settings._folder_path = folder_path

    # --------------------------------------------------------------------------------------------

    @staticmethod
    def set_file_name(file_name: str) -> None:
        """
        Set the report file name.
        
        Parameters
        ----------
        file_name : str
            The name of the report file.
        """
        Reports_Settings._report_file_name = file_name

    # --------------------------------------------------------------------------------------------
    #                               OPEN FILE SETTINGS
    # --------------------------------------------------------------------------------------------

    @staticmethod
    def disable_open_saved_file() -> None:
        """
        Disable automatically opening the saved report file after generation.
        """
        Reports_Settings.use_open_saved_file = False

    # --------------------------------------------------------------------------------------------

    @staticmethod
    def enable_open_saved_file() -> None:
        """
        Enable automatically opening the saved report file after generation.
        """
        Reports_Settings.use_open_saved_file = True

    # --------------------------------------------------------------------------------------------
    #                         HEADER TITLE BACKGROUND SETTINGS
    # --------------------------------------------------------------------------------------------

    @staticmethod
    def disable_header_title_on_background() -> None:
        """
        Disable the header title background.
        """
        Reports_Settings.use_header_title_on_background = False

    # --------------------------------------------------------------------------------------------

    @staticmethod
    def enable_header_title_on_background() -> None:
        """
        Enable the header title background.
        """
        Reports_Settings.use_header_title_on_background = True

    # --------------------------------------------------------------------------------------------
    #                                   REPORT INFO METHOD
    # --------------------------------------------------------------------------------------------

    @staticmethod
    def info() -> None:
        """
        Print the current configuration of the `Reports_Settings`.
        """
        print('Reports Settings: \n')
        print(f'-------------------')
        print(f'+ Folder Path:         {Reports_Settings._folder_path}')
        print(f'+ Custom Folder Path:  {Reports_Settings.custom_folder_path}')
        print(f'+ File Name:           {Reports_Settings._report_file_name}')
        print(f'+ File Format:         {Reports_Settings._file_format}')
        print(f'+ Use Open Saved File: {Reports_Settings.use_open_saved_file}')
        print(f'+ Use Header Title:    {Reports_Settings.use_header_title_on_background}')

# ============================================================================================
