import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
            print("Did you mean %s instead?" %get_close_matches(w,data.keys())[0])
            yn = input(" Type Y if Yes or N if No : ")
            if yn.lower()=="y":
                return data[get_close_matches(w, data.keys())[0]]
            elif yn.lower()=="n":
                return "The word doesn't exist. Please double check it."
            else:
                return "We didn't understand your input :("
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word : ")
output = translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)