from datetime import datetime

date=datetime.now()
year=date.year
month=date.month
day=date.day
hour=date.hour
minite=date.minute
second=date.second
micro=date.microsecond
print(f"{year}-{month}{day}-{hour}{minite}{second}-{micro}")
