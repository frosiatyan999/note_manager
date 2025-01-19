from datetime import datetime as dt 
current_date = dt.now().date()
print('Текущая дата: ', current_date.strftime('%d-%m-%Y'))
while True:
    print('Ведите сначала день, затем месяц и год для определения даты в формате ДД-ММ-ГГГГ')
    issue_date = input()
    try:
        issue_date = dt.strptime(issue_date, '%d-%m-%Y').date()
        print('Ваш дедлайн: ', issue_date.strftime('%d-%m-%Y'))
    except ValueError:
        print('Не определена дата! Проверьте правильность ввода')
        continue
    if issue_date == current_date:
        print('Ваш дедлайн заканчивается сегодня!')
        break
    elif issue_date < current_date:
        difference = current_date - issue_date
        print('Ваш дедлайн закончился ',difference.days,' дней назад')
        break
    elif issue_date > current_date:
        difference = issue_date - current_date
        print('До конца вашего дедлайна ',difference.days,' дней')
        break
