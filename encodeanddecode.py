from cryptography.fernet import Fernet
import time
import os

text = ""

key = Fernet.generate_key()
fernet = Fernet(key)

enc_msg = fernet.encrypt(text.encode())
de_msg = fernet.decrypt(enc_msg).decode()

os.system('cls')
print("[+] Collecting Data.")
time.sleep(1)
os.system('cls')
print("[+] Collecting Data..")
time.sleep(1)
os.system('cls')
print("[+] Collecting Data...")
time.sleep(1)
os.system('cls')
print("[+] Collected Data.")
print()
print("· Original Text:", text)
print("· Encoded Text:", enc_msg)
print("· Decoded Text:", de_msg)