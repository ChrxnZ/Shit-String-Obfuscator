from base64 import b64encode as bencode
from cryptography.fernet import Fernet as fern
import rsa as RSA
list = [" ","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "×", "÷", "=", "/", "_", "€", "£", "¥", "₩", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "'", '"', ":", ";", ",", "?", "`", "~", "|", "<", ">", "{", "}", "[", "]", "°", "•", "○", "●", "□", "■", "♤", "♡", "◇", "♧", "☆", "▪︎", "¤", "《", "》", "¡", "¿", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "×", "÷", "=", "/", "_", "€", "£", "¥", "₩", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "'", '"', ":", ";", ",", "?", "`", "~", "|", "<", ">", "{", "}", "[", "]", "°", "•", "○", "●", "□", "■", "♤", "♡", "◇", "♧", "☆", "▪︎", "¤", "《", "》", "¡", "¿"]


def generate_keys():
    (pubKey, privKey) = RSA.newkeys(1024)
    with open('keys/pubkey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    with open('keys/privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))

def load_keys():
    with open('keys/pubkey.pem', 'rb') as f:
        pubKey = RSA.PublicKey.load_pkcs1(f.read())

    with open('keys/privkey.pem', 'rb') as f:
        privKey = RSA.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey
    
def load(type):
	if type == 0:
		with open("keys/pubkey.pem", "rb") as f:
			pub = RSA.PublicKey.load_pkcs1(f.read())
	elif type == 1:
		with open("keys/privkey.pem", "rb") as f:
			pub = RSA.PrivateKey.load_pkcs1(f.read())

def encrypt(msg, key):
    return RSA.encrypt(msg.encode('utf-8'), key)

def decrypt(ciphertext, key):
    try:
        return RSA.decrypt(ciphertext, key).decode('utf-8')
    except:
        return False

def sign_sha1(msg, key):
    return RSA.sign(msg.encode('utf-8'), key, 'SHA-1')

def verify_sha1(msg, signature, key):
    try:
        return RSA.verify(msg.encode('utf-8'), signature, key) == 'SHA-1'
    except:
        return False
        
def get_shift(min, max):
	key = int(input("How many letters to shift to the right (Max is 114) >  "))
	if key < min:
		return print(f"{key} is lower than {min}, hereby making it useless to use.")
	elif key > max:
		return print(f"{key} is higher than {max}, hereby making it useless to use")
	else:
		return int(key)
		
def all(msg):
	generate_keys()
	pub, priv = load_keys()
	cipher = encrypt(msg, pub)
	sig = sign_sha1(msg, priv)
	c = verify_sha1(msg, b, priv)
	return cipher, sig, pub
		
def get_text():
		text = str(input("Enter text >  "))
		return text
		
def obfuscate(text, key):
	string = []
	obfuscated = []
	d = ""
	for i in range(len(text)):
		slice = text[i:i+1]
		string.append(slice)
	for char in string:
		index = list.index(char)
		obfuscation = list[index + key]
		obfuscated.append(obfuscation)
	obstringg = d.join(obfuscated)
	return str(obstringg)
	
def base():
	b64 = str(input("Encode in base64? (y/n) >  "))
	if b64 == "y" or b64 == "Y":
		result = 1
	else:
		result = 0
	return result
	
def fernet():
	fr = str(input("Encrypt with AES-128? (y/n) >  "))
	if fr == "y" or fr == "Y":
		result = 1
	else:
		result = 0
	return result 
	
def rsa():
	rsa = str(input("Encrypt with RSA-1024? (y/n) >  "))
	if rsa == "y" or rsa == "Y":
		result = 1
	else:
		result = 0
	return result
	
def extra(obfuscated, base64, fernet, rsa):
	if base64 == 1:
		bobfuscated = bytes(obfuscated, "utf-8")
		based = bencode(bobfuscated)
	elif base64 == 0:
		based = "N/A"
	if fernet == 1:
		key = fern.generate_key()
		with open("keys/fernet_key.key", "wb") as wr:
			wr.write(key)
		bobfuscated = bytes(obfuscated, "utf-8")
		encrypt = fern(key).encrypt(bobfuscated)
	elif fernet == 0:
		encrypt = "N/A"
	if rsa == 1:
		cipher, signature, pub = all(obfuscated)
		if verify_sha1(obfuscated, signature, pub):
			print("Signature verified")
	elif rsa == 0:
		cipher = "N/A"
		signature = "N/A"
	return based, encrypt, cipher, signature
	
def output(obfuscated, base, fernet, rsa, rsa_sig):
	print(f"""
Base64: {base}
Obfuscated: {obfuscated}
AES-128: {fernet}
RSA-1024: {rsa}
RSA-Signature: {rsa_sig}""")

def main():
	shift = get_shift(1, 114)
	text = get_text()
	obf = obfuscate(text, shift)
	qb = base()
	qf = fernet()
	qr = rsa()
	generate_keys()
	based, encrypt, cipher, signature = extra(obf, qb, qf, qr)
	output(obf, based, encrypt, cipher, signature)
if __name__ == '__main__':	
	main()
