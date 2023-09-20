from stegano import lsb
import secrets
from Crypto.Cipher import DES

class Encryptor():
    def __init__(self) -> None:
        pass

    def __generate_key(self):
        return secrets.token_urlsafe(16)[0:8].encode('utf-8')
        
    def pad(self, text):
        while len(text) % 8 != 0:
            text += b' '

        return text
    
    # Encrypting file
    def encrypt(self, filepath: str, text:str):
        key = self.__generate_key()
        des = DES.new(key, DES.MODE_ECB)

        text = text.encode('utf-8')
        padded_text = self.pad(text)
        encrypted_text = des.encrypt(padded_text)

        file = lsb.hide(filepath, str(encrypted_text))
        file.save(filepath)

        return key.decode('utf-8')

    # Decripting file
    def decrypt(self, filepath: str, key: str):
        try:
            key = key.encode('utf-8')
            des = DES.new(key, DES.MODE_ECB)
            encrypted_text = eval(lsb.reveal(filepath))
            text = des.decrypt(encrypted_text).rstrip()

            return text.decode('utf-8')
        except:
            return False


if __name__ == '__main__':
    filepath = 'C:\\Users\\temat\\Desktop\\1.png'

    e = Encryptor()
    key = e.encrypt(filepath, 'Прикол')
    text = e.decrypt(filepath, key)

    print(text)
