from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# توليد مفتاح عشوائي بطول 128 بت (16 بايت)
key = get_random_bytes(16)

# النص الذي ترغب في إرساله
message = "Hello, World!"

# توليد nonce (قيمة عشوائية) بنفس الطول الصحيح (16 بايت)
nonce = get_random_bytes(16)

# إعداد المفتاح
cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

# تشفير الرسالة
ciphertext, tag = cipher.encrypt_and_digest(message.encode())

# إرسال المفتاح والنص المشفر والتاغ (tag) إلى المستقبل (يمكن تنفيذها في السياق الحقيقي)
# في هذا المثال، سنقوم بطباعة القيم لأغراض توضيحية فقط
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Nonce:", nonce)
print("Tag:", tag.hex())