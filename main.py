import json


with open('templates/dictionary.json') as f:
   data = json.load(f)

with open('text.txt','r') as file:
   
    for line in file:
   
        for word in line.split():
   
            try:
                translate = data[word]
                print(translate)
            except:
                print(word)
