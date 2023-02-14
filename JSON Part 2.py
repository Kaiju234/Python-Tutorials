import json
person_json = """
{
    "age": 18, 
    "city": "Panama City",
    "hasChildren": false, 
    "name": "Raj",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""
person = json.loads(person_json)
print(person)