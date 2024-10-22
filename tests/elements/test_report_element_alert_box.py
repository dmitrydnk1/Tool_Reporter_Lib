import unittest
from tool_reporter_lib.elements.report_element_alert_box import get_alert_box_element, _get_alert_type, _get_alert_box_emoji
from tool_reporter_lib.elements.report_element import ReportElementTypes

class TestReportElementAlertBox(unittest.TestCase):

    def test_get_alert_box_element_default(self):
        element = get_alert_box_element("This is an info alert")
        self.assertEqual(element.type, ReportElementTypes.ALERT_BOX)
        self.assertIn('class="alert-box info-box"', element.body_content)
        self.assertIn('ℹ️', element.body_content)
        self.assertIn('This is an info alert', element.body_content)

    def test_get_alert_box_element_warning(self):
        element = get_alert_box_element("This is a warning alert", alert_type='warning')
        self.assertEqual(element.type, ReportElementTypes.ALERT_BOX)
        self.assertIn('class="alert-box warning-box"', element.body_content)
        self.assertIn('⚠️', element.body_content)
        self.assertIn('This is a warning alert', element.body_content)

    def test_get_alert_box_element_custom_emoji(self):
        element = get_alert_box_element("This is a custom emoji alert", emoji='🚀')
        self.assertEqual(element.type, ReportElementTypes.ALERT_BOX)
        self.assertIn('class="alert-box info-box"', element.body_content)
        self.assertIn('🚀', element.body_content)
        self.assertIn('This is a custom emoji alert', element.body_content)

    def test_get_alert_type(self):
        self.assertEqual(_get_alert_type('i'), 'info')
        self.assertEqual(_get_alert_type('info'), 'info')
        self.assertEqual(_get_alert_type('w'), 'warning')
        self.assertEqual(_get_alert_type('warning'), 'warning')
        self.assertEqual(_get_alert_type('n'), 'note')
        self.assertEqual(_get_alert_type('note'), 'note')
        self.assertEqual(_get_alert_type('e'), 'error')
        self.assertEqual(_get_alert_type('error'), 'error')
        self.assertEqual(_get_alert_type('unknown'), 'info')

    def test_get_alert_box_emoji(self):
        self.assertEqual(_get_alert_box_emoji('info'), 'ℹ️')
        self.assertEqual(_get_alert_box_emoji('warning'), '⚠️')
        self.assertEqual(_get_alert_box_emoji('note'), '')
        self.assertEqual(_get_alert_box_emoji('error'), '❌')
        self.assertEqual(_get_alert_box_emoji('unknown'), 'ℹ️')

if __name__ == '__main__':
    unittest.main()