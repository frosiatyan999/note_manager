status = ['1.В процессе', '2.Отложено','3.Выполнено']
print('Текущий статус заметки: ' + status[0])
print('Выберите новое значение для статуса:')
print('\n'.join(status))
while True:
    choise = print(input('Напишите число для изменения статуса заметки: '))
    if choise == '1':
        print('Текущий статус заметки: ' + status[0])
        break
    elif choise == '2':
        print('Текущий статус заметки: ' + status[1])
        break
    elif choise == '3':
        print('Текущий статус заметки: ' + status[2])
        break
    else:
        print('Неверный ввод')
        break


