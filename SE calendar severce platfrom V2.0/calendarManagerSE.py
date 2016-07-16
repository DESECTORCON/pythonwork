# This program is imported to MAINCODE.py.
import calendar, datetime

class clanderM():
    def clander():
        c = calendar.TextCalendar(calendar.SUNDAY)
        CLAV = str(datetime.datetime.now()).split()[0].split('-')[0]
        CLAV2 = str(datetime.datetime.now()).split()[0].split('-')[1]
        return c.prmonth(int(CLAV), int(CLAV2))