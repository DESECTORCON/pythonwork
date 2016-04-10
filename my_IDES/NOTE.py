__author__ = 'choe_min_jun'
import sys, random, time, datetime, NOTE_MAIL_controller
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
me = "choeminjun@naver.com"
my_password = r"minjun5627"

#mainv = open('SE_NOTE', 'w')
#mainv.close()
#mainv2 = open('ID&password', 'w')
#mainv2.close()


class NOTE_MAIN():
    class NOTE_SETUP_C():


        def NOTE_setup(ID, password, email):
            # data = ''
            # data1 = ''

            try:
                mainv = open('ID&password', 'w')
                mainv.write('ID: %s' % (ID))
                mainv.write('\npassword: %s' % (password))
                mainv.close()

                emaill = open('email', 'w')
                emaill.write('%s' % (email))
                emaill.close()

                # for dg in range(3):
                #     if dg == 0:
                #         data = 'ID: %s' % (ID)
                #
                #     if dg == 1:
                #         data = '\npassword: %s' % (password)
                #
                #     if dg == 2:
                #        data1 = 'email: %s' % (email)

                # mainv.write(data)
                # emaill.write(data1)

                user1 = open('user_note', 'w')
                user1.close()

                UM = NOTE_MAIL_controller.mail.getter.mailIdGetter()
                NOTE_MAIL_controller.mail.sender.mailsender(UM, 's.e 가입 메세지', \
                                                            '안녕하세요?\ns.e mail sender 입니다.\n'\
                                                            '환영합니다! s.e회사에서는 여러가지 서비스를 지원을 하는데 지금 가입하신 계정은\n'\
                                                            's.e NOTE 서비스를 사용할 수 있는 계정입니다.\n 나중에 다시 만나요~!\n From: s.e To:%s\n감사합니다!'%(ID))

            except Error as E:
                print('ERROR!! %s' % (E))
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
            mainv2.close()
            return mainv2_ID_password[0], mainv2_ID_password[1]



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
                        print('No commandword "%s"!\n please try again.' % (Eg))
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
                    print('No commandword "%s"!\n please try again.' % (userInput1))
                    userInput1 = input('Do you really are going to format the note?')

            print('Note formating...')
            mainv = open('user_note', 'r')
            lines = mainv.readlines()
            mainv.close()
            time.sleep(0.4)
            print('--->file formating...')
            time.sleep(0.7)
            demo = ''
            userI = []

            #userI = mainv.readlines()
            mainV2 = open('RecoverFile.txt', 'a')
            mainv = open('user_note', 'r')
            userI = mainv.readlines()
            linea = -1
            for line in userI:
                linea += 1
                mainV2.write(userI[int(linea)])
            mainV2.close()

            mainv = open('user_note', 'w')
            for line in lines:
                mainv.write(demo)

            mainv.close()


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
                    print('No commandword "%s"!\n please try again.' % (UI2))
                    UI2 = input('Do you really want to logout?')

            if UI2 == 'y' or UI2 == 'yes':
                print('logouting...')
                time.sleep(0.2)
                print('--->file closeing...')
                time.sleep(0.7)
                #mainv.close()
                #mainv2.close()

        def secession(userName, userpassword, useremailAddress):
            print('Do you really want to secession?')
            UI2 = input()
            while True:
                if UI2 == 'y' or UI2 == 'yes' or UI2 == 'n' or UI2 == 'no':
                    break

                else:
                    print('No commandword "%s"!\n please try again.' % (UI2))
                    UI2 = input('Do you really want to secession?')

            if UI2 == 'y' or UI2 == 'yes':
                mail = NOTE_MAIL_controller.mail.getter.mailIdGetter()
                NOTE_MAIL_controller.mail.sender.mailsender(mail, 's.e 회원 탈퇴메세지', \
                                                            '안녕하세요? s.e mail sender입니다.\n'\
                                                            '회원을 탈퇴하셨네요.'\
                                                            '다시 가입을 하시려면 OOOO.com 사이트에서 가입하세요.'\
                                                            '저희 서비스를 이용해 주셔서 감사함니다!')
                print('porgam shut downing...')
                time.sleep(0.6)
                print('--->file shut downing...')
                for trun in range(101):
                    print(str(trun) + '%')
                    time.sleep(0.2)
                print('good by~!')
                print('-----S.E----')
                mainV = open('ID&password', 'w')
                mainV.close()
                mainV2 = open('email', 'w')
                mainV2.close()
                mainV3 = open('user_note', 'w')
                mainV3.close()
                sys.exit(111)
            else:
                return

        def secessionChecker():
            mainV = open('ID&password', 'r')
            checkerV = mainV.readlines()
            if checkerV == [] or checkerV is ['']:
                mainV.close()
                return 'False'
            else:
                mainV.close()
                return 'True'


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
                mainlist = ['\n', '=========', 'user_command=shut_down', '-shutDowned on', str(datetime.datetime.now()), '=========']
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

    class Recovery():

        def Recovery():
            Ega = input('Do you really want to undo your fomet action?')

            while True:
                if Ega == 'y' or Ega == 'n':
                    break

                else:
                    print('No commandword "%s"!\n please try again.' % (Ega))
                    Ega = input('Do you really want to undo your fomet action?')

            if Ega == 'y':
                print('undoing fomet action...')
                time.sleep(0.8)
                mainv = open('RecoverFile.txt', 'r')
                main = mainv.readlines()
                mainv.close()
                mainv = open('RecoverFile.txt', 'w')
                mainv.write('')
                mainv.close()
                maia = open('user_note', 'w')
                V = -1

                for line in main:
                    V += 1
                    maia.write(main[V])

                print('Done!!')