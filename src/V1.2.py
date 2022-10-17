# shitty obfuscator
from base64 import b64encode as encode
from cryptography.fernet import Fernet as fern
import rsa
list = [" ","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "×", "÷", "=", "/", "_", "€", "£", "¥", "₩", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "'", '"', ":", ";", ",", "?", "`", "~", "|", "<", ">", "{", "}", "[", "]", "°", "•", "○", "●", "□", "■", "♤", "♡", "◇", "♧", "☆", "▪︎", "¤", "《", "》", "¡", "¿", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "×", "÷", "=", "/", "_", "€", "£", "¥", "₩", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "'", '"', ":", ";", ",", "?", "`", "~", "|", "<", ">", "{", "}", "[", "]", "°", "•", "○", "●", "□", "■", "♤", "♡", "◇", "♧", "☆", "▪︎", "¤", "《", "》", "¡", "¿"] #every char i could find on my keyboard lol / supports shifts up to 114 times to the right with optional base64 obfuscation 

def generate_keys():
    (pubKey, privKey) = rsa.newkeys(3072)
    with open('keys/pubkey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    with open('keys/privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))

def load_keys():
    with open('keys/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('keys/privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey

def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')

def verify_sha1(msg, signature, key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

    
key = int(input("How many letters to shift to the right? >  "))
if key > 114:
    print("Max shifting amount is 24")
elif key < 1:
    print("Min shifting amount is 1")
else:
    string = []
    obfuscated = []
    d = ""
    stinput = input("input text >  ")
    for i in range(len(stinput)):
        slice = stinput[i:i+1]
        string.append(slice)
    for char in string:
        ind = list.index(char)
        obfuscate = list[ind + key]
        obfuscated.append(obfuscate)
    obfstring = d.join(obfuscated)
    base = input("Encode in base64? (y/n) >  ")
    if base == "y":
        e = encode(obfstring.encode("utf-8"))
        based = str(e, "utf-8")
        fr = input("Encrypt using AES-128? (y/n) >  ")
        if fr == "y":
            fkey = fern.generate_key()
            with open("Encryption_Key.key", "wb") as keyw:
                keyw.write(fkey)
                print("Exported Encryption Key: ", str(fkey))
            obfs = bytes(obfstring, "utf-8")
            encrypt = fern(fkey).encrypt(obfs)
            print("Original: ", stinput)
            print("Obfuscated: ", obfstring)
            print("B64: ", based)
            print("Encrypted: ", str(encrypt))
        else:
           print("Original: ", stinput)
           print("Obfuscated: ", obfstring)
           print("B64: ", based)
    else:
        fr = input("Encrypt using AES-128? (y/n) >  ")
        if fr == "y":
            fkey = fern.generate_key()
            with open("Encryption_Key.key", "wb") as keyw:
                keyw.write(fkey)
                print("Exported Encryption Key: ", str(fkey))
            obfs = bytes(obfstring, "utf-8")
            encrypt = fern(fkey).encrypt(obfs)
            print("Original: ", stinput)
            print("Obfuscated: ", obfstring)
            print("Encrypted: ", str(encrypt))
        
        
