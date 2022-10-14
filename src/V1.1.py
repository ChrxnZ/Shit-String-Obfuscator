# shitty obfuscator
from base64 import b64encode as encode
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] #alphabet written 2 times to support shifting up to 24 letters to the right

    
key = int(input("How many letters to shift to the right? >  "))
if key > 24:
    print("Max shifting amount is 24")
elif key < 1:
    print("Min shifting amount is 1")
else:
    string = []
    chars = int(input("How many chars? >  "))
    if chars == 3:
        st = input("3 char word >  ")
        base = input("Encode in base64? (y/n) >  ")
        st1 = st[0:1]
        st2 = st[1:2]
        st3 = st[2:3]
        string.append(st1)
        string.append(st2)
        string.append(st3)

    obf = []
    obfsc = []

    for char in string:
        ab = list.index(char)
        obf.append(char)
        obfs = list[ab + key]
        obfsc.append(obfs)
    obfus = f"{obfsc[0]}{obfsc[1]}{obfsc[2]}"
    if base == "y":
        bs = encode(obfus.encode("utf-8"))
        stz = str(bs, "utf-8")
        print(f"Obfuscated: " + stz)
    else:
        print(obfus)
        print(st)   
