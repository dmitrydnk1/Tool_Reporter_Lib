import random
import os
import re
from .report_element import ReportElement, ReportElementTypes

# ============================================================================================
# Meta Information
__version__:      str = '0.0.6'
__version_date__: str = '2024-08-21'
_name_:           str = 'Report Element - header title'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.6 @ 2024-08-21 : Updated header background images to random dynamic generated background.
# ============================================================================================


# --- FILE LOCATIONS (CONSTANTS): ------------------------------------------------------------

# Defining the paths for CSS and HTML files dynamically based on the current file location.

CURRENT_DIR    = os.path.dirname(__file__)  # Directory of the current script

CSS_FILE_PATH  = os.path.join(CURRENT_DIR, 'report_element_header_title_style.css')  # CSS file path
HTML_FILE_PATH = os.path.join(CURRENT_DIR, 'report_element_header_title_body.html')  # HTML file path

# ============================================================================================


# --------------------------------------------------------------------------------------------
#                                  REPORT ELEMENTS:
# --------------------------------------------------------------------------------------------


def get_header_title(
            title               : str,
            subtitle            : str = "",
            use_background_image: bool = True
                ) -> ReportElement:
    """
    Generates a ReportElement containing a header title with an optional animated background.

    Parameters
    ----------
    title : str
        The main title to display.
    subtitle : str, optional
        The subtitle to display, by default `''`.
    use_background_image : bool, optional
        Determines if the header should have a random animated background, by default `True`.

    Returns
    -------
    ReportElement
        A ReportElement object containing the header title, with or without an animated background.
    """

    if not use_background_image:
        return _get_header_title_simple(title, subtitle)

    res      = ReportElement()
    res.type = ReportElementTypes.HEAD_TITLE_ON_BACKGROUND

    # Generate random parameters for CSS
    params = {
        'color1'       : _generate_random_color(),
        'color2'       : _generate_random_color(),
        'color3'       : _generate_random_color(),
        'color4'       : _generate_random_color(),
        'shape_a_size' : _generate_random_size(),
        'shape_b_size' : _generate_random_size(),
        'shape_c_size' : _generate_random_size(),
        'shape_a_top'  : _generate_random_position(),
        'shape_a_left' : _generate_random_position(),
        'shape_b_top'  : _generate_random_position(),
        'shape_b_left' : _generate_random_position(),
        'shape_c_top'  : _generate_random_position(),
        'shape_c_left' : _generate_random_position(),
        'title'        : title,
        'subtitle_html': f'<h2 class="subtitle">{subtitle}</h2>' if subtitle else ''
        }

    # Load and format CSS
    res.style_content = _load_and_format_file(CSS_FILE_PATH, params)

    # Load and format body content
    res.body_content  = _load_and_format_file(HTML_FILE_PATH, params)
    
    # Clean CSS and HTML files
    res.style_content = clean_css_content(res.style_content)
    res.body_content  = clean_css_content(res.body_content)    

    return res


# --------------------------------------------------------------------------------------------
#
#                SUPPORTING FUNCTIONS:
#
# --------------------------------------------------------------------------------------------

def _generate_random_color() -> str:
    """Generates a random hex color code."""
    return f'#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}'

# --------------------------------------------------------------------------------------------

def _generate_random_size(min_size: int = 50, max_size: int = 200) -> int:
    """Generates a random size for the background shapes."""
    return random.randint(min_size, max_size)

# --------------------------------------------------------------------------------------------

def _generate_random_position() -> int:
    """Generates a random position percentage (0-90) for the background shapes."""
    return random.randint(0, 90)

# --------------------------------------------------------------------------------------------

def _load_and_format_file(  filename: str, 
                            params  : dict, 
                                ) -> str:
    """Loads a file and replaces placeholders with actual values from params."""
    with open(filename, 'r') as file:
        content = file.read()
    
    for key, value in params.items():
        content = content.replace(f'{{{{{key}}}}}', str(value))
    
    return content

# --------------------------------------------------------------------------------------------

def _get_header_title_simple(   title   : str, 
                                subtitle: str = '',
                                    ) -> ReportElement:
    """Generates a simple header title without an animated background."""
    
    res      = ReportElement()
    res.type = ReportElementTypes.HEAD_TITLE_ON_BACKGROUND
    
    res.body_content = f'''
        <div id="header">
            <div class="grid_12">
                <div class="grid_8 alpha">
                    <h1 class="title">{title}</h1>
                    {'<h2 class="subtitle">' + subtitle + '</h2>' if subtitle else ''}
                </div>
            </div>
        </div>
        <div class="content"></div>
    '''
    
    return res

# --------------------------------------------------------------------------------------------

def clean_css_content(css_content: str) -> str:
    """
    Cleans the CSS content by removing comments, unwanted spaces, newlines, tabs, and multiple spaces.

    Parameters
    ----------
    css_content : str
        The original CSS content.

    Returns
    -------
    str
        The cleaned CSS content with comments and unnecessary whitespaces removed.
    """
    # Remove CSS comments using regular expression
    css_without_comments = re.sub(r'/\*.*?\*/', '', css_content, flags = re.DOTALL)

    # Remove unnecessary spaces, newlines, tabs, and multiple spaces
    cleaned_css = css_without_comments.replace(" ", "").replace("\n", "").replace("\t", "").replace("    ", "")

    return cleaned_css

# --------------------------------------------------------------------------------------------
