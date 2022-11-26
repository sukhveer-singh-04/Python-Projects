def encrypt(txt, s):  
    result = ""  
  
# transverse the plain txt  
    for i in range(len(txt)):  
        char = txt[i]  
        # encypt_func uppercase characters in plain txt  
  
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)  
        # encypt_func lowercase characters in plain txt  
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result  
  
txt = input("Enter the plain text:")

Shift = int(input("Enter the sift by value:"))

  
print("Plain txt : " + txt)  
print("Shift pattern : " + str(Shift))  
print("Cipher: " + encrypt(txt, Shift))  
