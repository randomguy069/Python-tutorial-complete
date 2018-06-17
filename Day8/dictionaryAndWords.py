import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json")) #the datatype of data will be a dictionary

def getMeaning(word):

        word = word.lower()#irrespective of what the user adds. This will make the word in lower case and then check for it
        if word in data:
            return data[word]
        elif word.capitalize() in data:
            return   data[word.capitalize()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(get_close_matches(word,data.keys())) > 0:  #condition present to check for the closest word based on similarity ratio between the word input and the data key
            print("Did you mean %s instead?" % get_close_matches(word,data.keys())[0])
            check = input ("Y or N?")
            if check == 'Y':
                return data[get_close_matches(word,data.keys())[0]]
            elif check == 'N':
                return "Word does not exist in our dictionary!"
            else:
                return "Please enter our choices only"
        else:
            return "Word does not exist in our dictionary!"


myWord = input("Enter your word -> ")
op = getMeaning (myWord)

if type(op) == list :
    for item in op:
        print (item)
else:
    print (op)
