import unittest
from tool_reporter_lib.elements.report_element_horizontal_line import get_horizontal_line_element
from tool_reporter_lib.elements.report_element import ReportElementTypes

class TestReportElementHorizontalLine(unittest.TestCase):

    def test_get_horizontal_line_element_type(self):
        element = get_horizontal_line_element()
        self.assertEqual(element.type, ReportElementTypes.HORIZONTAL_LINE, "The element type should be HORIZONTAL_LINE")

    def test_get_horizontal_line_element_body_content(self):
        element = get_horizontal_line_element()
        expected_body_content = '''
        <div class="grid_12">
            <hr width="100%">
        </div>
    '''
        self.assertEqual(element.body_content.strip(), expected_body_content.strip(), "The body content should match the expected HTML for a horizontal line")

if __name__ == '__main__':
    unittest.main()