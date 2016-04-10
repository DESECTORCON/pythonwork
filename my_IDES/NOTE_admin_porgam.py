__author__ = 'choeminjun'
import NOTE, datetime, NOTE_MAIL_controller

sysm = open('sysLog_2.1', 'a')
sysm.write('\n-------------------------time"%s"==logined--------------------------------' % (datetime.datetime.now()))
sysm.close()


NOTE.NOTE_MAIN.SysLogMaker.syslogSetup()

def mainb():
    while True:
                print('------------------------S.E Note-------------------------------')
                UI1 = input('Do you want to add Note or fomet Note or read Note?')

                ID, password = NOTE.NOTE_MAIN.NOTE_SETUP_C.getID_password()

                if UI1 == 'add' or UI1 == 'add Note':
                    newDataNote = input('Note data: ')
                    NOTE.NOTE_MAIN.NOTE_EDIT.NOTE_add(ID, password, newDataNote)
                    NOTE.NOTE_MAIN.SysLogMaker.syslogAdd('add')

                elif UI1 == 'fomet' or UI1 == 'f':
                    flag = NOTE.NOTE_MAIN.NOTE_EDIT.NOTE_format()

                    if flag == True:
                        NOTE.NOTE_MAIN.SysLogMaker.syslogAdd('fomet')

                elif UI1 == 'read' or UI1 == 'read Note' or UI1 == 'r':
                    readed_note = NOTE.NOTE_MAIN.NOTE_EDIT.NOTE_READ()
                    print(readed_note)
                    NOTE.NOTE_MAIN.SysLogMaker.syslogAdd('read')

                elif UI1 == 'off' or UI1 == 'OFF':
                    NOTE.NOTE_MAIN.SysLogMaker.syslogAdd('off')
                    NOTE.NOTE_MAIN.Msys.Note_shutdown(184)

                elif UI1 == 'logout' or UI1 == 'lo':
                    NOTE.NOTE_MAIN.Msys.NOTE_logout()
                    NOTE.NOTE_MAIN.SysLogMaker.syslogAdd('logout')
                    break

                elif UI1 == 'Recovery' or UI1 == 'R':
                     NOTE.NOTE_MAIN.Recovery.Recovery()


def setup():

    UISETUP = ''

    secessionCheckV = NOTE.NOTE_MAIN.Msys.secessionChecker()
    if secessionCheckV == 'False':
        print('You have to make a new ID!')


        newID = input('ID: ')
        newPassword = input('password: ')
        newemail = input('email: ')
        NOTE.NOTE_MAIN.NOTE_SETUP_C.NOTE_setup(newID, newPassword, newemail)
        print('ID setup Done!!')
        return

    elif secessionCheckV == 'True':

        UISETUP = input('Do you want to make a new ID?(1) or secession your ID?(2)')
        while True:
                    if UISETUP == '1' or UISETUP == '2' or UISETUP == 'login' or UISETUP == 'l':
                        break

                    else:
                        print('No commandword "%s"!\n please try again.' % (UISETUP))
                        UISETUP = input('Do you want to make a new ID?(1) or secession your ID?(2)')
        if UISETUP == '1':

            newID = input('ID: ')
            newPassword = input('password: ')
            newemail = input('email: ')
            NOTE.NOTE_MAIN.NOTE_SETUP_C.NOTE_setup(newID, newPassword, newemail)
            print('ID setup Done!!')

        elif UISETUP == '2':

            print('if you want to secession, login.')
            NOTE.NOTE_MAIN.NOTE_SETUP_C.NOTE_self_login()
            ID, password = NOTE.NOTE_MAIN.NOTE_SETUP_C.getID_password()
            mail = NOTE_MAIL_controller.mail.getter.mailIdGetter()
            NOTE.NOTE_MAIN.Msys.secession(ID, password, mail)

        print('')


def main():
    try:
        opr = open('ID&password', 'r')
        opr.close()

    except:
        print('Error found!!')
        raise FileNotFoundError('"ID&password" file Not found.')

    while True:

        while True:
            loginT = NOTE.NOTE_MAIN.NOTE_SETUP_C.NOTE_self_login()
            if loginT == 'NO':
                print('ID is not login ID!!')

            else:
                break

        if loginT ==  'login_OK':
            NOTE.NOTE_MAIN.SysLogMaker.syslogAdd('login')
            mainb()
        print('---------------s.e home-------------------')
        IO = input('Do you want to login? or shut down?')
        if IO == 'login' or IO == 'l':
            loginT = NOTE.NOTE_MAIN.NOTE_SETUP_C.NOTE_self_login()
            if loginT == 'NO':
                print('ID is not login ID!!')
            elif loginT == 'login_OK':
                NOTE.NOTE_MAIN.SysLogMaker.syslogAdd('login')
                mainb()

        elif IO == 'shut down' or IO == 'sd':
            NOTE.NOTE_MAIN.SysLogMaker.syslogAdd('sd')
            NOTE.NOTE_MAIN.Msys.Note_shutdown(55)



if __name__ == '__main__':
    setup()
    main()