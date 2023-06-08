# Peer-to-Peer Pattern

The peer-to-peer pattern enables direct communication and interaction among multiple peers in a decentralized manner. In this pattern, each peer can act as both a client and a server, allowing direct communication between peers without relying on a central server.

## Implementation

This implementation demonstrates a simplified Peer-to-Peer connection, that does not require any socket or http connection.
This is just a demonstration of Peer-to-Peer principles.

The implementation consists of a `Peer` class that represents a peer in the network. Each peer can establish connections with other peers and exchange messages.

### Peer Class

The Peer class provides the following functionality:

- `add_peer(peer)`: Asking for a connection with the specified peer.
- `establish_connection(peer)`: Establishing a connection with peer as requested, notifies if this connection is indeed established.
- `send_message(peer, message)`: Sends a message to the specified peer.
- `receive_message(peer, message)`: Receives a message from the specified peer.

## Usage

To demonstrate the peer-to-peer pattern, you can `run example` using
```zsh
python3 main.py
```

In this example, `peer1` establishes connections with `peer2` and `peer3` by calling the `add_peer` method. The method ensures that the connection is not already established before adding the peer to the list of connected peers.

Once the connections are established, peers can send messages to each other.

The `send_message` method sends a message from one peer to another by invoking the `receive_message` method on the recipient peer.

When a peer receives a message, it can process it in the `receive_message` method.

*Provided example*:
```python
peer1 = Peer("Peer 1")
peer2 = Peer("Peer 2")
peer3 = Peer("Peer 3")

peer1.add_peer(peer2)
peer1.add_peer(peer3)

peer1.send_message(peer2, "Hello")
peer2.send_message(peer1, "Hi there")
peer2.send_message(peer3, "Try hello")
```

*Output*
```zsh
Peer 1 is establishing a connection with Peer 2
Peer 2 accepted connection with Peer 1
Peer 2 is now connected to Peer 1
Peer 1 is now connected to Peer 2
Peer 1 is establishing a connection with Peer 3
Peer 3 accepted connection with Peer 1
Peer 3 is now connected to Peer 1
Peer 1 is now connected to Peer 3
Peer 2 received a message from Peer 1: Hello
Peer 1 received a message from Peer 2: Hi there
Peer 2 is not connected to Peer 3
```

This example demonstrates the exchange of messages between the connected peers. Each peer receives messages from other connected peers, allowing for direct communication and interaction.

To `run tests`, execute the following command:

```zsh
python3 test.py
```
