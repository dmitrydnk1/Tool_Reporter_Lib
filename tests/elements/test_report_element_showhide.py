import unittest
from tool_reporter_lib.elements.report_element import ReportElementTypes

from tool_reporter_lib.elements.report_element_showhide import (
    get_showhide_region_open_element,
    get_showhide_region_close_element
)

class TestReportElementShowHide(unittest.TestCase):

    def test_get_showhide_region_open_element(self):
        title = "Test Title"
        region_name = "test_region"
        use_hide = True

        element = get_showhide_region_open_element(title, region_name, use_hide)

        self.assertEqual(element.type, ReportElementTypes.SHOWHIDE_REGION_OPEN)
        self.assertIn(f"toggleContent('{region_name}', this, '{title}')", element.body_content)
        self.assertIn(f"id=\"{region_name}\"", element.body_content)
        self.assertIn(f"▶ Show {title}", element.body_content)

    def test_get_showhide_region_close_element(self):
        element = get_showhide_region_close_element()

        self.assertEqual(element.type, ReportElementTypes.SHOWHIDE_REGION_CLOSE)
        self.assertEqual(element.body_content.strip(), "</div>")

if __name__ == '__main__':
    unittest.main()