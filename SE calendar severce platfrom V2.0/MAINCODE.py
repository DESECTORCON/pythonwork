# SE severce platfrom v2.0
# clander - v2.0
# 이 프로그램은 달력, 현재시각을 볼 수 있고, 알람 기능을 재공한다.
# 업대이트할 내용: stopwatch기능 추가하기.
'''업대이트할때 주의사항:
    -> 바꾸거나 수정을 할 때에는 원본을 저장하고 하십시오.
    -> 복제하지 마십시오.'''

import datetime, time, calendar                            # 이 프로그램에 필요한 모든 모듈을 인포트함.
import alarmSE, stopwachSE, sysSE, timeprinterSE, calendarManagerSE, timeprinterSE


print('----------------calendar----------------')
print('     welcome to s.e severce platfrom!    ')
while True:
    print('Do you want to check the time or set alarm or see the clander?') # 사용자의 명령을 'USRN'
    USRIN = input()                                                         # 변수에 저장.


    if USRIN == 'time':
        while True:

            USRIN2 = input('Do you also want to chak the date?')
            if USRIN2 == 'y' or USRIN2 == 'yes' or USRIN2 == 'n' or USRIN2 == 'no':
                break
            else:
                print('No command  named "%s". please type y or n.' % (USRIN2))

        if USRIN2 == 'yes' or USRIN2 == 'y':
            DATEV = timeprinterSE.timeprint.timewithdate()
            print(DATEV)

        elif USRIN2 == 'no' or USRIN2 == 'n':
            DATEV = timeprinterSE.timeprint.timewithoutdate()
            print(DATEV)


    elif USRIN == 'clander':
        calendarManagerSE.clanderM.clander()


    elif USRIN == 'alarm':
        alarmSE.alarm()

    elif USRIN == 'stopwach':
        stopwachSE.stopwatch()

    elif USRIN == 'OFF':
        sysSE.OFF()

    else:
        print('No command named %s! Please try again.' % (USRIN))