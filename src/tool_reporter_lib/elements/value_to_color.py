import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Colormap, rgb2hex

# ============================================================================================
# Meta Information
__version__:      str = "0.0.2"
__version_date__: str = "2024-08-13"
_name_:           str = "Value to Color Function"
VERSION:          str = f'{_name_:<20} VERSION: {__version__} @ {__version_date__}'

# --- VERSION HISTORY: -----------------------------------------------------------------------
# version: 0.0.2 @ 2024-08-13 : Initial Release
# ============================================================================================

# --- CONSTANTS: -----------------------------------------------------------------------------
COLOR_MAP_NAME_DEFAULT_LIST: list[str] = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
VIRIDIS_COLOR_MAP          : Colormap  = plt.get_cmap('viridis')

# ============================================================================================
#               Functions for Converting Value to Heatmap Color
# ============================================================================================

def generate_hex_colors_list(
                        colormap : Colormap = VIRIDIS_COLOR_MAP,
                        amount   : int      = 20,
                            ) -> list[str]: 
    """
    Generate a list of HEX colors from a colormap.

    Parameters
    ----------
    colormap : Colormap, optional
        The colormap to generate colors from, by default 'viridis'.
    amount : int, optional
        The number of colors to generate, by default 20.

    Returns
    -------
    list[str]
        List of HEX colors generated from the colormap.
    """
    colors     = colormap(np.linspace(0, 1, amount))
    hex_colors = [rgb2hex(color) for color in colors]  # Convert colors to HEX format
    
    return hex_colors

# --------------------------------------------------------------------------------------------

def value_to_color(
                    value            : float,
                    min_value        : float,
                    max_value        : float,
                    colormap_name    : str = 'viridis',
                    nan_color        : str = '#ff0000',
                    used_palette_part: float = 0.4,
                        ) -> str:
    """
    Return the HEX color for a given value based on a colormap.

    Parameters
    ----------
    value : float
        The value to be converted to a color.
    min_value : float
        The minimum value in the range.
    max_value : float
        The maximum value in the range.
    colormap_name : str, optional
        The name of the colormap to use, by default 'viridis'.
    nan_color : str, optional
        HEX color for NaN values, by default '#ff0000'.
    used_palette_part : float, optional
        The part of the palette to use, between 0.05 and 1.0, by default 0.4.

    Returns
    -------
    str
        HEX color value corresponding to the input value.
    
    Example
    -------
    >>> value_to_color(0.5, 0, 1, colormap_name = 'viridis')
    '#7fff7f'
    """

    # Handle NaN values
    if np.isnan(value):
        return nan_color
    
    # Validate colormap name
    if colormap_name not in plt.colormaps():
        emergency_colormap = COLOR_MAP_NAME_DEFAULT_LIST[0]
        print(f"!!! ERROR !!! Invalid colormap name: '{colormap_name}'")
        print(f"Using default colormap: '{emergency_colormap}'")
        colormap_name = emergency_colormap
    
    colormap = plt.get_cmap(colormap_name)
    
    # Normalize value between 0 and 1
    normalized_value = np.clip((value - min_value) / (max_value - min_value), 0, 1)
    
    # Adjust the used palette part
    used_palette_part = np.clip(used_palette_part, 0.05, 1.0)
    normalized_value  = 0.5 * (1.0 - used_palette_part) + normalized_value * used_palette_part
    
    # Get the color from the colormap and convert to HEX
    color     = colormap(normalized_value)
    hex_color = rgb2hex(color)
    
    return hex_color

# --------------------------------------------------------------------------------------------
