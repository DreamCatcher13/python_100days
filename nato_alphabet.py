import pandas

nato_alp = pandas.read_csv("data\\nato_alp.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alp.iterrows()}
word = input("Enter your word: ")
result = [nato_dict[f"{l}"] for l in word.upper()]
print(result)
