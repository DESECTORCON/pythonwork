import time
import os
from b import nonBlockingRawInput

name = input("Enter your name.")

print("Hello, " + name)

alarm_HH = input("Enter the hour you want to wake up at")
alarm_MM = input("Enter the minute you want to wake up at")

print("You want to wake up at " + alarm_HH + ":" + alarm_MM)

while True:
    now = time.localtime()
    if now.tm_hour == int(alarm_HH) and now.tm_min == int(alarm_MM):
        print("ALARM NOW!")
        os.popen("open mpg321 /home/pi/voltage.mp3")
        break

    else:
        print("no alarm")
    timeout = 60 - now.tm_sec
    if nonBlockingRawInput('', timeout) == 'stop':
        break