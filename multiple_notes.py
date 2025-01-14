from time import sleep
from datetime import datetime as dt
multiple_notes = []
print('Добро пожаловать')
current_date = dt.today().date()
print('Сегодня: ', current_date)
while True:
    welcome = input('Хотите создать заметку? да/нет\n').strip().lower()
    if welcome.strip().lower() == 'да':
        break
    elif welcome.strip().lower() == 'нет':
        quit('До встречи!')
    else: 
        print('Неверное значение')
i = 0
while True:
    note = {}
    while True:
        i += 1
        username = input('Введите ваше имя \n').strip().lower()
        # Пишем условие которое должно выполняться что бы остановить добавление заголовков а так же добавление заголовков в список
        if username.lower() == '':
            print('Вы не добавили имя! \n')
            continue
        else:
            note['Имя'] = username
            break
    while True:
        title = input('Введите заголовок вашей заметки: \n')
        note['Заголовок:'] = title
        if title == '':
            print('Неверный ввод! Попробуйте ещё раз.')
            continue
        else:
            break
    while True:
        content = input('Придумайте описание вашей заметки: \n')
        note['Описание:'] = content
        if content == '':
            print('Неверный ввод! Попробуйте ещё раз.')
            continue
        else:
            break
    while True:
        status_list = {'1': "Выполняется", '2': "Выполнено", '3': "Отложено"}
        print('1.', status_list['1'], '\n''2.', status_list['2'], '\n''3.', status_list['3'])
        choice = input('Напишите число или напишите нужный статус для изменения статуса заметки: \n').strip().lower()
        if choice.strip().lower() == '1' or choice.strip().lower() == 'выполняется':
            choice1 = choice
            print('Текущий статус заметки: ' + status_list['1'])
            break
        elif choice.strip().lower() == '2' or choice.strip().lower() == 'выполнено':
            choice1 = choice
            print('Текущий статус заметки: ' + status_list['2'])
            break
        elif choice.strip().lower() == '3' or choice.strip().lower() == 'отложено':
            choice1 = choice
            print('Текущий статус заметки: ' + status_list['3'])
            break
        # Создаем условия для остальный символов при котором пустой ввод будет окончательным выбором, а остальные символы ошибкой
        else:
            print('Неверный ввод')
            continue
    # Здесь спасает choise1 который перенимает строку choise и в случае пустого ввода не потеряет строку
        note['Cтатус заметки:'] = status_list.get(choice1)
    while True:
        print('Ведите сначала день, затем месяц и год для определения даты в формате ДД-ММ-ГГГГ')
        created_date = input()
        try:
            created_date = dt.strptime(created_date, '%d-%m-%Y').date()
            print('Ваш дедлайн: ', created_date.strftime('%d-%m-%Y'))
            break
        except ValueError:
            print('Не определена дата! Проверьте правильность ввода')
            continue
    note['Дата начала заметки'] = created_date
    while True:
        print('Ведите сначала день, затем месяц и год для определения даты в формате ДД-ММ-ГГГГ')
        issue_date = input()
        try:
            issue_date = dt.strptime(issue_date, '%d-%m-%Y').date()
            print('Ваш дедлайн: ', issue_date.strftime('%d-%m-%Y'))
            break
        except ValueError:
            print('Не определена дата! Проверьте правильность ввода')
            continue
    note['Дата дедлайна заметки'] = issue_date
    print('-----------------------------------')
    print('Создаем заметку')
    multiple_notes.append(note)
    welcome = input('Хотите создать ещё одну заметку? (да/нет): \n').lower()
    if welcome == 'да':
        continue
    elif welcome == 'нет':
        print('Группируем ваши данные...')
        sleep(3)
        break
    else:
        print('Неверный ввод! Попробуйте ещё раз.')
        continue
print('Вы создали следующие заметки: ')
z = 0
for item in multiple_notes:
    print(f'Заметка №{z + 1}:')
    z += 1
    print(*item.items(), sep='\n')





