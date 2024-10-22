import unittest

from tool_reporter_lib.utils.report_utils import (
    sanitize_filename,
    update_filename,
    get_current_datetime,
    get_clean_HTML_code
)

class TestReportUtils(unittest.TestCase):

    def test_sanitize_filename(self):
        self.assertEqual(sanitize_filename('my:invalid?file/name'), 'my_invalid_file_name')
        self.assertEqual(sanitize_filename('valid_filename'), 'valid_filename')
        self.assertEqual(sanitize_filename(''), 'default_filename')
        self.assertEqual(sanitize_filename('file with spaces'), 'file_with_spaces')
        self.assertEqual(sanitize_filename('file--with--dashes'), 'file_with_dashes')

    def test_update_filename(self):
        self.assertEqual(update_filename('report_(0001)'), 'report_(0002)')
        self.assertEqual(update_filename('my_report'), 'my_report_(0001)')
        self.assertEqual(update_filename('report_(0099)'), 'report_(0100)')
        self.assertEqual(update_filename('report_(9999)'), 'report_(10000)')
        self.assertEqual(update_filename('report'), 'report_(0001)')

    def test_get_current_datetime(self):
        current_datetime = get_current_datetime()
        self.assertRegex(current_datetime, r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}')

    def test_get_clean_HTML_code(self):
        html_code = '''
        <!-- This is a comment -->
        <div>    <p>My Text   </p>   </div>
        <script>  console.log('debug');   </script>
        '''
        expected_clean_html = '<div><p>My Text</p></div><script>console.log(\'debug\');</script>'
        self.assertEqual(get_clean_HTML_code(html_code), expected_clean_html)

        html_code_with_newlines = '''
        <div>
            <p>Line 1</p>
            <p>Line 2</p>
        </div>
        '''
        expected_clean_html_with_newlines = '<div><p>Line 1</p><p>Line 2</p></div>'
        self.assertEqual(get_clean_HTML_code(html_code_with_newlines), expected_clean_html_with_newlines)

if __name__ == '__main__':
    unittest.main()