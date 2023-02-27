import string

def greeting():
    print("""* * * 
Welcome to Caesar Cipher.
Have fun. Don't forget your shift :)
* * *""")

alphabet = list(string.ascii_lowercase + string.digits + ".,:;!?@%")

def encrypt(message, shift):
    encrypted = []
    for l in list(message):
        if l == ' ':
            encrypted += l
            continue
        indx = alphabet.index(l)
        encrypted += alphabet[(indx+shift)%len(alphabet)]
    return ''.join(encrypted)

def decrypt(message, shift):
    decrypted = []
    for l in list(message):
        if l == ' ':
            decrypted += l
            continue
        indx = alphabet.index(l)
        decrypted += alphabet[(indx-shift)%len(alphabet)]
    return ''.join(decrypted)


greeting()
action = input("Type 'encrypt', 'decrypt' or 'quit':\n").lower()
while  action != "quit":
    message = input("Type your message:\n").lower()
    shift = input("Type the shift number\n")
    if message == '' or shift == '':
        print("Wrong input")
        action = 'quit'
        continue
    if action == 'encrypt':
        print(encrypt(message, int(shift)))
    elif action == 'decrypt':
        print(decrypt(message, int(shift)))
    else:
        print("Wrong action choice")
        action = 'quit'
    action = input("Type 'encrypt', 'decrypt' or 'quit':\n").lower()