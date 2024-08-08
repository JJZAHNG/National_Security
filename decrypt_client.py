import socket


def start_decrypt_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Enter server IP address: ")
    server_port = 12345
    client_socket.connect((server_ip, server_port))

    while True:
        encrypted_message = client_socket.recv(1024).decode()
        if encrypted_message.lower() == 'exit':
            break
        print(f"Encrypted message from server: {encrypted_message}")
        decrypted_message = caesar_decrypt(encrypted_message, 3)  # 使用凯撒密码解密
        client_socket.send(decrypted_message.encode())

    client_socket.close()


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
    start_decrypt_client()
