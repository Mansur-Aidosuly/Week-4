import datetime

now = datetime.datetime.now()

# Example 1 – Format date as YYYY-MM-DD
print(now.strftime("%Y-%m-%d"))

# Example 2 – Format time as HH:MM:SS
print(now.strftime("%H:%M:%S"))

# Example 3 – Format full date and time
print(now.strftime("%A, %d %B %Y %I:%M %p"))

# Example 4 – Parse string to datetime
date_str = "22-02-2026 14:30"
parsed_date = datetime.datetime.strptime(date_str, "%d-%m-%Y %H:%M")
print(parsed_date)

# Example 5 – Custom formatting with weekday
print(now.strftime("Today is %A"))