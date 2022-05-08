import unittest

from src.naming_utils import unique_name_with_ts, unique_names_with_ts


class TestNamingUtils(unittest.TestCase):
    def test_unique_name_with_ts(self):
        for path, extension in zip(['', 'prod', 'dev'], ['', 'log', 'txt']):
            name = unique_name_with_ts(path, extension)
            self.assertTrue(name)
            self.assertGreaterEqual(len(name), 20)
            self.assertTrue(name.endswith(extension))
            self.assertTrue(name.startswith(path))
        
        self.assertRaises(TypeError, unique_name_with_ts, 1, 'txt')
        self.assertRaises(TypeError, unique_name_with_ts, ['prod'], 'txt')
        self.assertRaises(TypeError, unique_name_with_ts, 'prod', 1)
        self.assertRaises(TypeError, unique_name_with_ts, 'prod', ['log'])
    
    def test_unique_names_with_ts(self):
        for count, path, extension in zip([1, 10], ['', 'dev'], ['', 'log']):
            names = unique_names_with_ts(count, path, extension)
            self.assertEqual(len(names), count)
        
        self.assertRaises(TypeError, unique_names_with_ts, '1', 'prod', 'log')
        self.assertRaises(ValueError, unique_names_with_ts, 0, 'prod', 'log')