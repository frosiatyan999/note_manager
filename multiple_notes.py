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
    print('Введите данные для заметки{i \\]}')
    note = {}
    while True:
        username = input('Введите ваше имя').strip().lower()
        # Пишем условие которое должно выполняться что бы остановить добавление заголовков а так же добавление заголовков в список
        if username.lower() == '':
            print('Вы не добавили имя!')
            continue
        else:
            note['Имя'] = username
            break
    while True:
        title = input('Введите заголовок вашей заметки: ')
        note['Заголовок:'] = title
        if title == '':
            print('Неверный ввод! Попробуйте ещё раз.')
            continue
        else:
            break
    while True:
        content = input('Придумайте описание вашей заметки: ')
        note['Описание:'] = content
        if content == '':
            print('Неверный ввод! Попробуйте ещё раз.')
            continue
        else:
            break


