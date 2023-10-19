from Crypto.Cipher import AES

# المفتاح المستخدم لفك التشفير، يجب أن يكون مشتركًا مع المرسل
key = b'\xda\xfez\xb1\xfd\x80\xab\x82\x8e\xeb\xb93\x17\xa9F\x12'  # استبدل بالمفتاح الصحيح

# النص المشفر المقروء من الملف
ciphertext = b'`\xe4\xd7\x8d\xaf\xa6;\xa0\xa4\x87\x10R\xda'
tag= 'a3bed15d713fb737ab75f15efe21a9fc'

# إعداد المفتاح
cipher = AES.new(key, AES.MODE_EAX, nonce=  b'\x82?]\xa5\x8e\xb61\x14\x9b\x1d\\\x9a\xfe\xd9=\x18')  # استبدل القيمة nonce بالقيمة الصحيحة

# فك التشفير
try:
    
  decrypted_message = cipher.decrypt_and_verify(ciphertext)
  print("Decrypted Message:",decrypted_message.decode())
except ValueError:
  print("Decryption failed")
