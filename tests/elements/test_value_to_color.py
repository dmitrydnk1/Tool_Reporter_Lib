import unittest
import numpy as np
from matplotlib.colors import Colormap
from matplotlib import pyplot as plt
from tool_reporter_lib.elements.value_to_color import generate_hex_colors_list, value_to_color, VIRIDIS_COLOR_MAP

class TestValueToColorFunctions(unittest.TestCase):

    def test_generate_hex_colors_list_default(self):
        hex_colors = generate_hex_colors_list()
        self.assertEqual(len(hex_colors), 20)
        self.assertTrue(all(isinstance(color, str) and color.startswith('#') for color in hex_colors))

    def test_generate_hex_colors_list_custom_amount(self):
        hex_colors = generate_hex_colors_list(amount=10)
        self.assertEqual(len(hex_colors), 10)
        self.assertTrue(all(isinstance(color, str) and color.startswith('#') for color in hex_colors))

    def test_generate_hex_colors_list_custom_colormap(self):
        colormap = plt.get_cmap('plasma')
        hex_colors = generate_hex_colors_list(colormap=colormap)
        self.assertEqual(len(hex_colors), 20)
        self.assertTrue(all(isinstance(color, str) and color.startswith('#') for color in hex_colors))

    def test_value_to_color_default(self):
        color = value_to_color(0.5, 0, 1)
        self.assertTrue(isinstance(color, str) and color.startswith('#'))

    def test_value_to_color_nan(self):
        color = value_to_color(np.nan, 0, 1)
        self.assertEqual(color, '#ff0000')

    def test_value_to_color_invalid_colormap(self):
        color = value_to_color(0.5, 0, 1, colormap_name='invalid_colormap')
        self.assertTrue(isinstance(color, str) and color.startswith('#'))

    def test_value_to_color_custom_colormap(self):
        color = value_to_color(0.5, 0, 1, colormap_name='plasma')
        self.assertTrue(isinstance(color, str) and color.startswith('#'))

    def test_value_to_color_custom_palette_part(self):
        color = value_to_color(0.5, 0, 1, used_palette_part=0.8)
        self.assertTrue(isinstance(color, str) and color.startswith('#'))

    def test_value_to_color_min_max(self):
        color = value_to_color(0, 0, 1)
        self.assertTrue(isinstance(color, str) and color.startswith('#'))
        color = value_to_color(1, 0, 1)
        self.assertTrue(isinstance(color, str) and color.startswith('#'))

if __name__ == '__main__':
    unittest.main()