from datetime import datetime, timedelta
from pytz import timezone

#Time Format
fmt = "%H:%M:%S"

now_pacific = datetime.now(timezone('US/Pacific'))
print 'Portland HQ Time:', now_pacific.strftime(fmt)

now_eastern = now_pacific.astimezone(timezone('US/Eastern'))
print 'New York HQ Time:', now_eastern.strftime(fmt)

now_london = now_pacific.astimezone(timezone('Europe/London'))
print 'London HQ Time:', now_london.strftime(fmt)

#Naive datetime object - non UTC time zone
pdxopen = datetime.strptime("09:00:00", '%H:%M:%S')
pdxclose = datetime.strptime("18:00:00", '%H:%M:%S')

if datetime.now() >= pdxopen > pdxclose:
    print ("Portland HQ Open")
else:
    print("Portland HQ Closed")

nycopen = datetime.strptime("09:00:00", '%H:%M:%S')
nycclose = datetime.strptime("18:00:00", '%H:%M:%S')
nycopen += timedelta(hours=3) # add 3 hours
nycclose += timedelta(hours=3)

if datetime.now() >= nycopen > nycclose:
   print("New York HQ Open")
else:
   print("New York HQ Closed")

lcyopen = datetime.strptime("09:00:00", '%H:%M:%S')
lcyclose = datetime.strptime("18:00:00", '%H:%M:%S')
lcyopen += timedelta(hours=8) # add 8 hours
lcyclose += timedelta(hours=8)

if datetime.now() >= lcyopen > lcyclose:
    print("London HQ Open")
else:
    print("London HQ Closed")
    






