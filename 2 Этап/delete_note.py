note_list = [{'Имя:': 'Алекс',
              'Заголовок:': 'Поход в магазин',
              'Описание:': 'Купить хлеб'
              },
             {
              'Имя:': 'Дима',
              'Заголовок:': 'Спортзал',
              'Описание:': 'Сходить в спортзал'
             },
             {
              'Имя:': 'Маша',
              'Заголовок:': 'Работа',
              'Описание:': 'Сдать отчёт'
             }]
print('Список заметок: ')
i = 0
for item in note_list:
    print(f'\nЗаметка {i + 1}: ')
    i += 1
    print(*item.items(), sep='\n')
while True:
    choice_title = input('Введите имя пользователя или заголовок заметки которую хотите удалить: \n').lower().strip()
    for j in reversed(range(len(note_list))):
        if (note_list[j]['Заголовок:'].lower().strip() != choice_title
                and note_list[j]['Имя:'] != choice_title):
            continue
# Когда заголовки совпали, предлагается подтвердить удаление
        elif note_list[j]['Заголовок:'].lower().strip() == choice_title or note_list[j]['Имя:'] == choice_title:
            while True:
                answer = input('Заметка найдена! Подтвердите удаление(да/нет):\n').lower()
                if answer == 'да':
                    del note_list[j]
                    print('Удаление успешно!')
                    break
                elif answer == 'нет':
                    break
                elif answer == '' or str:
                    print('Неверный ввод! Попробуйте ещё.')
                    continue
# Если заголовок не найден, программа об этом сообщает либо после удаления таких заметок нет
        print('Заметок для удаления не найдено!')
        continue
    stop_ = input('\nВведите стоп если хотите закончить удаление: \n').lower().strip()
# Выводим список заметок после изменения
    print('Ваш список заметок после изменения:\n')
    b = 0

    for item in note_list:
        print(f'Заметка №{b + 1}:')
        b += 1
        print(*item.items(), sep='\n')
    if stop_.lower() == "стоп":
        break
    continue

