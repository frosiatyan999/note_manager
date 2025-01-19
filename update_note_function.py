# Загружаем библиотеку datetime для работы с датами
from datetime import datetime




# Создаём принимающую функцию
def update_note(note):
    while True:
    # Выводим заметку в удобном формате
        print('Ваша заметка:')
        for key, value in note.items():
            print('{0}: {1}'.format(key, value))

    # Предлагаем пользователю выбрать данные для изменения

        print()
        change = input('Какие данные хотите обновить?\n'
            '1:username\n2:title\n3:content\n4:status\n5:issue_date\n').strip().lower()
        if (change == "username" or change == "1" or
            change == "title" or change == "2" or
            change ==  "content" or change == "3" or
            change == "status" or change == "4" or
            change == "issue_date" or change == "5"):
            break
        else:
            print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
            continue

    # Выбранные данные изменяются и записываются в словарь
    while True:
        if change == 'username' or change == '1':
            # Можно ввести любое имя, но поле не может быть пустым
            while True:
                username = input('Введите новое ваше имя: ')
                if username == '':
                    print('Имя не изменено')
                    break
                else:
                    note['username'] = username
                    break
            break
        elif change == 'title' or change == '2':
            #Может быть введён любой заголовок, но моле не может быть пустым
            while True:
                title = input('Введите новый заголовок заметки: ')
                if title == '':
                    print('Заголовок не изменен')
                    break
                else:
                    note['title'] = title
                    break
            break
        elif change == 'content' or change == '3':
            while True:
                # Можно ввести любое описание а с пустыми символами поле для изменения не меняется
                content = input('Введите новое описание заметки: ')
                if content == '':
                    print('Описание не изменено')
                    break
                else:
                    note['content'] = content
                    break
            break
        elif change == 'status' or change == '4':
            while True:
                # Можно ввести любой статус, но поле не может быть пустым
                status = input('Введите  новый статус заметки ("новая", "в процессе", "выполнена"): ')
                if status == '':
                    print('Статус не изменен')
                    break
                else:
                    note['status'] = status
                    break
            break
        elif change == 'issue_date' or change == '5':
            while True:
                issue_date = input('Введите новую дату дедлайна заметки\n'
                                   ' в формате "дд-мм-гггг"(через дефис и без пробелов): ')
                try:
                    issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
                    break
                except ValueError:
                    print('Неверный ввод! Попробуйте ещё.')
                    continue
            note['issue_date'] = datetime.strftime(issue_date, '%d-%m-%Y')
            break
    # Возвращаем обновлённую заметку
    return note

# Заметка в которой надо что-то поменять
note = {
        'username': 'Дима',
        'title': 'Спортзал',
        'content': 'Пойти в спортзал',
        'status': 'новая',
        'created_date': '28-11-2024',
        'issue_date': '3-02-2025'
}


# Вызываем функцию для изменения содержания заметки
note = update_note(note)


# Выводим результат работы функции
print('--------------------------')
print('Ваша обновлённая заметка:')
for key, value in note.items():
    print('{0}: {1}'.format(key, value))

