import unittest
from tool_reporter_lib.elements.report_element_text_console import get_text_console_element
from tool_reporter_lib.elements.report_element import ReportElement, ReportElementTypes

class TestReportElementTextConsole(unittest.TestCase):

    def test_get_text_console_element(self):
        text = "Sample console text"
        element = get_text_console_element(text)
        
        self.assertIsInstance(element, ReportElement)
        self.assertEqual(element.type, ReportElementTypes.TEXT_CONSOLE)
        self.assertIn('<div class="grid_12">', element.body_content)
        self.assertIn('<div style="font-family: monospace; white-space: pre;">', element.body_content)
        self.assertIn(f'<p>{text}</p>', element.body_content)

    def test_get_text_console_element_empty_text(self):
        text = ""
        element = get_text_console_element(text)
        
        self.assertIsInstance(element, ReportElement)
        self.assertEqual(element.type, ReportElementTypes.TEXT_CONSOLE)
        self.assertIn('<div class="grid_12">', element.body_content)
        self.assertIn('<div style="font-family: monospace; white-space: pre;">', element.body_content)
        self.assertIn('<p></p>', element.body_content)

    def test_get_text_console_element_whitespace_text(self):
        text = "   "
        element = get_text_console_element(text)
        
        self.assertIsInstance(element, ReportElement)
        self.assertEqual(element.type, ReportElementTypes.TEXT_CONSOLE)
        self.assertIn('<div class="grid_12">', element.body_content)
        self.assertIn('<div style="font-family: monospace; white-space: pre;">', element.body_content)
        self.assertIn(f'<p>{text}</p>', element.body_content)

if __name__ == '__main__':
    unittest.main()