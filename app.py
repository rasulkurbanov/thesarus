import json
from difflib import get_close_matches

f = open("data.json")
some_data = f.read()
data = json.loads(some_data)


def give_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    if len(get_close_matches(word, data.keys())) > 0:
        answer = input(
            f"Did you mean {get_close_matches(word, data.keys())[0]} instead of {word}. If so enter Y, otherwise N: ")
        if answer == "Y" or answer == "y":
            for found_word in data[get_close_matches(word, data)[0]]:
                return found_word
        elif answer == "N" or answer == "n":
            return "Please checkout the word one more"
        else:
            return "Unfortunately, this word does not exist"
    else:
        return "Can not find the word or no this kind of word. Please check it out"


input_word = input("Enter the searching word: ")


print(give_definition(input_word))
