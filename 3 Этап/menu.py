from datetime import datetime
from colorama import init, deinit
from colorama import Fore, Style
init(autoreset=True)
notes = []
# Создаём функцию "Меню действий"
def menu():
    while True:
        print(Fore.YELLOW +
              '    Меню действий:\n'
              '1. Создать новую заметку\n'
              '2. Показать все заметки\n'
              '3. Обновить заметку\n'
              '4. Удалить заметку\n'
              '5. Поиск заметки\n'
              '6. Выйти из программы'
              )
        print('--------------------------------')
        menu_choice = input(Style.BRIGHT + 'Введите цифру действия которое хотите совершить: ')
        if menu_choice == '1':
            print(Fore.YELLOW + 'Ваш выбор: 1. Создать новую заметку.')
            print('--------------------------------')
            create_note()

        elif menu_choice == '2':
            print(Fore.YELLOW + 'Ваш выбор: 2. Показать все заметки.')
            print('--------------------------------')
            if len(notes) > 0:
                display_notes(notes)

        elif menu_choice == '3':
            print(Fore.YELLOW + 'Ваш выбор: 3. Обновить заметку.')
            print('--------------------------------')
            handle_update_notes_choice(notes)

        elif menu_choice == '4':
            print(Fore.YELLOW + 'Ваш выбор: 4. Удалить заметку.')
            delete_note(notes)

        elif menu_choice == '5':
            print(Fore.YELLOW + 'Ваш выбор: 5. Поиск заметки.')
            print('--------------------------------')
            choice_search_notes(notes)

        elif menu_choice == '6':
            print('Завершение работы программы. Спасибо за использование нашей программы!')
            quit()
        else:
            print('Неверный ввод. Пожалуйста попробуйте ещё раз.')
            continue

# Функция: 1. Создать новую заметку
def create_note():
    print(Style.BRIGHT + 'Давайте создадим новую заметку!')
# Просим пользователя ввести данные для заметки
    while True:
        username = input('Введите ваше имя: ')
        if username == '':
            print(Fore.RED + 'Неверный ввод! Попробуйте ещё раз пожалуйста.')
            continue
        else:
            break
    while True:
        title = input('Введите заголовок заметки: ')
        if title == '':
            print(Fore.RED + 'Неверный ввод! Попробуйте ещё раз пожалуйста.')
            continue
        else:
            break
    while True:
        content = input('Введите описание заметки: ')
        if content == '':
            print(Fore.RED + 'Неверный ввод! Попробуйте ещё раз пожалуйста.')
            continue
        else:
            break
# Статус для новых заметок присваивается по умолчанию
    status = 'Новая'
# Текущая дата вводится автоматически
    created_date = datetime.now().date().strftime('%d-%m-%Y')
# С помощью цикла вводим и проверяем правильность даты дедлайна
    while True:
        issue_date = input('Введите дату дедлайна заметки\n'
                    ' в формате "дд-мм-гггг"(через дефис и без пробелов): ')
        try:
            issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
            break
        except ValueError:
            print(Fore.RED + 'Неверный ввод! Попробуйте ещё.')
            continue
# Записываем все полученные данные в словарь
    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": datetime.strftime(issue_date, '%d-%m-%Y')
    }
    notes.append(note)
# Выводим результат работы функции на экран
    print(Style.BRIGHT + "Заметка создана: ")
    print(*note.items(), sep='\n')
    print('--------------------------------')
# Возвращаем список заметок и пользователь возвращается в меню программы
    return notes and menu()

# Функция: 2. Показать все заметки
def display_notes(notes):
    # Функция проверяет список заметок на их наличие и выводит результат
    print(Style.BRIGHT + 'Список ваших заметок:')
    if len(notes) == 0:
        print(Fore.RED + 'К сожалению у вас нет созданных заметок')
        print('--------------------------------')
        return menu()
    a = 0
    for item in notes:
        print('--------------------------------')
        print(Style.BRIGHT + f'Заметка №{a + 1}:')
        a += 1
        print(*item.items(), sep='\n')
        print('--------------------------------')
# Возвращаем список заметок и пользователь возвращается в меню программы
    return notes and menu()

# Функция: 3. Обновить заметку
def update_note(note):
    # Предлагаем пользователю выбрать данные для изменения
    while True:
        print()
        change = input('Какие данные хотите обновить?\n'
            '("username, title, content, status, issue_date"): ')
        if (change == "username" or
            change == "title" or
            change ==  "content" or
            change == "status" or
            change == "issue_date"):
            break
        else:
            print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
            continue
    # Выбранные данные изменяются и записываются в словарь
    while True:
        if change == 'username':
            # Можно ввести любое имя, но поле не может быть пустым
            while True:
                username = input('Введите новое ваше имя: ')
                if username == '':
                    print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
                    continue
                else:
                    break
            note['username'] = username
            break
        elif change == 'title':
            #Может быть введён любой заголовок, но моле не может быть пустым
            while True:
                title = input('Введите новый заголовок заметки: ')
                if title == '':
                    print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
                    continue
                else:
                    break
            note['title'] = title
            break
        elif change == 'content':
            while True:
                # Можно ввести любое описание, но поле не может быть пустым
                content = input('Введите новое описание заметки: ')
                if content == '':
                    print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
                    continue
                else:
                    break
            note['content'] = content
            break
        elif change == 'status':
            while True:
                # Можно ввести любой статус, но поле не может быть пустым
                status = input('Введите  новый статус заметки (например, "новая", "в процессе", "выполнена"): ')
                if status == '':
                    print('Неверный ввод! Попробуйте ещё раз пожалуйста.')
                    continue
                else:
                    break
            note['status'] = status
            break
        elif change == 'issue_date':
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

# Возвращаем список с обновлённой заметкой и пользователь возвращается в меню программы
    return notes and menu()

# Функция для обработки выбора заметки для изменения
def handle_update_notes_choice(notes):
    if len(notes) > 0:
        i = 0
        for note in notes:
            print(f'Заметка №{i + 1}')
            i += 1
            print(*note.items(), sep='\n')
            print('--------------------------------')
    else:
        print('Ваш список заметок пуст.')
    while True:
        if note in notes:
            selected_note = int(input('Введите номер заметки для изменения: ')) - 1
            if selected_note == notes.index(note):
                print('Ваш выбор заметки:')
                print(*note.items(), sep='\n')
                print('--------------------------------')
                note = update_note(note)
                update_note(note)
            else:
                print('Заметки под таким номером нет.')
        break
# Функция: 4. Удалить заметку
def delete_note(notes):
    print(Fore.RED + 'Извините, данная функция пока не реализована.')
    print('--------------------------------')
    return notes and menu()

# Функция выбора метода поиска
def choice_search_notes(notes):
    while True:
        print('Какой тип пойска заметки хотите осуществить?')
        question = input('1 - по ключевому слову\n'
                         '2 - по статусу\n'
                         '3 - по ключевому слову и статусу\n'
                         'Введите цифру вашего выбора: ')
        print('--------------------------------')
        if question == '1':
            print(Style.BRIGHT + 'Ваш выбор: Поиск по ключевому слову.')
            keyword = input('Введите имя, название или описание заметки для поиска: ')
            keyword = search_notes(notes, keyword)
            break
        if question == '2':
            print(Style.BRIGHT + 'Ваш выбор: Поиск по статусу заметки.')
            status = input('Введите статус заметки для поиска (новая, в процессе, выполнено): ')
            status = search_notes(notes, status)
            break
        if question == '3':
            print(Style.BRIGHT + 'Ваш выбор: Поиск по имени пользователя и статусу.')
            keyword = input('Введите имя, название или описание заметки для поиска: ')
            status = input('Введите статус заметки для поиска (новая, в процессе, выполнена): ')
            notes = search_notes(notes, keyword, status)
            break
        else:
            print(Fore.RED + 'Неверный ввод. Попробуйте ещё раз.')

# Функция: 5. Поиск заметки
def search_notes(notes, keyword=None, status=None):
# Проверка для пустого списка
    if len(notes) < 0:
         print('Список заметок пуст.')
         return notes and menu()

# Если не задано ключевое слово или статус возвращаем исходный список заметок и пользователь возвращается в меню
    if keyword is None and status is None:
         return notes and menu()

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

# Отображаем результат поиска
    if len(notes_list) > 0:
        print('Результат поиска:')
        for i, note in enumerate(notes_list, 1):
            print(f'Заметка №{i}:')
            print(*note.items(), sep='\n')
    else:
        print('Поиск не дал результата.')

    return notes and menu()
menu()
deinit()