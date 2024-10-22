import unittest
from unittest.mock import patch, mock_open

from tool_reporter_lib.elements.report_element_header_title import (
    get_header_title,
    _generate_random_color,
    _generate_random_size,
    _generate_random_position,
    _load_and_format_file,
    _get_header_title_simple,
    clean_css_content,
    ReportElement,
    ReportElementTypes
)

class TestReportElementHeaderTitle(unittest.TestCase):

    @patch('tool_reporter_lib.elements.report_element_header_title._load_and_format_file')
    def test_get_header_title_with_background(self, mock_load_and_format_file):
        mock_load_and_format_file.side_effect = ["formatted_css", "formatted_html"]
        title = "Main Title"
        subtitle = "Subtitle"
        result = get_header_title(title, subtitle, use_background_image=True)
        
        self.assertIsInstance(result, ReportElement)
        self.assertEqual(result.type, ReportElementTypes.HEAD_TITLE_ON_BACKGROUND)
        self.assertEqual(result.style_content, "formatted_css")
        self.assertEqual(result.body_content, "formatted_html")

    def test_get_header_title_without_background(self):
        title = "Main Title"
        subtitle = "Subtitle"
        result = get_header_title(title, subtitle, use_background_image=False)
        
        self.assertIsInstance(result, ReportElement)
        self.assertEqual(result.type, ReportElementTypes.HEAD_TITLE_ON_BACKGROUND)
        self.assertIn('<h1 class="title">Main Title</h1>', result.body_content)
        self.assertIn('<h2 class="subtitle">Subtitle</h2>', result.body_content)

    def test_generate_random_color(self):
        color = _generate_random_color()
        self.assertRegex(color, r'^#[0-9a-fA-F]{6}$')

    def test_generate_random_size(self):
        size = _generate_random_size()
        self.assertGreaterEqual(size, 50)
        self.assertLessEqual(size, 200)

    def test_generate_random_position(self):
        position = _generate_random_position()
        self.assertGreaterEqual(position, 0)
        self.assertLessEqual(position, 90)

    @patch('builtins.open', new_callable=mock_open, read_data="content with {{key}}")
    def test_load_and_format_file(self, mock_file):
        params = {'key': 'value'}
        result = _load_and_format_file('dummy_path', params)
        self.assertEqual(result, "content with value")

    def test_get_header_title_simple(self):
        title = "Main Title"
        subtitle = "Subtitle"
        result = _get_header_title_simple(title, subtitle)
        
        self.assertIsInstance(result, ReportElement)
        self.assertEqual(result.type, ReportElementTypes.HEAD_TITLE_ON_BACKGROUND)
        self.assertIn('<h1 class="title">Main Title</h1>', result.body_content)
        self.assertIn('<h2 class="subtitle">Subtitle</h2>', result.body_content)

    def test_clean_css_content(self):
        css_content = "/* comment */ body { color: red; }"
        cleaned_content = clean_css_content(css_content)
        self.assertNotIn("/* comment */", cleaned_content)
        self.assertIn("body { color: red; }", cleaned_content)

if __name__ == '__main__':
    unittest.main()