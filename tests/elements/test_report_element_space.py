import unittest
from tool_reporter_lib.elements.report_element_space import get_space_element
from tool_reporter_lib.elements.report_element import ReportElement, ReportElementTypes

class TestReportElementSpace(unittest.TestCase):

    def test_get_space_element_type(self):
        """Test if the type of the returned ReportElement is SPACE."""
        element = get_space_element()
        self.assertEqual(element.type, ReportElementTypes.SPACE)

    def test_get_space_element_body_content(self):
        """Test if the body content of the returned ReportElement is an empty paragraph."""
        element = get_space_element()
        expected_body_content = '''        
        <p></p>
    '''
        self.assertEqual(element.body_content, expected_body_content)

    def test_get_space_element_instance(self):
        """Test if the returned object is an instance of ReportElement."""
        element = get_space_element()
        self.assertIsInstance(element, ReportElement)

if __name__ == '__main__':
    unittest.main()