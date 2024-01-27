import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.60.246', 8889))  # Replace '192.168.x.x' with the server's local IP
server.listen(1)

print("Server listening on 192.168.60.246:8889...")

while True:
    client_socket, client_address = server.accept()
    print(f"Connection from {client_address} has been established.")

    while True:
        message = client_socket.recv(1024).decode()

        if not message:
            break

        # Check for spam (basic pattern matching)
        spam_keywords = ['buy now', 'discount', 'limited offer', 'act fast', 'limited time only','free', 'gifts','hurry up', 'buy two get one free', 'prize pool', 'lucky amount', 'never miss', 'exclusive deal', 'amazing offer', 'cash prize', 'earn money', 'make money fast']  # Your spam keywords here
        is_spam = any(keyword in message.lower() for keyword in spam_keywords)

        # Respond based on spam detection
        if is_spam:
            response = "Suspected Spam!:("
        else:
            response = "Free of spam!:)"

        client_socket.send(response.encode())

    client_socket.close()
