import unittest
from filters import uppercase, reverse

from main import run_pipe_filter


class TestPipeFilter(unittest.TestCase):
    def test_filter_uppercase(self):
        input_data = 'hello, world!'
        expected_output = 'HELLO, WORLD!'
        result = uppercase(input_data)
        self.assertEqual(result, expected_output)

    def test_filter_reverse(self):
        input_data = 'Hello, World!'
        expected_output = '!dlroW ,olleH'
        result = reverse(input_data)
        self.assertEqual(result, expected_output)

    def test_run_pipe_filter(self):
        input_data = 'hello, world!'
        expected_output = '!DLROW ,OLLEH'
        result = run_pipe_filter(input_data)
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
