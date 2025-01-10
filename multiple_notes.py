from datetime import datetime as dt 
current_date = dt.now().date()
print('Текущая дата: ', current_date.strftime('%d-%m-%Y'))
