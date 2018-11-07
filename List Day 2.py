weekdays = ["sun", "Tues", "Wed", "Thurs", "Fri"]
print(weekdays)
del weekdays[0]
print(weekdays)
weekdays.insert(0,"Mon")
print(weekdays)


a = "hello World"
b = "42"
c = 42


print(a.isdigit())
print(b.isdigit())
print(c.isdigit()) # doesn't work because function only works for strings and the number is not a string (not in quotes)
