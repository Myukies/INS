def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted_text += char
    
    return encrypted_text

text = input("Enter the text to encrypt: ")
shift = 3
print("Text:", text)
print("Cipher:", encrypt(text, shift))
