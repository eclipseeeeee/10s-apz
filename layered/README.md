# Software Architecture: Kyiv Polytechnic Institute course

This repository consists of 10 most popular Software Architecture design patterns implemented in Python.

Each pattern has a simple Python implementation example with tests.

All examples are implemented in different branches.

## Patterns:

1. [**Layered Arhitecture**](https://github.com/annavasylashko/kpi-architecture/tree/layered-architecture)
2. [**Client-Server Architecture**](https://github.com/annavasylashko/kpi-architecture/tree/client-server)
3. [**Master-Slave Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/master-slave)
4. [**Pipe-Filter Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/pipe-filter)
5. [**Broker Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/broker)
6. [**Peer-to-Peer Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/peer-to-peer)
7. [**Event Bus Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/event-bus)
8. [**Model-View-Controller Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/mvc)
9. [**Blackboard Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/blackboard)
10. [**Interpreter Pattern**](https://github.com/annavasylashko/kpi-architecture/tree/interpreter)

---

# Layered Architecture Pattern

The Layered architecture pattern is a software design pattern that promotes the separation of concerns and modularization of an application. It divides the application into distinct layers, each responsible for a specific set of tasks. The typical layers include presentation, business logic, and data storage, although additional layers can be added as needed.

## Usage and Benefits

The Layered architecture pattern offers several benefits, including:

- **Modularity**: The separation of concerns into layers allows for easier maintenance, testing, and modification of individual components without affecting the entire system.
- **Scalability**: Each layer can be scaled independently, allowing for efficient resource allocation and performance optimization.
- **Reusability**: The modular nature of the pattern promotes code reuse as each layer can be developed and tested independently, making it easier to incorporate into other projects or extend functionality.
- **Separation of Concerns**: The pattern enforces a clear separation of concerns, making the codebase more manageable and easier to understand.

## Example

In this example, we demonstrate a simple implementation of the Layered architecture pattern in Python, consisting of the following layers:

- **Presentation Layer**: Handles user interactions and displays information to the user.
- **Business Logic Layer**: Encapsulates the core logic of the application.
- **Data Layer**: Responsible for data retrieval.

## Usage

To `run the example` and validate the pattern implementation, execute the following command:

```zsh
python3 main.py
```

*Output:*
```zsh
Data from the Business Logic Layer:
Item 1
Item 2
Item 3
```

To `run the test`, execute the following command:

```zsh
python3 ./tests/test_layered_architecture.py
```

The provided test case ensures that the data is correctly retrieved from the data layer, passed to the business logic layer, and displayed in the presentation layer.