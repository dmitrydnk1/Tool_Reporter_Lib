import unittest
from tool_reporter_lib.elements.report_element_title import get_title_element
from tool_reporter_lib.elements.report_element import ReportElement, ReportElementTypes

class TestGetTitleElement(unittest.TestCase):

    def test_default_title(self):
        title = "Default Title"
        element = get_title_element(title)
        self.assertEqual(element.type, ReportElementTypes.TITLE)
        self.assertIn('<h1>Default Title</h1>', element.body_content)
        self.assertNotIn('align="center"', element.body_content)

    def test_custom_heading_level(self):
        title = "Custom Heading"
        element = get_title_element(title, h_level=2)
        self.assertEqual(element.type, ReportElementTypes.TITLE)
        self.assertIn('<h2>Custom Heading</h2>', element.body_content)

    def test_heading_level_out_of_bounds(self):
        title = "Out of Bounds Heading"
        element = get_title_element(title, h_level=5)
        self.assertEqual(element.type, ReportElementTypes.TITLE)
        self.assertIn('<h3>Out of Bounds Heading</h3>', element.body_content)

    def test_centered_title(self):
        title = "Centered Title"
        element = get_title_element(title, use_center=True)
        self.assertEqual(element.type, ReportElementTypes.TITLE)
        self.assertIn('<div align="center">', element.body_content)
        self.assertIn('<h1>Centered Title</h1>', element.body_content)

    def test_centered_custom_heading(self):
        title = "Centered Custom Heading"
        element = get_title_element(title, h_level=3, use_center=True)
        self.assertEqual(element.type, ReportElementTypes.TITLE)
        self.assertIn('<div align="center">', element.body_content)
        self.assertIn('<h3>Centered Custom Heading</h3>', element.body_content)

if __name__ == '__main__':
    unittest.main()