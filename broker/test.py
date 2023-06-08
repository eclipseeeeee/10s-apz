import unittest
from unittest.mock import patch, MagicMock
from broker import Broker
from components import ComponentA, ComponentB


class TestBrokerPattern(unittest.TestCase):
    def test_broker_subscribe(self):
        broker = Broker()
        callback_a = lambda: None
        callback_b = lambda: None

        broker.subscribe('event', callback_a)
        broker.subscribe('event', callback_b)

        self.assertEqual(len(broker.subscribers['event']), 2)
        self.assertIn(callback_a, broker.subscribers['event'])
        self.assertIn(callback_b, broker.subscribers['event'])

    def test_broker_publish(self):
        broker = Broker()
        callback_a = MagicMock()
        callback_b = MagicMock()

        broker.subscribe('event', callback_a)
        broker.subscribe('event', callback_b)

        component_a = ComponentA(broker)
        component_b = ComponentB(broker)

        broker.publish('event')

        callback_a.assert_called_once_with()
        callback_b.assert_called_once_with()

    def test_component_a_handle_event(self):
        component_a = ComponentA(Broker())
        with patch('builtins.print') as mock_print:
            component_a.handle_event('Hello', name='John')
            mock_print.assert_called_with('Component A handling event:', ('Hello',), {'name': 'John'})

    def test_component_b_handle_event(self):
        component_b = ComponentB(Broker())
        with patch('builtins.print') as mock_print:
            component_b.handle_event('Hello', name='John')
            mock_print.assert_called_with('Component B handling event:', ('Hello',), {'name': 'John'})


if __name__ == '__main__':
    unittest.main()
