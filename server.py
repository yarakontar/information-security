# from cryptography.fernet import Fernet
# import socket


# key = Fernet.generate_key()
# fernet = Fernet(key)


# server_socket = socket.socket()
# server_socket.bind(("127.1.0.10", 1345))
# server_socket.listen(5)
# print("Server is listening...")

# conn, addr = server_socket.accept()
# print("Connection from:", addr)

# conn.send(key)

# message = "Hello, client!"
# encrypted_message = fernet.encrypt(message.encode())
# conn.send(encrypted_message)

# conn.close()
import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# المفتاح المشترك (يجب مشاركته مع العميل بأمان)
shared_key = b'ThisIsASharedKey'

# إعداد الخادم
host = '127.0.0.1'
port = 12346

# إنشاء مولد عشوائي لل IV (Initialization Vector)
iv = get_random_bytes(16)

# إعداد المشفر باستخدام مفتاح المشترك و IV
cipher = AES.new(shared_key, AES.MODE_CFB, iv)

# انشاء السيرفر
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"hhhh {host}:{port}")
    conn, addr = server_socket.accept()

    with conn:
        print(f"tm{addr}")

        # الرسالة المراد إرسالها
        message = "This is a secret message."

        # تشفير الرسالة
        ciphertext = iv + cipher.encrypt(message.encode('utf-8'))

        # إرسال الرسالة المشفرة إلى العميل
        conn.sendall(ciphertext)
