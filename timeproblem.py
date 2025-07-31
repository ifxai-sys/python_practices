#this program will display a message of good evening after etc on basis of current time
import time
current_time=time.strftime('%H:%M:%S')
print(current_time)
current_hours=int(time.strftime('%H'))
print(current_hours)
current_minutes=int(time.strftime('%M'))
print(current_minutes)
current_seconds=int(time.strftime('%S'))
print(current_seconds)
if 5<=current_hours<12 :
    print("Good Morning Sir.")
elif  12<=current_hours<17 :
    print("Good Afternoon Sir.") 
elif 17<=current_hours<=21 :
    print("Good Evening Sir.")
else:
    print("Good Night Sir.")

