from datetime import datetime
from colorama import init, deinit

# Используем библиотеку colorama для визуального оформления
init(autoreset=True)
from colorama import Fore, Style

# Создаём функцию, которая будет выводить список созданных заметок
def display_notes(notes):
    print(Fore.YELLOW + 'Список ваших заметок:')
    if len(notes) == 0:
        print(Fore.RED + 'К сожалению у вас нет созданных заметок')
    a = 0
    for item in notes:
        print('--------------------------')
        print(Style.BRIGHT + f'Заметка №{a + 1}:')
        a += 1
        print(*item.items(), sep='\n')
    return notes
# Создаём список в который будем добавлять готовые заметки
notes = []

# Простой цикл для интерактивности
# Создание заметок начинаем с вопроса
while True:
    question = input(Style.BRIGHT + 'Хотите создать заметку? (да\нет): ').lower()

# Если вопрос положительный, начинается сбор информации для заметки
    if question == 'да':
       note = {}
       while True:
           username = input(Style.BRIGHT + 'Введите имя пользователя: ')
           if username == '':
               print(Fore.RED + 'Неверный ввод. Нужно ввести хоть один символ.')
               continue
           else:
               break
       note['username'] = username
       while True:
           title = input(Style.BRIGHT + 'Введите название заметки: ')
           if title == '':
               print(Fore.RED + 'Неверный ввод. Нужно ввести хоть один символ.')
               continue
           else:
               break
       note['title'] = title
       while True:
           content = input(Style.BRIGHT + 'Введите описание заметки: ')
           if content == '':
               print(Fore.RED + 'Неверный ввод. Нужно ввести хоть один символ.')
               continue
           else:
               break
       note['content'] = content

# Статус для новых заметок присваивается автоматически
       status = 'Новая'
       note['status'] = status

# Время создания присваивается автоматически
       created_date = datetime.today().date()
       note['created_date'] = datetime.strftime(created_date, '%d-%m-%Y')
       while True:
           issue_date = input(Style.BRIGHT + 'Пожалуйста, введите дату дедлайна\n'
                              ' в формате "дд-мм-гггг"(через дефис и без пробелов): ')
           try:
               issue_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
               print(Style.BRIGHT + 'Вы ввели: ', issue_date.strftime('%d-%m-%Y'))
           except ValueError:
               print(Fore.RED + 'Неверный ввод! Попробуйте ещё.')
               continue
           if issue_date == created_date:
               print(Fore.RED + 'Внимание! Дедлайн истекает сегодня.')
               break
           elif issue_date < created_date:
               difference = created_date - issue_date
               print(Fore.RED + 'Внимание! Дедлайн истёк: ', difference.days, 'дней назад!')
               break
           elif issue_date > created_date:
               difference_1 = issue_date - created_date
               print(Fore.RED + 'Внимание! До дедлайна: ', difference_1.days, 'дней!')
               break
       note['issue_date'] = datetime.strftime(issue_date, '%d-%m-%Y')
       notes.append(note)
       continue
# При отрицательном ответе в список нечего не добавляется
    elif question == 'нет':
        break
    else:
        print(Fore.RED + 'Неверный ввод. Попробуйте ещё раз.')
        continue
deinit()
# В конце выводится функция, которая показывает созданные или нет заметки
display_notes(notes)


