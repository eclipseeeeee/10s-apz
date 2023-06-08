from client import Client

client = Client()

def main():
    # Get the current messages
    messages = client.get_messages()
    if messages is not None:
        print("Current messages:")
        for message in messages:
            print("-", message)
    else:
        print("Failed to get messages.")

    # Send a new message
    response = client.post_message("New message")
    if response is not None:
        print("Response:", response)
    else:
        print("Failed to send message.")

    # Get the updated messages
    messages = client.get_messages()
    if messages is not None:
        print("Updated messages:")
        for message in messages:
            print("-", message)
    else:
        print("Failed to get messages.")


if __name__ == '__main__':
    main()