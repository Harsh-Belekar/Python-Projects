import pandas

data=pandas.read_csv("./Assets/nato_phonetic_alphabet.csv")

data_dic={ row.letter: row.code for (index,row) in data.iterrows()}

def generate_nato():
    word=input("Enter a Word: ").upper()
    try:
        nato_word=[data_dic[letter] for letter in word ]

    except KeyError:
        print("Please Enter Letters in Alphabets.")
        generate_nato()

    else:
        print(nato_word)

generate_nato()