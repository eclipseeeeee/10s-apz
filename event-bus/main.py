from event_bus import EventBus

def main():
    # Create an instance of the Event Bus
    event_bus = EventBus()

    # Define event types
    EVENT_USER_CREATED = 'user_created'
    EVENT_ORDER_PLACED = 'order_placed'

    # Subscriber functions
    def handle_user_created(user_data):
        print(f"User created: {user_data['name']}")

    def handle_order_placed(order_data):
        print(f"Order placed: {order_data['id']}")

    # Subscribe to events
    event_bus.subscribe(EVENT_USER_CREATED, handle_user_created)
    event_bus.subscribe(EVENT_ORDER_PLACED, handle_order_placed)

    # Publish events
    event_bus.publish(EVENT_USER_CREATED, {'name': 'John Doe'})
    event_bus.publish(EVENT_ORDER_PLACED, {'id': '123456'})

if __name__ == "__main__":
    main()