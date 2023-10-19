# from cryptography.fernet import Fernet
# import socket

# # العميل يستلم المفتاح المشترك من السيرفر
# client_socket = socket.socket()
# client_socket.connect(("127.0.0.10", 1345))

# key = client_socket.recv(1024)
# fernet = Fernet(key)

# data = client_socket.recv(1024)
# decrypted_message = fernet.decrypt(data)

# print("Received:", decrypted_message.decode())
# client_socket.close()


import socket
from Crypto.Cipher import AES

# المفتاح المشترك (يجب مشاركته مع الخادم بأمان)
shared_key = b'ThisIsASharedKey'

# إعداد العميل
host = '127.0.0.1'
port = 12346

# انشاء العميل
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((host, port))

    # استقبال الرسالة المشفرة من الخادم
    received_data = client_socket.recv(1024)

    # ال IV هو الجزء الأول من البيانات المستلمة
    iv = received_data[:16]

    # البيانات المشفرة بعد ال IV
    ciphertext = received_data[16:]

    # إعداد المشفر باستخدام المفتاح المشترك و IV
    cipher = AES.new(shared_key, AES.MODE_CFB, iv)

    # فك تشفير الرسالة
    decrypted_message = cipher.decrypt(ciphertext).decode('utf-8')

    print("yyy:", decrypted_message)