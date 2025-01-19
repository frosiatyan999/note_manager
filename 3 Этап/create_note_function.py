# Загружаем библиотеку datetime для работы с датами
from datetime import datetime as dt
from datetime import timedelta


# Создаём функцию создания заметки
def create_note():
# Просим пользователя ввести данные для заметки
    username = input('Введите ваше имя: ').strip()
    title = input('Введите заголовок заметки: ').strip()
    content = input('Введите описание заметки: ').strip()
    status = input('Введите статус заметки ("новая", "в процессе", "выполнена"): ').lower().strip()
# Текущая дата вводится автоматически
    created_date = dt.now().date().strftime('%d-%m-%Y')
# С помощью цикла вводим и проверяем правильность даты дедлайна
    while True:
        issue_date = input('Введите дату дедлайна заметкив формате "дд-мм-гггг"\n'
                    ' (через дефис и без пробелов): или выберите по умолчанию нажав Enter ')
        if issue_date == '':
            created_date = dt.strptime(created_date, '%d-%m-%Y').date()
            issue_date = created_date + timedelta(days=7)
            break
        else:
            try:
                issue_date = dt.strptime(issue_date, '%d-%m-%Y').date()
                break
            except ValueError:
                print('Неверный ввод! Попробуйте ещё.')
                continue


# Записываем все полученные данные в словарь
    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": dt.strftime(issue_date, '%d-%m-%Y')
    }

    return note

# Вызываем созданную функцию
note = create_note()
# Выводим результат работы функции на экран
print("Заметка создана: ")
print(*note.items(), sep='\n')