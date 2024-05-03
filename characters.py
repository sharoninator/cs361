import socket

with socket.socket() as server_socket:
    server_socket.bind(('localhost', 4546))
    server_socket.listen(1)
    print("Server is listening on port 4546...")

    while True:
        connection, _ = server_socket.accept()
        with connection:
            data = connection.recv(1024)
            if data:
                connection.sendall(str(len(data)).encode())
