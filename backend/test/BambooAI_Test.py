import unittest
from BambooAi import generate_branding_snippet, generate_keywords
from BambooAi_api import validate_input_length

class TestGenerateMethods(unittest.TestCase):

    def test_length(self):
        self.assertTrue(validate_input_length(22))

        generate_branding_snippet
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
