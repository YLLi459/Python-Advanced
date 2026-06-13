import os
import datetime


file_path = 'example.txt'
if os.path.exists('example.txt'):
    print('file exists')
else:
    print('Doesnt exist')

name = 'Alice'
age = 30

with open('example.txt','w') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")

current_datetime = datetime.datetime.now()
print(current_datetime)
print("Year", current_datetime.year)
print("Month", current_datetime.month)
print("Dita", current_datetime.day)
print("Hour", current_datetime.hour)
print("Minute", current_datetime.minute)
print("Second", current_datetime.second)
print("Microsecond", current_datetime.microsecond)

deadline_time = datetime.time(12,00,00,000)
print(deadline_time)

print("Ora:",deadline_time.hour)
print("Minutat:",deadline_time.minute)
print("Sekondat:",deadline_time.second)
print("Milisekondat:",deadline_time.microsecond)

duration = datetime.timedelta(days=5,hours=3)
print(duration)

new_date = current_datetime + duration
print(new_date)

previous_date = current_datetime - duration
print(previous_date)