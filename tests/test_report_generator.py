import unittest
import os
import pandas as pd
from unittest.mock import patch, MagicMock
from tool_reporter_lib.report_generator import ReportHTML

import matplotlib.pyplot as plt

class TestReportHTML(unittest.TestCase):

    def setUp(self):
        self.report = ReportHTML(title="Test Report", sub_title="Test Subtitle", file_name="test_report")

    def tearDown(self):
        # Clean up any files created during tests
        if os.path.exists(self.report._file_path):
            os.remove(self.report._file_path)

    def test_initialization(self):
        self.assertEqual(self.report.title, "Test Report")
        self.assertEqual(self.report.sub_title, "Test Subtitle")
        self.assertEqual(self.report.report_file_name, "test_report")
        self.assertTrue(self.report.use_title_background)
        self.assertIsInstance(self.report.elements_list, list)
        self.assertIsInstance(self.report.bottom_elements_list, list)

    def test_add_title(self):
        self.report.add_title("Section Title", h_level=2, use_center=True)
        self.assertEqual(len(self.report.elements_list), 3)  # style, header, and title elements

    def test_add_text(self):
        self.report.add_text("This is a test text.")
        self.assertEqual(len(self.report.elements_list), 3)  # style, header, and text elements

    def test_add_chart(self):
        plt.figure()
        plt.plot([1, 2, 3, 4])
        self.report.add_chart(plt)
        self.assertEqual(len(self.report.elements_list), 3)  # style, header, and chart elements

    def test_add_dataframe_table(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        self.report.add_dataframe_table(df)
        self.assertEqual(len(self.report.elements_list), 3)  # style, header, and dataframe table elements

    def test_save_to_file(self):
        with patch('webbrowser.open_new_tab') as mock_open:
            self.report.save_to_file()
            self.assertTrue(os.path.exists(self.report._file_path))
            mock_open.assert_called_once_with(self.report._file_path)

    def test_update_header_title(self):
        self.report.update_header_title(title="Updated Title", subtitle="Updated Subtitle", use_title_background=False)
        self.assertEqual(self.report.title, "Updated Title")
        self.assertEqual(self.report.sub_title, "Updated Subtitle")
        self.assertFalse(self.report.use_title_background)

    def test_add_alert_box(self):
        self.report.add_alert_box("This is an info alert.", alert_type='i')
        self.assertEqual(len(self.report.elements_list), 3)  # style, header, and alert box elements

    def test_add_showhide_region(self):
        self.report.add_showhide_region_open("Show/Hide Region")
        self.report.add_text("This is inside the region.")
        self.report.add_showhide_region_close()
        self.assertEqual(len(self.report.elements_list), 5)  # style, header, show/hide open, text, and show/hide close elements

    def test_move_element_to_bottom(self):
        self.report.add_text("This is a text element.")
        self.report.move_element_to_bottom()
        self.assertEqual(len(self.report.elements_list), 2)  # style and header elements
        self.assertEqual(len(self.report.bottom_elements_list), 1)  # text element

if __name__ == '__main__':
    unittest.main()