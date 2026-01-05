# Program for getting phonetic spelling of a word

import pandas as pd
nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}

def get_nato_phonetic(word):
    clean_word = word.strip().upper()
    nato_list = [nato_alphabet_dict[letter] for letter in clean_word]
    print(f"\n {nato_list}")

def get_user_input():
    while True:
        try:
            word = input("\nEnter a word for its phonetic spelling: ")
            get_nato_phonetic(word)
        except KeyError:
            print("\nPlease enter only one word, letters only. Try again.")

        retry = input("\nWould you like to enter another word?(y/n): ")
        if retry.lower() != "y":
            print("\nThank you for using the nato alphabet. Goodbye.")
            break

get_user_input()

# Learning portion

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
