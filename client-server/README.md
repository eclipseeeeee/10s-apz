# Client-Server Architecture

The Client-Server architecture is a common software architecture pattern where a client application communicates with a server over a network. The client sends requests to the server, and the server processes those requests and returns responses back to the client.

## Key Features of Client-Server Architecture

- **Client**: The client application initiates communication with the server by sending requests over a network. The client can be any software or device that interacts with the server to access services or resources.
- **Server**: The server application receives and processes client requests, performs necessary operations, and sends responses back to the client. It hosts services, resources, or data that the client can access.
- **Network Communication**: The client and server communicate over a network using predefined protocols such as HTTP, TCP/IP, or WebSocket. The communication can be synchronous or asynchronous, depending on the application requirements.
- **Scalability**: Client-Server architecture allows for scalable systems where multiple clients can concurrently communicate with the server. Servers can handle multiple client connections and distribute the workload efficiently.
- **Centralized Logic**: The server hosts the core logic, processes requests, and performs complex operations, enabling clients to be lightweight and focused on the user interface or presentation layer.

## Examples

In this repository, you will find the example that demonstrate the basic implementation of the Client-Server architecture using Python. The examples include a client application and a server application that communicate over HTTP.

- **client.py**: Implements the client-side logic for sending requests to the server and receiving responses.
- **server.py**: Implements the server-side logic for processing client requests and returning responses.

## Usage

1. Run the server:
    ```zsh
    python3 server
    ```
2. Run the client:
    ```zsh
    python3 client
    ```

*Output*:
```zsh
% python3 client
Current messages:
Response: Message sent
Updated messages:
- New message

% python3 client
Current messages:
- New message
Response: Message sent
Updated messages:
- New message
- New message
```

## Testing

To `run server tests`, execute the following command:
```zsh
python3 server/tests/test_server.py
```

To `run client tests`, execute the following command:
```zsh
python3 client/tests/test_client.py
```
