import json

data = json.load(open("data.json"))

def lookUp(word):    
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The Word doesn't exist. Please double check it."

word = input("Enter word: ")

print(lookUp(word))
