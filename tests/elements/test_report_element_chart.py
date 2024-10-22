import unittest
from tool_reporter_lib.elements.report_element_chart import get_chart_element
from tool_reporter_lib.elements.report_element import ReportElement, ReportElementTypes

import matplotlib.pyplot as plt

class TestGetChartElement(unittest.TestCase):

    def setUp(self):
        # Create a simple plot for testing
        self.fig, self.ax = plt.subplots()
        self.ax.plot([0, 1], [0, 1])

    def test_default_parameters(self):
        element = get_chart_element(self.fig)
        self.assertIsInstance(element, ReportElement)
        self.assertEqual(element.type, ReportElementTypes.CHART)
        self.assertIn('<img align="center"', element.body_content)
        self.assertIn('data:image/png;base64,', element.body_content)
        self.assertIn('width=""', element.body_content)
        self.assertIn('height=""', element.body_content)

    def test_custom_dimensions(self):
        element = get_chart_element(self.fig, heigth=400, width=600)
        self.assertIn('width="600"', element.body_content)
        self.assertIn('height="400"', element.body_content)

    def test_fullwidth(self):
        element = get_chart_element(self.fig, use_fullwidth=True)
        self.assertNotIn('<div class="grid_12">', element.body_content)

    def test_non_transparent_plot(self):
        element = get_chart_element(self.fig, use_transparent_plots=False)
        self.assertIn('data:image/png;base64,', element.body_content)

if __name__ == '__main__':
    unittest.main()