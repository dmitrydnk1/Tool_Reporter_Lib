import unittest
from unittest.mock import patch, mock_open
import os
from tool_reporter_lib.elements.report_style import get_css_file_path, clean_css_content, get_css_content, validate_css_structure

class TestReportStyle(unittest.TestCase):
    
    def test_clean_css_content(self):
        css_content = """
        /* This is a comment */
        body {
            background-color: white; /* Another comment */
        }
        .grid_2 {
            width: 50%;
        }
        """
        expected_cleaned_content = "body {background-color: white;}.grid_2 {width: 50%;}"
        self.assertEqual(clean_css_content(css_content), expected_cleaned_content)

    @patch('os.path.exists')
    def test_get_css_content_file_not_found(self, mock_exists):
        mock_exists.return_value = False
        with self.assertRaises(FileNotFoundError):
            get_css_content()

    def test_validate_css_structure(self):
        valid_css_content = """
        body { background-color: white; }
        .grid_2 { width: 50%; }
        #header { height: 100px; }
        .minimalistic-style-table { border: 1px solid black; }
        """
        invalid_css_content = "body { background-color: white; }"
        self.assertTrue(validate_css_structure(valid_css_content))
        self.assertFalse(validate_css_structure(invalid_css_content))

if __name__ == '__main__':
    unittest.main()