import unittest
from event_bus import EventBus

class TestEventBus(unittest.TestCase):
    def setUp(self):
        self.event_bus = EventBus()

    def test_publish_subscribe(self):
        event_data = {'name': 'John Doe'}
        received_data = {}

        def event_handler(data):
            nonlocal received_data
            received_data = data

        # Subscribe to the event
        self.event_bus.subscribe('user_created', event_handler)

        # Publish the event
        self.event_bus.publish('user_created', event_data)

        # Check if the event handler received the correct data
        self.assertEqual(received_data, event_data)

    def test_unsubscribe(self):
        event_data = {'name': 'John Doe'}
        received_data = {}

        def event_handler(data):
            nonlocal received_data
            received_data = data

        # Subscribe to the event
        subscription_id = self.event_bus.subscribe('user_created', event_handler)

        # Unsubscribe from the event
        self.event_bus.unsubscribe(subscription_id)

        # Publish the event
        self.event_bus.publish('user_created', event_data)

        # Check if the event handler did not receive any data
        self.assertEqual(received_data, {})

    def test_multiple_subscribers(self):
        event_data = {'name': 'John Doe'}
        received_data_1 = {}
        received_data_2 = {}

        def event_handler_1(data):
            nonlocal received_data_1
            received_data_1 = data

        def event_handler_2(data):
            nonlocal received_data_2
            received_data_2 = data

        # Subscribe both event handlers to the event
        self.event_bus.subscribe('user_created', event_handler_1)
        self.event_bus.subscribe('user_created', event_handler_2)

        # Publish the event
        self.event_bus.publish('user_created', event_data)

        # Check if both event handlers received the correct data
        self.assertEqual(received_data_1, event_data)
        self.assertEqual(received_data_2, event_data)

if __name__ == '__main__':
    unittest.main()
