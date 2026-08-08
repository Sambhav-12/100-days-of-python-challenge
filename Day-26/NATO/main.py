import pandas

data = pandas.read_csv("Day-26/NATO/nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

words = input("Enter the word: ").replace(" ", "").upper()
print(words)
phonetic_list = [nato_dict[word] for word in words ]
print(phonetic_list)
