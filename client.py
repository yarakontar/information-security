from cryptography.fernet import Fernet
import socket

# العميل يستلم المفتاح المشترك من السيرفر
client_socket = socket.socket()
client_socket.connect(("127.0.0.10", 1345))

key = client_socket.recv(1024)
fernet = Fernet(key)

data = client_socket.recv(1024)
decrypted_message = fernet.decrypt(data)

print("Received:", decrypted_message.decode())
client_socket.close()