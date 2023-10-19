from cryptography.fernet import Fernet
import socket


key = Fernet.generate_key()
fernet = Fernet(key)


server_socket = socket.socket()
server_socket.bind(("127.1.0.10", 1345))
server_socket.listen(5)
print("Server is listening...")

conn, addr = server_socket.accept()
print("Connection from:", addr)

conn.send(key)

message = "Hello, client!"
encrypted_message = fernet.encrypt(message.encode())
conn.send(encrypted_message)

conn.close()