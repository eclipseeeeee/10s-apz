import unittest
from unittest import mock

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import server

class TestMessageService(unittest.TestCase):
    def setUp(self):
        server.MessageService.messages = ['Hello', 'World']

    def test_get_messages(self):
        messages = server.MessageService.get_messages()

        self.assertEqual(messages, ['Hello', 'World'])

    def test_add_message(self):
        message = 'Test message'

        initial_messages_count = len(server.MessageService.messages)
        server.MessageService.add_message(message)
        updated_messages_count = len(server.MessageService.messages)

        self.assertEqual(updated_messages_count, initial_messages_count + 1)
        self.assertEqual(server.MessageService.messages[-1], message)


if __name__ == '__main__':
    unittest.main()