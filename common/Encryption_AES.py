from Crypto.Cipher import AES
import base64
import hashlib


def encrypt(plain_text, key):
    """
    加密算法
    """
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = cipher.encrypt(padded_text)
    encoded_text = base64.b64encode(encrypted_text)
    return encoded_text


def decrypt(encoded_text, key):
    """
    解密算法
    """
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_text = base64.b64decode(encoded_text)
    decrypted_text = cipher.decrypt(encrypted_text)
    unpadded_text = unpad(decrypted_text)
    return unpadded_text


def pad(text):
    padding_size = AES.block_size - len(text) % AES.block_size
    padding = chr(padding_size).encode('utf-8') * padding_size
    padded_text = text.encode('utf-8') + padding
    return padded_text


def unpad(text):
    padding_size = text[-1]
    unpadded_text = text[:-padding_size]
    return unpadded_text


def md5_encode(text):
    """
    md5加密，32位小数
    """
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    encode_text = md5_hash.hexdigest()
    # encode('utf-8') 以字节形式返回参数
    return encode_text.encode('utf-8')


if __name__ == '__main__':
    key = b'd0965c07d1a00fcc85d28b8a241ae35a'
    a = "zhb"
    encrypted_username = encrypt(a, key)
    # 解密并传输给登录接口
    decrypted_username = decrypt(encrypted_username, key)
    print("加密数据:", encrypted_username)


