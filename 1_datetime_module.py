import datetime

# Example 1 – Get current date and time
now = datetime.datetime.now()
print("Now:", now)

# Example 2 – Get today's date
today = datetime.date.today()
print("Today:", today)

# Example 3 – Current time only
current_time = datetime.datetime.now().time()
print("Current Time:", current_time)

# Example 4 – Current UTC time
utc_now = datetime.datetime.utcnow()
print("UTC Now:", utc_now)

# Example 5 – Get components of datetime
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)