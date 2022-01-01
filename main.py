import json


with open('templates/dictionary.json') as f:
   data = json.load(f)

s = ""

with open('text.txt','r') as file:
   
    for line in file:
   
        for word in line.split():
   
            try:
                translate = data[word]
                s = s + " " + translate
            except:
                s = s + " " + word

print(s)
