from broker import Broker
from components import ComponentA, ComponentB

def main():
    broker = Broker()
    component_a = ComponentA(broker)
    component_b = ComponentB(broker)

    # Publish an event
    broker.publish('event', 'Hello', name='John')

if __name__ == '__main__':
    main()