import unittest
from tool_reporter_lib.elements.report_element_text import get_text_element
from tool_reporter_lib.elements.report_element import ReportElementTypes

class TestReportElementText(unittest.TestCase):

    def test_get_text_element(self):
        text = "Sample text for testing"
        element = get_text_element(text)
        
        self.assertIsNotNone(element)
        self.assertEqual(element.type, ReportElementTypes.TEXT)
        self.assertIn('<div class="grid_12">', element.body_content)
        self.assertIn('<div style="white-space: pre;">', element.body_content)
        self.assertIn(f'<p>{text}</p>', element.body_content)

if __name__ == '__main__':
    unittest.main()