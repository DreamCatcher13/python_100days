import string

def greeting():
    print("""* * * 
Welcome to Caesar Cipher.
Have fun. Don't forget your shift :)
* * *""")

alphabet = list(string.ascii_lowercase + string.digits + ".,:;!?@%")

def caesar(message, shift, action):
    result = []
    # from the course
    if action == "decrypt":
        shift *= -1
    #  
    for l in list(message):
        if l == ' ':
            result += l
            continue
        indx = alphabet.index(l)
        result += alphabet[(indx+shift)%len(alphabet)]
    return ''.join(result)

greeting()
action = input("Type 'encrypt', 'decrypt' or 'quit':\n").lower()
while  action != "quit":    
    if action not in ["encrypt", "decrypt"]:
        print("Wrong action choice")
        action = input("Type 'encrypt', 'decrypt' or 'quit':\n").lower()
    message = input("Type your message:\n").lower()
    shift = input("Type the shift number\n")
    if message == '' or shift == '':
        print("Wrong input")
        action = 'quit'
        continue
    print(caesar(message, int(shift), action))
    action = input("Type 'encrypt', 'decrypt' or 'quit':\n").lower()