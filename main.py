# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd

nato_read = pd.read_csv("nato_phonetic_alphabet.csv")
nato_df = pd.DataFrame(nato_read)
nato_dict = {row["letter"]:row["code"] for (index, row) in nato_df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_nato_equi():
    word_input = input("Input a word to convert to NATO phonetic format: ").upper()

    try:
        nato_equivalent = [nato_dict[f"{letter}"] for letter in word_input]
    except KeyError:
        print("Sorry, only letters in the alphabet only.")
        generate_nato_equi()
    else:    
        print(nato_equivalent)


generate_nato_equi()