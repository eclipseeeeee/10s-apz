# Event Bus Pattern

The Event Bus pattern is a messaging pattern that facilitates communication between components using an event-based publish/subscribe model. 

It promotes loose coupling and enables components to communicate through the exchange of events. In this pattern, components can subscribe to specific events and receive notifications when those events are published.

## Key Components
- Event Bus: The central component that manages the event publication and subscription process. It acts as a mediator between the publishers and subscribers, routing events to the appropriate subscribers.

- Publishers: Components or modules that generate and publish events to the Event Bus. They provide the necessary data and context for the events.

- Subscribers: Components or modules that register with the Event Bus to receive notifications when specific events occur. They define event handlers or callbacks to process the received events.

## Usage

- Event Bus Setup: Create an instance of the Event Bus, which will serve as the central messaging component.

- Publish Events: Components that generate events can publish them to the Event Bus. They specify the event type and provide any required data or context.

- Subscribe to Events: Components interested in specific events can subscribe to them on the Event Bus. They register event handlers or callbacks to be invoked when the subscribed events occur.

- Handle Events: When an event is published on the Event Bus, the subscribers' event handlers or callbacks are invoked, allowing them to react to the event.

Example (**`main.py`**):

```python
from event_bus import EventBus

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
```

To `run the example`, execute the following command:

```zsh
python3 main.py
```

*Output*:

```zsh
% python3 main.py
User created: John Doe
Order placed: 123456
```

To `run the tests`, execute the following command:
```zsh
python3 test.py
```

## When to Use the Event Bus Pattern
- When you want to decouple components and establish communication through events.
- When you need to handle notifications, asynchronous updates, or data propagation between components.
- When you want to introduce flexibility and scalability in your system by allowing new components to subscribe to existing events or introduce new events without affecting existing components.