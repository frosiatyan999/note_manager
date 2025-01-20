def display_page(notes, page):
    start_index = 0 + page * 5
    end_index = 5 + page * 5
                                # notes[0:5] - первая страница
                                # notes[5:10] - вторая страница
    for index, note in enumerate(notes[start_index:end_index], start=1):  # f строки f string
        print(f"""
        Номер заметки: {index}
        Имя пользователя: {note["username"]}
        Заголовок: {note["title"]}
        """)
        print("_" * 80)  # str * int

def display_notes(notes, page_number=0):
    if len(notes) == 0:
        print("Список заметок пуст")
    else:
        display_page(notes, page_number)

if __name__ == '__main__':
    notes = [
        {"username": "1", "title": "Y", "status": "F"},
        {"username": "2", "title": "CV"},
        {"username": "3", "title": "CV"},
        {"username": "4", "title": "CV"},
        {"username": "5", "title": "CV"},
        {"username": "6", "title": "CV"},
        {"username": "7", "title": "CV"},
        {"username": "8", "title": "CV"},
        {"username": "9", "title": "CV"},
        {"username": "10", "title": "CV"},
    ]
    display_notes(notes=notes, page_number=1)