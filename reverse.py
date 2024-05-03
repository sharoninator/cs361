import socket

with socket.socket() as server_socket:
    server_socket.bind(('localhost', 4545))
    server_socket.listen(1)
    print("Server is listening on port 4545...")

    while True:
        connection, _ = server_socket.accept()
        with connection:
            data = connection.recv(1024)
            if data:
                connection.sendall(data[::-1])
