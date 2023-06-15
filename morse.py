morse_dict = { 'A':'.-', 'B':'-...',
                'C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....',
                'I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.',
                'O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-',
                'U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..',
                '1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....',
                '7':'--...', '8':'---..', '9':'----.',
                '0':'-----', ', ':'--..--', '.':'.-.-.-',
                '?':'..--..', '/':'-..-.', '-':'-....-',
                '(':'-.--.', ')':'-.--.-' 
            }


print("##  WELCOME to Python Morse code converter  ##")
print("*"*46 + "\n")

def converter(text):
    encrypted = ""
    if len(text) == 0:
        print("[ERROR]  you should enter some text to convert")
        converter()
    else:
        text = text.upper()
        for c in text:
            if c not in morse_dict.keys():
                encrypted += c
            else:
                encrypted += morse_dict[c]
        print(f"Your converted text:\n {encrypted}")

while True:
    user_input = input("Enter your text: ")
    converter(user_input)
    ans = input("Do you want to encrypt another text? y \ n : ")
    if ans.lower() == 'y':
        continue
    else:
        print("Bye")
        break

    
    

