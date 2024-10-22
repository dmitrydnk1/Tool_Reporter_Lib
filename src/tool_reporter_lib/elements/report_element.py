from enum import Enum

# ============================================================================================
# Meta Information
__version__:      str = '0.0.2'
__version_date__: str = '2024-08-13'
_name_:           str = 'Report Element'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}' 

# Version History
# v0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================

# --------------------------------------------------------------------------------------------
#                         REPORT ELEMENT TYPES (ENUM):
# --------------------------------------------------------------------------------------------

class ReportElementTypes(Enum):
    """
    Enum for different types of report elements.

    Attributes
    ----------
    NONE : str
        Placeholder for no element.
    TITLE : str
        Title element.
    TEXT : str
        Text element.
    CHART : str
        Chart element.
    STYLE : str
        Style-related element.
    SPACE : str
        Space element for formatting.
    DFTABLE : str
        DataFrame table.
    OTHER : str
        Placeholder for other element types.
    FOOTER : str
        Footer element.
    CODE : str
        Code block.
    ALERT_BOX : str
        Alert box.
    TEXT_CONSOLE : str
        Console-style text.
    HEAD_TITLE_ON_BACKGROUND : str
        Title over a background element.
    HORIZONTAL_LINE : str
        Horizontal line for visual separation.
    PARAM_VALUE_TABLE : str
        Parameter-value table.
    PARAM_VALUE_TABLE_v2 : str
        Version 2 of the parameter-value table.
    PARAM_VALUE_GRID : str
        Parameter-value grid.
    SHOWHIDE_REGION_OPEN : str
        Start of a collapsible region.
    SHOWHIDE_REGION_CLOSE : str
        End of a collapsible region.
    IMAGE_JPEG : str
        JPEG image.
    IMAGE_PNG : str
        PNG image.
    """
    NONE:                       str = 'none'
    TITLE:                      str = 'title'
    TEXT:                       str = 'text'
    CHART:                      str = 'chart'
    STYLE:                      str = 'style'
    SPACE:                      str = 'space'
    DFTABLE:                    str = 'df_table'
    OTHER:                      str = 'other'
    FOOTER:                     str = 'footer'
    CODE:                       str = 'code'
    ALERT_BOX:                  str = 'alert_box'
    TEXT_CONSOLE:               str = 'text_console'
    HEAD_TITLE_ON_BACKGROUND:   str = 'Head_title_on_background'
    HORIZONTAL_LINE:            str = 'horizontal_line'
    PARAM_VALUE_TABLE:          str = 'param_value_table'
    PARAM_VALUE_TABLE_v2:       str = 'param_value_table_v2'
    PARAM_VALUE_GRID:           str = 'param_value_grid'
    SHOWHIDE_REGION_OPEN:       str = 'showhide_region_open'
    SHOWHIDE_REGION_CLOSE:      str = 'showhide_region_close'
    IMAGE_JPEG:                 str = 'image/jpeg'
    IMAGE_PNG:                  str = 'image/png'

# --------------------------------------------------------------------------------------------
#                         REPORT ELEMENT TYPES (FUNCTIONS):
# --------------------------------------------------------------------------------------------

def get_report_element_type_str(element_type: ReportElementTypes) -> str:
    """
    Get the string representation of the enum: ReportElementTypes.
    
    Parameters
    ----------
    element_type : ReportElementTypes
        The enum value of the report element.
    
    Returns
    -------
    str
        String representation of the report element type.
    """
    return element_type.value

# --------------------------------------------------------------------------------------------
#                                 REPORT ELEMENT:
# --------------------------------------------------------------------------------------------

class ReportElement:
    """
    Represents an element in the report, which can have different types (e.g., text, chart, image).

    Attributes
    ----------
    type : ReportElementTypes
        Type of the report element, default is NONE.
    body_content : str
        The body content of the element in string format.
    style_content : str
        The style content of the element in string format.
    
    Methods
    -------
    __str__() -> str
        Returns a human-readable description of the element type.
    __repr__() -> str
        Returns a developer-friendly representation of the element.
    get_style_str() -> str
        Returns the style string for the element.
    get_body_str() -> str
        Returns the body string for the element.
    """

    def __init__(self) -> None:
        """
        Initialize a new ReportElement with default type as NONE.
        """
        self.type: ReportElementTypes = ReportElementTypes.NONE        
        self.body_content:  str = ''
        self.style_content: str = ''

    def __str__(self) -> str:
        """
        String representation of the report element.

        Returns
        -------
        str
            A human-readable description of the element type.
        """
        return f'ReportElement: \t{self.type.value}'

    def __repr__(self) -> str:
        """
        Internal representation of the report element (for developers).

        Returns
        -------
        str
            String representation of the report element.
        """
        return self.__str__()

    def get_style_str(self) -> str:
        """
        Returns the style string for the element.

        Returns
        -------
        str
            The style content for the report element.
        """
        return self.style_content

    def get_body_str(self) -> str:
        """
        Returns the body string for the element.

        Returns
        -------
        str
            The body content for the report element.
        """
        return self.body_content

# ==================================================================================================
