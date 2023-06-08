class ComponentB:
    def __init__(self, broker):
        self.broker = broker
        self.broker.subscribe('event', self.handle_event)

    def handle_event(self, *args, **kwargs):
        print('Component B handling event:', args, kwargs)