# Заметки для поиска
notes = [
    {
        'username': 'Алекс',
        'title': 'Список покупок',
        'content': 'Купить продукты',
        'status': 'новая',
        'created_date': '20-01-2025',
        'issue_date': '30-01-2025'
    },
    {
        'username': 'Дима',
        'title': 'Спортзал',
        'content': 'Сходить в спортзал',
        'status': 'в процессе',
        'created_date': '20-01-2025',
        'issue_date': '01-02-2025'
    },
    {
        'username': 'Даша',
        'title': 'День рождения',
        'content': 'Купить подарок',
        'status': 'выполнено',
        'created_date': '20-03-2025',
        'issue_date': '26-05-2025'
}
]

def search_notes(notes, keyword=None, status=None):
# Проверка для пустого списка
    if len(notes) < 0:
         print('Список заметок пуст.')
         return []

# Если не задано ключевое слово или статус вернуть исходный список заметок
    if keyword is None and status is None:
         return notes

    notes_list = []

    for note in notes:
        my_keyword = True
        my_status = True

# Поиск по ключевому слову
        if keyword is not None:
            keyword = keyword.lower()

# Поиск в имени пользователя, заголовке заметки или в описании заметки
            my_keyword = (
                    keyword in note['title'].lower() or
                    keyword in note['content'].lower() or
                    keyword in note['username'].lower()
            )

# Поиск по статусу
        if status is not None:
            my_status = note['status'].lower() == status.lower()

# Поиск по двум параметрам keyword и status
        if my_keyword and my_status:
            notes_list.append(note)

# Отобразить результат
    if len(notes_list) > 0:
        print('Результат поиска:')
        for i, note in enumerate(notes_list, 1):
            print(f'Заметка №{i}:')
            print(f'Имя пользователя: {note['username']}')
            print(f'Заголовок: {note['title']}')
            print(f'Описание: {note['content']}')
            print(f'Статус: {note['status']}')
            print(f'Дата создания: {note['created_date']}')
            print(f'Дата дедлайна: {note['issue_date']}')
    else:
        print('Ваш запрос не дал результата.')

    return notes

# Цикл для тестирования функции
while True:
    print('Какой тип поиска заметки хотите осуществить?')
    question = input('1 - по ключевому слову\n'
                     '2 - по статусу\n'
                     '3 - по ключевому слову и статусу\n'
                     'Введите цифру вашего выбора: ')
    if question == '1':
        keyword = str(input('Введите имя, название или описание заметки для поиска: '))
        print('Результат поиска по ключевому слову:')
        keyword = search_notes(notes, keyword)
        break
    if question == '2':
        status = input('Введите статус заметки для поиска (новая, в процессе, выполнено): ')
        print('Результат поиска по статусу:')
        status = search_notes(notes, status)
        break
    if question == '3':
        keyword = input('Введите имя, название или описание заметки для поиска: ')
        status = input('Введите статус заметки для поиска (новая, в процессе, выполнена): ')
        notes = search_notes(notes, keyword, status)
        break