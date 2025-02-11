import datetime

current_date = datetime.datetime.today()
yesterday_date = current_date - datetime.timedelta(days=1)
tommorow_date = current_date + datetime.timedelta(days=1)
print(yesterday_date.strftime('%Y-%m-%d') , current_date.strftime('%Y-%m-%d') , tommorow_date.strftime('%Y-%m-%d'))