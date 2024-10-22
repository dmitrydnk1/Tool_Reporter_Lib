import unittest
from tool_reporter_lib.elements.report_element_footer import get_footer_element
from tool_reporter_lib.elements.report_element import ReportElementTypes

class TestReportElementFooter(unittest.TestCase):

    def test_get_footer_element_type(self):
        footer_element = get_footer_element()
        self.assertEqual(footer_element.type, ReportElementTypes.FOOTER, "Footer element type should be FOOTER")

    def test_get_footer_element_body_content(self):
        footer_element = get_footer_element()
        expected_body_content = '''
        </div>
        </div>        
    '''
        self.assertEqual(footer_element.body_content.strip(), expected_body_content.strip(), "Footer element body content does not match expected content")

if __name__ == '__main__':
    unittest.main()