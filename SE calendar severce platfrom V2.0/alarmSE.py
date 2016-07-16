# alarm_clock.py
# For SE progemes-MAINCODE.py
import time, sys

class AlarmException(Exception):
    pass


def alarm():
    print('welcome to alarm clock severce!!')
    ALARM_H = input('Enter the hour you want to wake up at:')
    ALARM_M = input('Enter the minute you want to wake up at:')

    while True:
        nowC = time.localtime()
        if nowC.tm_hour == int(ALARM_H) and nowC.tm_min == int(ALARM_M):
            print('ALARM!!!!')
            return

