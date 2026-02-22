import datetime

# Example 1 – UTC timezone
utc_dt = datetime.datetime.now(datetime.timezone.utc)
print("UTC datetime:", utc_dt)

# Example 2 – Create a fixed offset timezone (+3 hours)
tz = datetime.timezone(datetime.timedelta(hours=3))
dt_with_tz = datetime.datetime(2026, 2, 22, 12, 0, tzinfo=tz)
print(dt_with_tz)

# Example 3 – Convert naive datetime to UTC
naive_dt = datetime.datetime(2026, 2, 22, 12, 0)
aware_dt = naive_dt.replace(tzinfo=datetime.timezone.utc)
print(aware_dt)

# Example 4 – Current time in different timezone
dt_utc = datetime.datetime.now(datetime.timezone.utc)
dt_plus5 = dt_utc.astimezone(datetime.timezone(datetime.timedelta(hours=5)))
print(dt_plus5)

# Example 5 – Difference between timezones
tz1 = datetime.timezone(datetime.timedelta(hours=2))
tz2 = datetime.timezone(datetime.timedelta(hours=-5))
dt1 = datetime.datetime(2026, 2, 22, 12, 0, tzinfo=tz1)
dt2 = datetime.datetime(2026, 2, 22, 12, 0, tzinfo=tz2)
print("Time difference (hours):", (dt1 - dt2).total_seconds() / 3600)