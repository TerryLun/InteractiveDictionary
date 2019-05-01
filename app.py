import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def lookUp(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(),cutoff=0.8))>0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(word, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == "n":
            return "The Word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The Word doesn't exist. Please double check it."

word = input("Enter word: ")

output = lookUp(word)

if type(output) == list:
    index = 1
    for item in output:
        print(str(index) + ". " + item)
        index += 1
else:
    print(output)
