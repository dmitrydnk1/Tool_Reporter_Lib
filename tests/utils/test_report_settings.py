import unittest
from unittest.mock import patch, MagicMock
from tool_reporter_lib.utils.report_settings import Reports_Settings

class TestReportsSettings(unittest.TestCase):

    @patch('tool_reporter_lib.utils.report_settings.keyring')
    def test_activate_default_report_path(self, mock_keyring):
        mock_keyring.get_password.return_value = 'C:\\Reports\\'
        Reports_Settings.activate_default_report_path()
        self.assertEqual(Reports_Settings._folder_path, 'C:\\Reports\\')

    def test_set_folder_path(self):
        folder_path = 'D:\\CustomReports'
        Reports_Settings.set_folder_path(folder_path)
        self.assertEqual(Reports_Settings._folder_path, folder_path)

    def test_set_file_name(self):
        file_name = 'custom_report'
        Reports_Settings.set_file_name(file_name)
        self.assertEqual(Reports_Settings._report_file_name, file_name)

    def test_disable_open_saved_file(self):
        Reports_Settings.disable_open_saved_file()
        self.assertFalse(Reports_Settings.use_open_saved_file)

    def test_enable_open_saved_file(self):
        Reports_Settings.enable_open_saved_file()
        self.assertTrue(Reports_Settings.use_open_saved_file)

    def test_disable_header_title_on_background(self):
        Reports_Settings.disable_header_title_on_background()
        self.assertFalse(Reports_Settings.use_header_title_on_background)

    def test_enable_header_title_on_background(self):
        Reports_Settings.enable_header_title_on_background()
        self.assertTrue(Reports_Settings.use_header_title_on_background)

    @patch('builtins.print')
    def test_info(self, mock_print):
        Reports_Settings.info()
        mock_print.assert_any_call('Reports Settings: \n')
        mock_print.assert_any_call('-------------------')
        mock_print.assert_any_call(f'+ Folder Path:         {Reports_Settings._folder_path}')
        mock_print.assert_any_call(f'+ Custom Folder Path:  {Reports_Settings.custom_folder_path}')
        mock_print.assert_any_call(f'+ File Name:           {Reports_Settings._report_file_name}')
        mock_print.assert_any_call(f'+ File Format:         {Reports_Settings._file_format}')
        mock_print.assert_any_call(f'+ Use Open Saved File: {Reports_Settings.use_open_saved_file}')
        mock_print.assert_any_call(f'+ Use Header Title:    {Reports_Settings.use_header_title_on_background}')

if __name__ == '__main__':
    unittest.main()