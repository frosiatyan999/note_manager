from datetime import datetime as dt
multiple_notes = []
print('Добро пожаловать')
current_date = dt.today().date()
print('Сегодня: ', current_date)
while True:
    welcome = input('Хотите создать заметку? да/нет').strip().lower()
    if welcome.strip().lower() == 'да':
        break
    elif welcome.strip().lower() == 'нет':
        quit('До встречи!')
    else: 
        print('Неверное значение')
