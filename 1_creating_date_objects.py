import datetime

# Example 1 – Specific date
d1 = datetime.date(2026, 2, 22)
print(d1)

# Example 2 – Using today() and replace()
d2 = datetime.date.today().replace(year=2025)
print(d2)

# Example 3 – From timestamp
timestamp = 1677024000
d3 = datetime.date.fromtimestamp(timestamp)
print(d3)

# Example 4 – Create datetime (date + time)
dt = datetime.datetime(2026, 2, 22, 14, 30)
print(dt)

# Example 5 – From ISO format string
iso_date = "2026-02-22"
d5 = datetime.datetime.fromisoformat(iso_date)
print(d5)