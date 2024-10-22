import unittest
from tool_reporter_lib.elements.report_element_code import get_code_element
from tool_reporter_lib.elements.report_element import ReportElementTypes

class TestGetCodeElement(unittest.TestCase):

    def test_get_code_element(self):
        code: str = 'code_function()'
        element = get_code_element(code)
        
        self.assertEqual(element.type, ReportElementTypes.CODE)
        self.assertIn('<pre><code class="python">code_function()</code></pre>', element.body_content)            
        self.assertTrue(element.body_content.startswith('<div class="grid_12">'))
        self.assertTrue(element.body_content.endswith('</div>'))

    def test_empty_code(self):
        code: str = ''
        element = get_code_element(code)
        
        self.assertEqual(element.type, ReportElementTypes.CODE)
        self.assertIn('<pre><code class="python"></code></pre>', element.body_content)            
        self.assertTrue(element.body_content.startswith('<div class="grid_12">'))
        self.assertTrue(element.body_content.endswith('</div>'))

    def test_code_with_special_characters(self):
        code: str = '<>&"\''
        element = get_code_element(code)
        
        self.assertEqual(element.type, ReportElementTypes.CODE)
        self.assertIn('<pre><code class="python"><>&"\'</code></pre>', element.body_content)            
        self.assertTrue(element.body_content.startswith('<div class="grid_12">'))
        self.assertTrue(element.body_content.endswith('</div>'))

if __name__ == '__main__':
    unittest.main()