import os
import base64

filepath = "./storage/"


def morse(pswrd):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    morse_code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-',
                  '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', 
                  '.--', '-..-', '-.--', '--..']
    mapping = {letter: code for letter, code in zip(alphabet, morse_code)}

    pswrd = pswrd.upper()
    encrypted = ''.join(mapping[char] + " " if char in mapping else "/" if char == " " else char for char in pswrd)
    return encrypted

def caesar(pswrd, shift=7):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted = alphabet[shift:] + alphabet[:shift]
    mapping = {letter: shifted[i] for i, letter in enumerate(alphabet)}

    pswrd = pswrd.upper()
    encrypted = ''.join(mapping[char] if char in mapping else char for char in pswrd)
    return encrypted


def obfuscate(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def deobfuscate(text):
    return base64.b64decode(text).decode('utf-8')


def add():
    name = input("Name: ")
    password = input("Password: ")
    encrypt = int(input("Caesar(1) Morse(2) Base64(3): "))

    file_path = os.path.join(filepath, obfuscate(name))
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    with open(file_path, "w") as file:
        if encrypt == 1:
            file.write(caesar(password))
        elif encrypt == 2:
            file.write(morse(password))
        elif encrypt == 3:
            file.write(obfuscate(password))
        else:
            print("Invalid encryption type selected.")


def browse():
    if not os.path.exists(filepath):
        print("No storage directory found.")
        return

    for filename in os.listdir(filepath):
        try:
            
            decoded_name = deobfuscate(filename)
            full_path = os.path.join(filepath, filename)
            
            with open(full_path, "r") as file:
                encrypted_password = file.read()
                print(f"Username: {decoded_name}")
                print(f"Encrypted Password: {encrypted_password}")
                
                
                decrypted_password = decrypt(encrypted_password)
                print(f"Decrypted Password: {decrypted_password}")
                print("-" * 30)
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    input("Press any key to exit:")



def delete():
    file = input("Enter username to delete: ")
    file_path = os.path.join(filepath, obfuscate(file))

    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted.")
    else:
        print("File not found.")

def decrypt(pswrd):
    method = int(input("Decryption method: Caesar(1), Morse(2), Base64(3): "))

    if method == 1:
        shift = 7
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        shifted = alphabet[shift:] + alphabet[:shift]
        mapping = {shifted[i]: alphabet[i] for i in range(len(alphabet))}
        decrypted = ''.join(mapping[char] if char in mapping else char for char in pswrd)
        return decrypted
    elif method == 2:
        morse_to_alpha = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', 
                          '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', 
                          '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', 
                          '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', 
                          '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', 
                          '--..': 'Z'}
        decrypted = ''.join(morse_to_alpha[char] if char in morse_to_alpha else " " if char == "/" else char for char in pswrd.split())
        return decrypted
    elif method == 3:
        try:
            return deobfuscate(pswrd)
        except Exception as e:
            return f"Error decoding Base64: {e}"
    else:
        return "Invalid decryption method."
