__author__ = 'choe_min_jun'
import sys, random, time, datetime

#mainv = open('SE_NOTE', 'w')
#mainv.close()
#mainv2 = open('ID&password', 'w')
#mainv2.close()


class NOTE_MAIN():
    class NOTE_SETUP_C():


        def NOTE_setup(ID, password):
            data = ''

            try:
                mainv = open('ID&password', 'w')

                for dg in range(2):
                    if dg == 0:
                        data = 'ID: %s' % (ID)

                    elif dg == 1:
                        data = '\npassword: %s' % (password)
                    mainv.write(data)

                mainv.close()
                user1 = open('user_note', 'w')
                user1.close()

            except TypeError:
                print('TypeError!!')
                return 'Error: TypeError'


        def NOTE_login(ID, password):
            mainv = open('ID&password', 'r')
            rangea = mainv.readlines()

            for dg in range(len(rangea)):
                if ID and password in rangea[dg]:
                    return 'login_OK'

            return 'NO'


        def NOTE_self_login():
            mainv2 = open('ID&password', 'r')
            userInputID = input('ID: ')
            userInputpassword = input('password: ')
            mainv2_ID_password = mainv2.readlines()

            if 'ID: ' + userInputID + '\n' == mainv2_ID_password[0] and 'password: ' + userInputpassword == mainv2_ID_password[1]:
                return 'login_OK'

            return 'NO'


        def getID_password():
            mainv2 = open('ID&password', 'r')
            mainv2_ID_password = mainv2.readlines()
            return mainv2_ID_password[0], mainv2_ID_password[1]

            mainv2.close()




    class NOTE_EDIT():

        def NOTE_add(ID, password, noteText):
            result = NOTE_MAIN.NOTE_SETUP_C.NOTE_login(ID, password)

            if result == 'login_OK':
                print('login OK.')
                Eg = input('english or 한국어?')

                while True:
                    if Eg == 'e' or Eg == '한':
                        break

                    else:
                        print('No commandword "%s"!\n please try again.')
                        Eg = input('english or 한국어?')

                if Eg == 'e':
                    print('Note opening...')
                    user_note_data = open('user_note', 'a')
                    time.sleep(0.6)
                    print('text adding...')
                    user_note_data.write('\n' + noteText)
                    time.sleep(0.4)
                    print('Done!')
                    return
                elif Eg == '한':
                    print('노트 여는중...')
                    time.sleep(0.6)
                    user_note_data = open('user_note', 'a')
                    print('내용 쓰는중...')
                    user_note_data.write('\n' + noteText)
                    time.sleep(0.4)
                    print('완료!')
                    return


        def NOTE_format():
            userInput1 = input('Do you really are going to format the note?')

            while True:
                if userInput1 == 'y' or userInput1 == 'yes':
                    break

                elif userInput1 == 'n' or userInput1 == 'no':
                    return False

                else:
                    print('No commandword "%s"!\n please try again.')
                    userInput1 = input('Do you really are going to format the note?')

            print('Note formating...')
            mainv = open('user_note', 'r')
            lines = mainv.readlines()
            mainv.close()
            time.sleep(0.4)
            print('--->file formating...')
            time.sleep(0.7)
            mainv = open('user_note', 'w')
            demo = ''
            for line in lines:
                mainv.write(demo)

            mainv.close()
            return True

        def NOTE_READ():
            print('Note reading...')
            mainv = open('user_note', 'r')
            data = mainv.read()
            time.sleep(0.3)
            print('--->file opening...')
            time.sleep(0.5)
            print('Done!')
            mainv.close()
            return data

    class copyright():
        def copright_D(s=None):
            print('copyrite by %s. %s' % (__author__, s))
            return


    class Msys():

        def Note_shutdown(excode):
            print('porgam shut downing...')
            time.sleep(0.6)
            print('--->file shut downing...')
            for trun in range(101):
                print(str(trun) + '%')
                time.sleep(0.2)
            print('good by~!')
            print('-----S.E----')
            sys.exit(excode)



        def NOTE_logout():
            UI2 = input('Do you really want to logout?')

            while True:
                if UI2 == 'y' or UI2 == 'yes' or UI2 == 'n' or UI2 == 'no':
                    break

                else:
                    print('No commandword "%s"!\n please try again.')
                    UI2 = input('Do you really want to logout?')

            if UI2 == 'y' or UI2 == 'yes':
                print('logouting...')
                time.sleep(0.2)
                print('--->file closeing...')
                time.sleep(0.7)
                #mainv.close()
                #mainv2.close()

    class SysLogMaker():


        def syslogSetup():
            syslog = open('sysLog_2.1', 'a')
            syslog.close()


        def syslogAdd(type, maintext=None):

            syslog = open('sysLog_2.1', 'a')


            if type == 'add':
                mainlist = ['\n', '<<<', 'user_answer = add', str(datetime.datetime.now()), 'add on', '>>>']
                maintext = ''.join(mainlist)
                syslog.write(maintext)

            elif type == 'read':
                mainlist = ['\n', '<<<', 'user_answer = read', '-readed on', str(datetime.datetime.now()), '>>>']
                maintext = ''.join(mainlist)
                syslog.write(maintext)

            elif type == 'fomet':
                mainlist = ['\n', '<<<', 'user_answer = fomet', ' fometed on ', str(datetime.datetime.now()), '>>>']
                maintext = ''.join(mainlist)
                syslog.write(maintext)

            elif type == 'read':
                mainlist = ['\n', '<<<', 'user_answer = read', '-readed on', str(datetime.datetime.now()), '>>>']
                maintext = ''.join(mainlist)
                syslog.write(maintext)

            elif type == 'logout':
                mainlist = ['\n', '<<<', 'user_command=logout', '-logouted on ', str(datetime.datetime.now()), '>>>']
                maintext = ''.join(mainlist)
                syslog.write(maintext)

            elif type == 'off' or type == 'OFF' or type == 'sd':
                mainlist = ['\n', '<<<', 'user_command=shut_down', '-shutDownged on', str(datetime.datetime.now()), '>>>']
                maintext = ''.join(mainlist)
                syslog.write(maintext)

            elif type == 'login':
                mainlist = ['\n', '<<<', 'user_login', '-logined on', str(datetime.datetime.now()), '>>>']
                maintext = ''.join(mainlist)
                syslog.write(maintext)

            elif type == 'logout':
                mainlist = ['\n', '<<<', 'user_logout', '-logouted on', str(datetime.datetime.now()), '>>>']
                maintext = ''.join(mainlist)
                syslog.write(maintext)


            else:
                print('"type" error!')
                raise ValueError