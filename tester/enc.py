from passlib.context import CryptContext
import hashlib
import base64

def sha512_base64(input_string):
    # SHA-512 해시 생성
    sha512_hash = hashlib.sha512(input_string.encode()).digest()
    # Base64로 인코딩
    base64_encoded = base64.b64encode(sha512_hash).decode()
    return base64_encoded


input='14tks0225!'
print('input : ',input)
print('pw: ',sha512_base64(input))