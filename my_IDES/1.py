__author__ = 'choeminjun'
import time
now = time.localtime()


print("현재 년: %d" % (now.tm_year))
print("현재 월: %d" % (now.tm_mon))
print("현재 일: %d" % (now.tm_mday))

print()

print("현재 시: %d" % (now.tm_hour))         # 24시간제
print("현재 분: %d" % (now.tm_min))
print("현재 초: %d" % (now.tm_sec))

print()

print("오늘 요일: %d"     % (now.tm_wday))  # 월요일 = 0
print("올해 몇번째 날: %d"% (now.tm_yday))  # 1월 1일 = 1
print("서머타임 여부: %d" % (now.tm_isdst)) # 서머타임 없으면 0