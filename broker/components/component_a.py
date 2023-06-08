class ComponentA:
    def __init__(self, broker):
        self.broker = broker
        self.broker.subscribe('event', self.handle_event)

    def handle_event(self, *args, **kwargs):
        print('Component A handling event:', args, kwargs)