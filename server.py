import socket
import threading

clients = []


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message.lower() == 'exit':
                clients.remove(client_socket)
                client_socket.close()
                break
            print(f"Received encrypted message: {message}")
            broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break


def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)
                client.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '0.0.0.0'
    server_port = 12345
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"Server started at {socket.gethostbyname(socket.gethostname())}:{server_port}, waiting for clients to connect...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established!")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
