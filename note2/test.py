import json

param = input("Введите что нибуд")
data = json.load(open("notes.json"))

for note in data['notes']:
    if note['title'] == param:
        print(note)
    elif note["timestamp"] == param:
        print(note)
    elif note['id'] == int(param):
        print(note)

