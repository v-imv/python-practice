"""
# To get current date and time must use datetime library
from datetime import datetime

current_date = datetime.now()
print(current_date)

print("Today is: " + str(current_date))
"""

"""
from datetime import datetime, timedelta
today = datetime.now()
print("Today is: " + str(today))

one_day = timedelta(days=1)
yesterday = today - one_day
print("Yesterday was " + str(yesterday))
"""

"""
from datetime import datetime
current_date = datetime.now()

print("Day: " + str(current_date.day))
print("Month: " + str(current_date.month))
print("Year: " + str(current_date.year))
"""

