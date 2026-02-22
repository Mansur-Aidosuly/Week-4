import datetime

# Example 1 – Difference between two dates
d1 = datetime.date(2026, 2, 22)
d2 = datetime.date(2026, 3, 1)
delta = d2 - d1
print("Days difference:", delta.days)

# Example 2 – Add days to a date
future = d1 + datetime.timedelta(days=10)
print("10 days later:", future)

# Example 3 – Subtract days
past = d1 - datetime.timedelta(days=5)
print("5 days before:", past)

# Example 4 – Difference between datetimes
dt1 = datetime.datetime(2026, 2, 22, 12, 0)
dt2 = datetime.datetime(2026, 2, 23, 15, 30)
diff = dt2 - dt1
print("Difference in seconds:", diff.total_seconds())

# Example 5 – Add hours and minutes
new_time = dt1 + datetime.timedelta(hours=5, minutes=45)
print("5h45m later:", new_time)