# 生成rsa密钥
from Crypto.PublicKey import RSA

rsa_obj = RSA.generate(1024)
private_pem = rsa_obj.exportKey()  # pem格式输出私钥
public_key = rsa_obj.publickey()
public_pem = public_key.exportKey()  # 将公钥输出成pem格式
print(public_pem)
