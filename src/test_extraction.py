import unittest
from extraction import *

class Test_Extraxtion(unittest.TestCase):
    def test_heading_extraction(self):
        heading = extract_title("# Hello")
        self.assertEqual("Hello", heading)

    def test_heading_extraction_multiple_blocks(self):
        heading = extract_title('''
```this is some code```
                                
                                ### This is an h3


                                    # This is the h1!       

                                some paragraph
        ''')
        self.assertEqual("This is the h1!", heading)
