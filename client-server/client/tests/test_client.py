import unittest
from unittest import mock

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import Client


class TestClient(unittest.TestCase):
    @mock.patch('urllib.request.urlopen')
    def test_get_messages(self, mock_urlopen):
        expected_messages = ['Hello']
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value.decode.return_value = '[' + ', '.join('"' + msg + '"' for msg in expected_messages) + ']'
        mock_urlopen.return_value = mock_response

        client = Client()
        messages = client.get_messages()

        self.assertEqual(messages, expected_messages)
        mock_urlopen.assert_called_once()

    @mock.patch('urllib.request.urlopen')
    def test_get_messages_empty(self, mock_urlopen):
        expected_messages = []
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value.decode.return_value = '[]'
        mock_urlopen.return_value = mock_response

        client = Client()
        messages = client.get_messages()

        self.assertEqual(messages, expected_messages)
        mock_urlopen.assert_called_once()

    @mock.patch('urllib.request.urlopen')
    def test_post_message(self, mock_urlopen):
        expected_message = 'New message'
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_urlopen.return_value = mock_response

        client = Client()
        response = client.post_message(expected_message)

        self.assertEqual(response, 'Message sent')
        mock_urlopen.assert_called_once()

    @mock.patch('urllib.request.urlopen')
    def test_post_message_error(self, mock_urlopen):
        expected_message = 'New message'
        mock_response = mock.Mock()
        mock_response.status = 500
        mock_urlopen.return_value = mock_response

        client = Client()
        response = client.post_message(expected_message)

        self.assertIsNone(response)
        mock_urlopen.assert_called_once()


if __name__ == '__main__':
    unittest.main()
