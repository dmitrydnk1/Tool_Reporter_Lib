import unittest
from unittest.mock import patch, MagicMock
from src.tool_reporter_lib.elements.report_element_style import get_style_element
from src.tool_reporter_lib.elements.report_element import ReportElement, ReportElementTypes

class TestReportElementStyle(unittest.TestCase):

    @patch('src.tool_reporter_lib.elements.report_element_style.get_css_content')
    def test_get_style_element_success(self, mock_get_css_content):
        # Arrange
        mock_css_content = "body { font-family: Arial; }"
        mock_get_css_content.return_value = mock_css_content

        # Act
        result = get_style_element()

        # Assert
        self.assertIsInstance(result, ReportElement)
        self.assertEqual(result.type, ReportElementTypes.STYLE)
        self.assertEqual(result.style_content, mock_css_content)
        mock_get_css_content.assert_called_once()

    @patch('src.tool_reporter_lib.elements.report_element_style.get_css_content')
    def test_get_style_element_file_not_found(self, mock_get_css_content):
        # Arrange
        mock_get_css_content.side_effect = FileNotFoundError("CSS file not found")

        # Act & Assert
        with self.assertRaises(FileNotFoundError):
            get_style_element()
        mock_get_css_content.assert_called_once()

if __name__ == '__main__':
    unittest.main()