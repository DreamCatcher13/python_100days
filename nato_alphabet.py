import pandas

nato_alp = pandas.read_csv("data\\nato_alp.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alp.iterrows()}

def generate_phonetic():
    word = input("Enter your word: ")
    try:
        result = [nato_dict[f"{l}"] for l in word.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
