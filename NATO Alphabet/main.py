

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
def generate_phonetic():
    try:
        word = input("Enter a word: ").upper()
        output_list=[]
        for letter in word:
            if letter not in phonetic_dict[letter]:
                raise KeyError
                generate_phonetic()
            else:
                output_list.append(phonetic_dict[letter])
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(output_list)

generate_phonetic()
