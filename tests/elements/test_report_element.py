import unittest
from tool_reporter_lib.elements.report_element import ReportElement, ReportElementTypes, get_report_element_type_str

class TestReportElementTypes(unittest.TestCase):

    def test_enum_values(self):
        self.assertEqual(ReportElementTypes.NONE.value, 'none')
        self.assertEqual(ReportElementTypes.TITLE.value, 'title')
        self.assertEqual(ReportElementTypes.TEXT.value, 'text')
        self.assertEqual(ReportElementTypes.CHART.value, 'chart')
        self.assertEqual(ReportElementTypes.STYLE.value, 'style')
        self.assertEqual(ReportElementTypes.SPACE.value, 'space')
        self.assertEqual(ReportElementTypes.DFTABLE.value, 'df_table')
        self.assertEqual(ReportElementTypes.OTHER.value, 'other')
        self.assertEqual(ReportElementTypes.FOOTER.value, 'footer')
        self.assertEqual(ReportElementTypes.CODE.value, 'code')
        self.assertEqual(ReportElementTypes.ALERT_BOX.value, 'alert_box')
        self.assertEqual(ReportElementTypes.TEXT_CONSOLE.value, 'text_console')
        self.assertEqual(ReportElementTypes.HEAD_TITLE_ON_BACKGROUND.value, 'Head_title_on_background')
        self.assertEqual(ReportElementTypes.HORIZONTAL_LINE.value, 'horizontal_line')
        self.assertEqual(ReportElementTypes.PARAM_VALUE_TABLE.value, 'param_value_table')
        self.assertEqual(ReportElementTypes.PARAM_VALUE_TABLE_v2.value, 'param_value_table_v2')
        self.assertEqual(ReportElementTypes.PARAM_VALUE_GRID.value, 'param_value_grid')
        self.assertEqual(ReportElementTypes.SHOWHIDE_REGION_OPEN.value, 'showhide_region_open')
        self.assertEqual(ReportElementTypes.SHOWHIDE_REGION_CLOSE.value, 'showhide_region_close')
        self.assertEqual(ReportElementTypes.IMAGE_JPEG.value, 'image/jpeg')
        self.assertEqual(ReportElementTypes.IMAGE_PNG.value, 'image/png')

    def test_get_report_element_type_str(self):
        self.assertEqual(get_report_element_type_str(ReportElementTypes.NONE), 'none')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.TITLE), 'title')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.TEXT), 'text')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.CHART), 'chart')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.STYLE), 'style')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.SPACE), 'space')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.DFTABLE), 'df_table')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.OTHER), 'other')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.FOOTER), 'footer')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.CODE), 'code')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.ALERT_BOX), 'alert_box')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.TEXT_CONSOLE), 'text_console')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.HEAD_TITLE_ON_BACKGROUND), 'Head_title_on_background')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.HORIZONTAL_LINE), 'horizontal_line')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.PARAM_VALUE_TABLE), 'param_value_table')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.PARAM_VALUE_TABLE_v2), 'param_value_table_v2')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.PARAM_VALUE_GRID), 'param_value_grid')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.SHOWHIDE_REGION_OPEN), 'showhide_region_open')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.SHOWHIDE_REGION_CLOSE), 'showhide_region_close')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.IMAGE_JPEG), 'image/jpeg')
        self.assertEqual(get_report_element_type_str(ReportElementTypes.IMAGE_PNG), 'image/png')

class TestReportElement(unittest.TestCase):

    def test_initialization(self):
        element = ReportElement()
        self.assertEqual(element.type, ReportElementTypes.NONE)
        self.assertEqual(element.body_content, '')
        self.assertEqual(element.style_content, '')

    def test_str_representation(self):
        element = ReportElement()
        self.assertEqual(str(element), 'ReportElement: \tnone')

    def test_repr_representation(self):
        element = ReportElement()
        self.assertEqual(repr(element), 'ReportElement: \tnone')

    def test_get_style_str(self):
        element = ReportElement()
        element.style_content = 'style content'
        self.assertEqual(element.get_style_str(), 'style content')

    def test_get_body_str(self):
        element = ReportElement()
        element.body_content = 'body content'
        self.assertEqual(element.get_body_str(), 'body content')

if __name__ == '__main__':
    unittest.main()