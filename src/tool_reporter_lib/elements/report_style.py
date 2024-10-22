# ============================================================================================
"""
This module provides functionality to load, clean, and validate the CSS styles from an external file.
"""

__version__     : str = '0.0.9'
__version_date__: str = '2024-10-20'
_name_          : str = 'Report Style Loader'
VERSION         : str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.9 @ 2024-10-20 : Added CSS content cleaning and validation functions.
#                     : Separated CSS file path retrieval from content loading.
# ============================================================================================

import os
import re

# --------------------------------------------------------------------------------------------
# TODO NOTES:
# --------------------------------------------------------------------------------------------
# 1. Consider adding fallback CSS if the external file is missing.
# 2. Add support for dynamic theming of report styles.
# 3. Create additional helper functions to modify CSS at runtime if needed.
# --------------------------------------------------------------------------------------------

def get_css_file_path() -> str:
    """
    Retrieves the path to the CSS file.

    Returns
    -------
    str
        The absolute path to the report_style.css file.
    """
    return os.path.join(os.path.dirname(__file__), 'report_style.css')

# -----------------------------------------------------------------------------------------------------------

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
    css_without_comments = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)

    # Remove leading and trailing whitespaces
    css_without_comments = css_without_comments.strip()

    # Remove unnecessary spaces, newlines, and tabs
    cleaned_css = re.sub(r'[\n\t]+', ' ', css_without_comments)

    # Remove multiple spaces
    cleaned_css = re.sub(r'\s{2,}', ' ', cleaned_css)

    # Ensure consistent spacing around '{', '}', and ';'
    cleaned_css = re.sub(r'\s*([{};])\s*', r'\1', cleaned_css)

    # Add a single space before '{'
    cleaned_css = re.sub(r'([^\s{])\{', r'\1 {', cleaned_css)

    # Final cleanup to remove leading/trailing spaces
    cleaned_css = cleaned_css.strip()
        
    return cleaned_css

# -----------------------------------------------------------------------------------------------------------

def get_css_content() -> str:
    """
    Loads the CSS content from the external CSS file and cleans it by removing comments and unwanted spaces.

    Returns
    -------
    str
        The cleaned and processed CSS content.

    Raises
    ------
    FileNotFoundError
        If the CSS file cannot be found.
    """
    css_file_path = get_css_file_path()
    
    if not os.path.exists(css_file_path):
        raise FileNotFoundError(f"CSS file not found at {css_file_path}")

    with open(css_file_path, 'r') as css_file:
        css_content = css_file.read()
    
    # Clean the CSS content
    return clean_css_content(css_content)


# -----------------------------------------------------------------------------------------------------------
#
#                            Testing: Add meaningful test cases
#
# -----------------------------------------------------------------------------------------------------------

def validate_css_structure(css_content: str) -> bool:
    """
    Validates the structure of the loaded CSS content.
    This is a simple validation function that ensures the CSS content is well-formed.

    Parameters
    ----------
    css_content : str
        The CSS content to validate.

    Returns
    -------
    bool
        True if the structure of the CSS content is valid, False otherwise.
    """
    # Example basic validation: check if important CSS selectors or keywords exist
    required_selectors = ['.grid_2', 'body', '#header', '.minimalistic-style-table']
    return all(selector in css_content for selector in required_selectors)

# -----------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    try:
        css_content = get_css_content()
        print("Cleaned CSS Content Successfully Loaded:\n", css_content)

        # Test the CSS structure
        if validate_css_structure(css_content):
            print("CSS Structure is valid.")
        else:
            print("CSS Structure validation failed.")
            
    except FileNotFoundError as e:
        print(str(e))
