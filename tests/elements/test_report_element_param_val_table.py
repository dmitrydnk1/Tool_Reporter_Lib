import unittest
from tool_reporter_lib.elements.report_element import ReportElement, ReportElementTypes

from tool_reporter_lib.elements.report_element_param_val_table import (
    get_param_value_table_element,
    get_param_value_table_element_v2,
    _short_str,
    _short_repr,
    _short_float,
    _truncate_long_string,
)

class TestReportElementParamValTable(unittest.TestCase):

    def test_get_param_value_table_element(self):
        param_value_table = {'param1': 'value1', 'param2': 'value2'}
        title = 'Test Title'
        cfg_truncate_len = 10

        result = get_param_value_table_element(param_value_table, title, cfg_truncate_len)

        self.assertIsInstance(result, ReportElement)
        self.assertEqual(result.type, ReportElementTypes.PARAM_VALUE_TABLE)
        self.assertIn('<h2>Test Title</h2>', result.body_content)
        self.assertIn('<div class="param-value-caption">param1</div>', result.body_content)
        self.assertIn('<div class="param-value-caption">param2</div>', result.body_content)

    def test_get_param_value_table_element_v2(self):
        param_value_table = {'param1': 'value1', 'param2': 'value2'}
        title = 'Test Title'

        result = get_param_value_table_element_v2(param_value_table, title)

        self.assertIsInstance(result, ReportElement)
        self.assertEqual(result.type, ReportElementTypes.PARAM_VALUE_TABLE_v2)
        self.assertIn('<h2>Test Title</h2>', result.body_content)
        self.assertIn('<td>param1</td>', result.body_content)
        self.assertIn('<td>param2</td>', result.body_content)

    def test_short_str(self):
        self.assertEqual(_short_str('a' * 100, 10), 'aaaaaaaaaa...')
        self.assertEqual(_short_str(123.456789, 10), '123.4568')
        self.assertEqual(_short_str([1, 2, 3, 4, 5], 10), '[1, 2, .., 5]')

    def test_short_repr(self):
        self.assertEqual(_short_repr([1, 2, 3, 4, 5]), '[1, 2, .., 5]')
        self.assertEqual(_short_repr([1, 2]), '[1, 2]')

    def test_short_float(self):
        self.assertEqual(_short_float(123.456789), '123.4568')
        self.assertEqual(_short_float(123.4), '123.4')

    def test_truncate_long_string(self):
        self.assertEqual(_truncate_long_string('a' * 100, 10), 'aaaaaaaaaa...')
        self.assertEqual(_truncate_long_string('short', 10), 'short')

if __name__ == '__main__':
    unittest.main()