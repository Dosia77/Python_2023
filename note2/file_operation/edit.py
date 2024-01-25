
from datetime import datetime
import json

def edit_note():

    note_id = int(input("Введите ID заметки, которую необходимо отредактировать: ")) 
    data = json.load(open("notes.json"))
    minimal = 0
    for txt in data['notes']:
        if txt['id'] == note_id:
            data['notes'].pop(minimal)
        else:
            print("Нет такой заметки")
        minimal = minimal+1   

    timestamp = datetime.now().strftime('%Y-%m-%d')#№ %H:%M:%S')
    note_title = input("Введите заголовок заметки: ")
    note_body = input("Введите текст заметки: ")
    new_data = {"id": note_id,
                "title": note_title,
                "body": note_body,
                "timestamp": timestamp
                }
    
    data['notes'].append(new_data)

    with open("notes.json", "w") as file:
        json.dump(data, file,indent=4, ensure_ascii=False )

    print("Заметка успешно отредактирована!")  
