import json
import os
from datetime import datetime

notes = []
def create_first_note():
    
    timestamp = datetime.now().strftime('%Y-%m-%d') #%H:%M:%S') 
    note_id = 1 
    note_title = input("Введите заголовок заметки: ")

    note_body = input("Введите текст заметки: ")
    note = {"id": note_id,
            "title": note_title,
            "body": note_body,
            "timestamp": timestamp
    }
    notes.append(note)
    global_note = { "notes": notes }
    with open("notes.json", "w") as file:

        json.dump(global_note, file,indent=4, ensure_ascii=False )

    print("Первая заметка успешно создана")

def add_notes():
    data = json.load(open("notes.json")) 
    timestamp = datetime.now().strftime('%Y-%m-%d')#№ %H:%M:%S')
    note_id = len(data['notes']) + 1 
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


def delete_note():
    note_id = int(input("Введите ID заметки, которую необходимо удалить: "))
    data = json.load(open("notes.json"))
    minimal = 0
    for txt in data['notes']:
        if txt['id'] == note_id:
            data['notes'].pop(minimal)
        else:
            print("Нет такой заметки")
        minimal = minimal+1   
    
    with open("notes.json", "w") as file:

        json.dump(data, file,indent=4, ensure_ascii=False )
  

def read_notes():
   
    data = json.load(open("notes.json"))
    for note in data['notes']:
        print(f"ID: {note['id']}\nЗаголовок: {note['title']}\nТекст: {note['body']}\nДата/Время: {note['timestamp']}\n")


def select_to_parametr():
    param = input("Введите параметр для поиска\n1. Поиск по id\n2. Введите название\n3. Введите дату в формате ГГГГ-ММ-ДД")
    #param = '1'
    data = json.load(open("notes.json"))
    minimal = 0
    for txt in data['notes']:
        if txt['id'] == param:
            print(data['notes'][minimal]['title'])
        else:
            print("opa")
            minimal = minimal+1  

#def start():

while True:

    print("Меню:\n1. Создать первую заметку\n2. Добавить новую заметку\n3. Просмотреть все заметки\n4. Редактировать заметку\n5. Удалить заметку\nВыход")
   
    choice = input("Выберите действие: ")

    if choice == "1":
        create_first_note()

    elif choice == "2":
        add_notes()

    elif choice == "3":
        read_notes()

    elif choice == "4":
        edit_note()

    elif choice == "5":
        delete_note()

    elif choice == "6":
        break

    elif choice == "7":
        select_to_parametr()

    else:
        print("Некорректный выбор. Попробуйте снова.")

# def print():
#     data = json.load(open("notes.json"))
#     # i=0
#     # for note in data['notes']:
#     note = data['notes'][0]
#         #i+=1
#     print(note['title'])

# def main():  
#     start()

# if __name__ == '__main__' :
#     main()