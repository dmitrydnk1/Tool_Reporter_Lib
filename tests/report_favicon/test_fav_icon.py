import unittest
from unittest.mock import patch, mock_open
from tool_reporter_lib.report_favicon.fav_icon import _get_base64_favicon, FALLBACK_FAVICON_BASE64, FAVICON_BASE64_PATH

class TestFavIcon(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='data:image/png;base64,example_base64_data')
    def test_get_base64_favicon_file_exists(self, mock_file):
        # Test when the favicon file exists and contains data
        result = _get_base64_favicon()
        self.assertEqual(result, 'data:image/png;base64,example_base64_data')
        mock_file.assert_called_once_with(FAVICON_BASE64_PATH, 'r')

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_get_base64_favicon_file_not_found(self, mock_file):
        # Test when the favicon file does not exist
        result = _get_base64_favicon()
        self.assertEqual(result, FALLBACK_FAVICON_BASE64)
        mock_file.assert_called_once_with(FAVICON_BASE64_PATH, 'r')

if __name__ == '__main__':
    unittest.main()