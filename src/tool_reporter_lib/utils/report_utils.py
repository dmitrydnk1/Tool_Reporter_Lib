# ============================================================================================
#                                  Reporter - Utils Functions
# ============================================================================================

__version__:      str = '0.0.9'
__version_date__: str = '2024-10-20'
_name_:           str = 'Reporter - Utils Functions'
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# v0.0.2 @ 2024-08-13 : Initial Release
# v0.0.3 @ 2024-08-21 : Added utility functions for filename sanitization and date-time retrieval.
# v0.0.9 @ 2024-10-20 : Added HTML code cleaner to minimize file size by removing comments, tabs, and excess spaces.
# --------------------------------------------------------------------------------------------

# --- TODO : ---------------------------------------------------------------------------------
# - Need to fix get clean HTML code function to handle script tags and other special cases.
# ============================================================================================

import re
from datetime import datetime

# --------------------------------------------------------------------------------------------
#                                   UTILITY FUNCTIONS:
# --------------------------------------------------------------------------------------------

def sanitize_filename(filename: str) -> str:
    """
    Sanitize the given filename by replacing unacceptable characters with underscores and
    ensuring that the filename is valid and safe to use in file systems.

    Parameters
    ----------
    filename : str
        The filename to sanitize.

    Returns
    -------
    str
        The sanitized filename. If the resulting string is empty, 'default_filename' is returned.
    
    Example
    -------
    >>> sanitize_filename('my:invalid?file/name')
    'my_invalid_file_name'
    """
    pattern   = r'[^\w\s-]'  # Match any character that is not alphanumeric, whitespace, underscore, or hyphen.
    sanitized = re.sub(pattern, '_', filename).strip()  # Replace with underscores and remove leading/trailing spaces.
    sanitized = re.sub(r'[\s_-]+', '_', sanitized)  # Replace multiple consecutive spaces/underscores with a single one.
    
    return sanitized or "default_filename"

# --------------------------------------------------------------------------------------------

def update_filename(filename_old: str) -> str:
    """
    Update the filename by appending or incrementing a number in (NNNN) format at the end.
    If the filename already contains a number, it increments it by 1.

    Parameters
    ----------
    filename_old : str
        The original filename to be updated.

    Returns
    -------
    str
        The updated filename with an incremented number or '(0001)' appended if no number exists.
    
    Example
    -------
    >>> update_filename('report_(0001)')
    'report_(0002)'
    
    >>> update_filename('my_report')
    'my_report_(0001)'
    """
    pattern = r"\(\d{4}\)$"  # Regex pattern to find (NNNN) at the end of the filename.
    match   = re.search(pattern, filename_old)

    if match:
        number = int(match.group()[1:-1]) + 1  # Extract the number and increment by 1.
        return re.sub(pattern, f"({number:04d})", filename_old)  # Replace the old number with the incremented number.
    else:
        return f"{filename_old}_(0001)"  # Append (0001) if no number exists in the filename.

# --------------------------------------------------------------------------------------------

def get_current_datetime() -> str:
    """
    Get the current date and time formatted as a string with milliseconds.

    Returns
    -------
    str
        The current date and time in the format: YYYY-MM-DD HH:MM:SS.mmm
    
    Example
    -------
    >>> get_current_datetime()
    '2024-08-21 15:23:45.123'
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

# --------------------------------------------------------------------------------------------

def get_clean_HTML_code(html_code: str) -> str:
    """
    Cleans and minifies the given HTML code by removing unnecessary comments, spaces, tabs, and 
    newlines to reduce the size of the final HTML file.

    Parameters
    ----------
    html_code : str
        The raw HTML code as a string.

    Returns
    -------
    str
        The cleaned and minified HTML code.
    
    Example
    -------
    >>> html_code = '''
    ... <!-- This is a comment -->
    ... <div>    <p>My Text   </p>   </div>
    ... <script>  console.log('debug');   </script>
    ... '''
    >>> clean_html = get_clean_HTML_code(html_code)
    >>> print(clean_html)
    '<div><p>My Text</p></div><script>console.log('debug');</script>'
    """
    # Step 1: Remove all HTML comments
    clean_code = re.sub(r'<!--.*?-->', '', html_code, flags=re.DOTALL)
    
    # Step 2: Remove leading and trailing whitespace from each line
    clean_code = "\n".join(line.strip() for line in clean_code.splitlines())
    
    # Step 3: Remove multiple spaces between HTML tags
    clean_code = re.sub(r'>\s+<', '><', clean_code)
    
    # Step 4: Replace multiple spaces or tabs within the text content
    clean_code = re.sub(r'\s{2,}', ' ', clean_code)
    
    # Step 5: Remove extra newlines
    clean_code = re.sub(r'\n+', '\n', clean_code)
    
    # Step 6: Remove spaces around tags
    clean_code = re.sub(r'\s*(<[^>]+>)\s*', r'\1', clean_code)
    
    return clean_code.strip()

# ============================================================================================
