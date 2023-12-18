


import base64
import time
from Crypto.Cipher import AES

# 设置偏移量
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def pkcs7_padding(data, blocksize=32):
    length = len(data)
    pad = blocksize - (length % blocksize)
    data = data + chr(pad) * pad
    return data.encode('ascii')


# 加密函数
def encrypt():
    text = str(time.time()).split('.')[0]
    key = 'GtoBDQxYXdn1rSxd'.encode('utf-8')
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, key)
    text = pkcs7_padding(text, 16)
    cipher_text = cryptos.encrypt(text)
    return base64.b64encode(cipher_text)

#rsa加密
def rsa_encrypt(pub_key:str,msg:str):
    public_key = f"""-----BEGIN PUBLIC KEY-----
    {pub_key}
    -----END PUBLIC KEY-----
    """
    en_msg = bytes(msg, encoding="utf8")
    rsakey = RSA.importKey(public_key)
    cipher = PKCS1_v1_5.new(rsakey)
    abc = cipher.encrypt(en_msg)
    return  str(base64.b64encode(abc),"utf8")