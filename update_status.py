# Создаем словарь и кортеж (нужен только для красивого отображения статусов) 
status_list = {'1':"Выполняется",'2':"Выполнено", '3':"Отложено"}
print('Текущий статус заметки: ' + status_list['1'])
print('Выберите новое значение для статуса:')
# Далее кортеж не будет нужен
print('1.',status_list['1'],'\n''2.',status_list['2'],'\n''3.',status_list['3'])
# Создаем условие, при котором дается на выбор 3 статуса и добавляем choise1 который поможет в конце
while True:
    choice = input('Напишите число или напишите нужный статус для изменения статуса заметки: ').strip().lower()
    if choice.strip().lower() == '1' or choice.strip().lower() == 'выполняется':
        print('Текущий статус заметки: ' + status_list['1'])
        print('Для подтверждения текущего статуса нажмите Enter')
    elif choice.strip().lower() == '2' or choice.strip().lower() == 'выполнено':
        print('Текущий статус заметки: ' + status_list['2'])
        print('Для подтверждения текущего статуса нажмите Enter')
    elif choice.strip().lower() == '3' or choice.strip().lower() == 'отложено':
        print('Текущий статус заметки: ' + status_list['3'])
        print('Для подтверждения текущего статуса нажмите Enter')
# Создаем условия для остальный символов пр и котором пустой ввод будет окончательным выбором, а остальные символы ошибкой
    else:
        if choice.strip() == '':
            break
        else:
            print('Неверный ввод')
            continue
# Здесь спасает choise1 который перенимает строку choise и в случае пустого ввода не потеряет строку
print('Обновление статуса: ', status_list.get(choice))
