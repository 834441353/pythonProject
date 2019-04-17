from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

# rsa加密，通常对加密结果进行base64编码
def encrypt(public_key, message):
    cipher = Cipher_pkcs1_v1_5.new(public_key)
    cipher_text = base64.b64encode(cipher.encrypt(message))
    return cipher_text


# rsa解密
def decrypt(rsakey, encrypt_text):
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    return cipher.decrypt(base64.b64decode(encrypt_text), '')


public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrxFZRhHap1xNnVH2rV5Zj7Bvp
PpKzdQG+KB40/8vF7uYivD7AWmMRtL2t+xJzfkjw3ZuaPxdL3gEdtmJR/pZZTIIe
0YioccGFu/55aO4Ym7l4gPfB33TAy60s+j1ZuZ7KK5E5xLh6JfmcfIl0bRBaw959
4Nn1w7aM39VMiJ+B+wIDAQAB
-----END PUBLIC KEY-----"""
msg = 'hello world'
encrypt_text = encrypt(public_key, msg)
print(encrypt_text)

'''
goWbZ961d34RdEEgvJJtATAcAxXiY6QFTi7ToSmXQEyEKcHTNLqDdkzt3Iqwkhtfro4xCpLm4g+XqSQRNNN+3uQ9/Fahk6TZmi9eRcte5fU72jwyK6ybOAln8Chl8h14bjIsOAahmp9nuYdEFi7tV4ydNE75KMuAcHGlsJYTNjU=
'''

# text = decrypt(rsa_obj, encrypt_text)
# print(text)
# 'hello world'
