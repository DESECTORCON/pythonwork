# This program is imported to MAINCODE.py.
import datetime

class timeprint():
    def timewithdate():
        DATEV = str(datetime.datetime.now()).split('.')[0]
        return 'time: '+DATEV


    def timewithoutdate():
        DATEV = str(datetime.datetime.now()).split()[1]
        dateV1 = DATEV.split(':')[0]
        dateV2 = DATEV.split(':')[1]
        dateV3 = DATEV.split(':')[2]
        return '%s:%s:%s' % (dateV1, dateV2, dateV3)
