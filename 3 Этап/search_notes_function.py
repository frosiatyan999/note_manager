def search_notes(notes, keyword=None, status=None):
    fields_for_search = ["title", "content", "username"]
    found_notes = []

    for note in notes:
        keyword_creteria = True
        status_creteria = True

        # if keyword != None: # сравнение по значение
        if keyword is not None: # сравнение по ссылки (объект один и тот же)
            for field in fields_for_search:
                if note[field] == keyword:
                    keyword_creteria = True
                else:
                    keyword_creteria = False
        if status is not None:
            if note["status"] == status:
                status_creteria = True
            else:
                status_creteria = False

        if keyword_creteria == True and status_creteria == True:
            found_notes.append(note)

    return found_notes

if __name__ == '__main__':
    notes = [
        {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
         'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
        {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
         'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
        {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
         'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
    ]
    found_notes = search_notes(notes)
    print(found_notes)