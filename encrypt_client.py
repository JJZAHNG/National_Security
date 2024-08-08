import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Received encrypted message: {message}")
                decrypted_message = caesar_decrypt(message, 3)  # 使用凯撒密码解密
                print(f"Decrypted message: {decrypted_message}")
        except:
            print("An error occurred.")
            client_socket.close()
            break


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Enter server IP address: ")
    server_port = 12345
    client_socket.connect((server_ip, server_port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Enter a message to encrypt (or 'exit' to quit): ")
        if message.lower() == 'exit':
            client_socket.send(message.encode())
            break
        encrypted_message = caesar_encrypt(message, 3)  # 使用凯撒密码加密
        client_socket.send(encrypted_message.encode())

    client_socket.close()


def caesar_encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result


def caesar_decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) - shift - 97) % 26 + 97)
    return result


if __name__ == "__main__":
    start_client()
