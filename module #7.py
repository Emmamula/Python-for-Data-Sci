#1
import sys
import datetime
date = datetime.datetime.now().time()
print("current time")
print(date)
print("")


#2
from datetime import datetime, date, time, timedelta
My_birthday = date(1998, 5, 6)
print ('Emmanuel Amula\'s birthday is on {}.'.format(My_birthday.strftime('%b %d, %Y')))

#3
import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)

data = My_birthday - datetime_object
print(data)