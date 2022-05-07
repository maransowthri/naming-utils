from distutils import extension
import unittest

from file_utils import unique_name_with_ts, unique_names_with_ts


class TestFileUtils(unittest.TestCase):
    def test_unique_name_with_ts(self):
        for path, extension in zip(['', 'prod', 'dev'], ['', 'log', 'txt']):
            filename = unique_name_with_ts(path, extension)
            self.assertTrue(filename)
            self.assertGreaterEqual(len(filename), 20)
            self.assertTrue(filename.endswith(extension))
            self.assertTrue(filename.startswith(path))
        
        self.assertRaises(TypeError, unique_name_with_ts, 1, 'txt')
        self.assertRaises(TypeError, unique_name_with_ts, ['prod'], 'txt')
        self.assertRaises(TypeError, unique_name_with_ts, 'prod', 1)
        self.assertRaises(TypeError, unique_name_with_ts, 'prod', ['log'])
    
    def test_unique_names_with_ts(self):
        for count, path, extension in zip([1, 10], ['', 'dev'], ['', 'log']):
            filenames = unique_names_with_ts(count, path, extension)
            self.assertEqual(len(filenames), count)
        
        self.assertRaises(TypeError, unique_names_with_ts, '1', 'prod', 'log')
        self.assertRaises(ValueError, unique_names_with_ts, 0, 'prod', 'log')