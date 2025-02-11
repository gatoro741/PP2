import datetime

current_date = datetime.datetime.today()
yesterday_date = current_date - datetime.timedelta(days=1)
print(abs((current_date - yesterday_date).total_seconds()))