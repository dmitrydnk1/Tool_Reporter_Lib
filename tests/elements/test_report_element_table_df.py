import unittest
import pandas as pd
from tool_reporter_lib.elements.report_element_table_df import get_table_dataframe_element
from tool_reporter_lib.elements.report_element import ReportElement, ReportElementTypes



class TestReportElementTableDF(unittest.TestCase):
    """
    Unit tests for the `get_table_dataframe_element` function in report_element_table_df.py.
    """

    def setUp(self):
        """Set up sample DataFrame for testing."""
        self.data = {
            "A": [1, 2, 3, 4, 5],
            "B": [5, 4, 3, 2, 1],
            "C": [2.5, 3.5, 4.5, 5.5, 6.5],
        }
        self.df = pd.DataFrame(self.data)

    def test_report_element_type(self):
        """Test if the returned object is of type `ReportElement` and has correct type `DFTABLE`."""
        report_element = get_table_dataframe_element(self.df)
        self.assertIsInstance(
            report_element, ReportElement, "Output is not a ReportElement."
        )
        self.assertEqual(
            report_element.type,
            ReportElementTypes.DFTABLE,
            "Element type is not DFTABLE.",
        )

    def test_html_table_in_body_content(self):
        """Test if the body content contains the DataFrame as an HTML table."""
        report_element = get_table_dataframe_element(self.df)
        self.assertIn(
            "<table",
            report_element.body_content,
            "HTML table not found in body content.",
        )

    def test_highlight_column(self):
        """Test if highlighting works correctly by checking the presence of background-color in HTML."""
        report_element = get_table_dataframe_element(self.df, highlight_columns=["C"])
        self.assertIn(
            "background-color",
            report_element.body_content,
            "Highlighting not applied to column C.",
        )

    def test_rounding(self):
        """Test if rounding of float values is correctly applied."""
        report_element = get_table_dataframe_element(self.df, round=1)
        self.assertIn(
            "2.5",
            report_element.body_content,
            "Rounding not correctly applied to float values.",
        )

    def test_table_with_multiple_columns(self):
        """Test if a table with multiple columns renders without errors and without extra divs."""
        df_wide = pd.DataFrame({f"col{i}": range(5) for i in range(10)})
        report_element = get_table_dataframe_element(
            df_wide, df_min_col_amount_for_full_width=8
        )
        self.assertNotIn(
            '<div class="grid_12">',
            report_element.body_content,
            "grid_12 div should not be added.",
        )



    


if __name__ == "__main__":
    unittest.main()
