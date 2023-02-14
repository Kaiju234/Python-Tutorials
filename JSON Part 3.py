import json 



with open('person.json', 'r') as f:
    person = json.load(f)
    print(person)