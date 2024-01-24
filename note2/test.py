import json

#param = input("введите id")
data = json.load(open("notes.json"))

data['notes'].pop()
    # i=0
# for note in data['notes']:
# note = data['notes'][0]
#         #i+=1
# print(note['title'])

# minimal = 0
# for txt in data['notes']:
#     if txt['id'] == param:
#         data['notes']minimal
#     else:
#         print("opa")
#     minimal = minimal+1  
