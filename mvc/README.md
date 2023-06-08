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

# Model-View-Controller (MVC)

This example demonstrates the Model-View-Controller (MVC) architectural pattern implemented with a user interface. 

The MVC pattern separates the application into three interconnected components: `Model`, `View`, and `Controller`. 

The user interface allows users to interact with the application, and the changes in the model are reflected in the view through the controller.

## Components

- **Model:**
    
    The Model represents the data and business logic of the application. It encapsulates the core functionality and maintains the state of the application. In this project, the `user.py` file represents the Model and defines the User class with its attributes and methods.

- **View:**

    The View is responsible for presenting the data to the users and rendering the user interface. It provides a visual representation of the Model's state. In this project, the `user_view.py` file represents the View and handles the console-based user interface for displaying user information.

- **Controller:**

    The Controller acts as an intermediary between the Model and the View. It receives user input from the View, updates the Model accordingly, and triggers the necessary updates in the View to reflect the changes. In this project, the `user_controller.py` file represents the Controller and manages the interactions between the Model and the View.

## Usage
To run the application, execute the `main.py` file:

```zsh
python3 main.py
```

The application will display a console-based user interface. 

Follow the on-screen instructions to interact with the application. You can create new users, view existing users, and update user information through the provided commands.

*Output*

```zsh
% python3 main.py
Enter a command (update, display, exit): display
User: Anna
Enter a command (update, display, exit): update
Enter the new name: Anya
Enter a command (update, display, exit): display
User: Anya
Enter a command (update, display, exit): exit
```

To `run tests`, execute the following command:

```zsh
python3 test.py
```