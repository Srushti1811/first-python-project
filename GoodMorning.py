import time

current_hour = time.localtime().tm_hour

if 0 <= current_hour < 12:
    print("Good Morning, Sir!")
elif 12 <= current_hour < 17:
    print("Good Afternoon, Sir!")
elif 17 <= current_hour < 21:
    print("Good Evening, Sir!")
else:
    print("Good Night, Sir!")