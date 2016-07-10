import os, zipfile, pprint, time, datetime, sys
import MAINCODE_Function_ZFR

class MAIN_ZFR():

    global langENKO, currentLang

    currentLang = 'en'

    langENKO = {
        'ask/open/ko':'아카이브파일을 여시겠습니까 아니면 아카이브 파일을 푸시겠습니까?',
        'ask/open/en':'Do you want to read a zipfile or make a zipfile?',
        'command/read/ko':'열기',
        'command/read/en':'read',
        'command/read/ER/ko':'입력하신 파일의 경로는 존재하지 않습니다! 다시 입력해 주십시오.',
        'command/read/ER/en':'The path you typed dase not exites.',
        'command/read/path/ko':'파일의 경로를 입력해 주십시오.',
        'command/read/path/en':'Please type a path.',
        'command/ExtractFile/ko':'파일풀기',
        'command/ExtractFile/en':'extract',
        'command/ExtractFile/path/ko':'파일의 경로를 입력해 주십시오.',
        'command/ExtractFile/path/en':'Please type a path.',
        'command/ExtractFile/done/ko':'파일이 풀어졌습니다.',
        'command/ExtractFile/done/en':'The file has extracted.',
        'command/termination/ko':'종료',
        'command/termination/en':'OFF',
        'command/termination/q/ko:':'진짜 작업을 종료하시겠습니까?',
        'command/termination/q/en':'Do you relay want termination?',
        'command/termination/yes/ko':'안녕히 계십시오.',
        'command/termination/yes/en':'Bye~!'
    }

    def getMsg(code):
        return langENKO[code + '/' + currentLang]

    # main한 - this code is 한.
    def main():
        # if c == 'ko':
        #     lang = 'ko'
        while True:
            print(MAIN_ZFR.getMsg('ask/open'))
            userV = input()

            if userV == MAIN_ZFR.getMsg('command/read'):
                PATH = input(MAIN_ZFR.getMsg('command/read/path'))
                if os.path.exists(PATH) == True:
                    contens = MAINCODE_Function_ZFR.reader(PATH)
                    print(contens)
                else:
                    print(MAIN_ZFR.getMsg('command/read/ER'))


            elif userV == MAIN_ZFR.getMsg('command/ExtractFile'):
                PATH = input(MAIN_ZFR.getMsg('command/ExtractFile/path'))
                if os.path.exists(PATH) == True:
                    contens = MAINCODE_Function_ZFR.Extracter(PATH)
                    print(MAIN_ZFR.getMsg('command/ExtractFile/done'))


            elif userV == MAIN_ZFR.getMsg('command/termination'):
                USERV = input(MAIN_ZFR.getMsg('command/termination/q'))
                if USERV == MAIN_ZFR.getMsg('command/termination/yes'):
                    print(MAIN_ZFR.getMsg('command/termination/yes'))
                    sys.exit(10)
                    # elif mainV == 'en':
                    #     while True:
                    #         print('Do you want to read a zipfile or make a zipfile?')
                    #         userV = input()
                    #         if userV == 'read':
                    #             PATH = input('Please type a path.')
                    #             if os.path.exists(PATH) == True:
                    #                 contens = MAINCODE_Function_ZFR.chipPicer.Zreader(PATH)
                    #                 print(contens)
                    #             else:
                    #                 print('The path you typed dase not exites.')
                    #
                    #
                    #         elif userV == 'extract':
                    #             PATH = input('Please type a path.')
                    #             if os.path.exists(PATH) == True:
                    #                 contens = MAINCODE_Function_ZFR.chipPicer.Extracter(PATH)
                    #                 print('the file has extracted.')
                    #
                    #
                    #         elif userV == 'OFF':
                    #             USERV = input('Do you relay want termination?')
                    #             if USERV == 'yes':
                    #                 print('Bye~!')
                    #                 sys.exit(10)


    # main - this code do the setup.(language setting)
    def mainSetup():
        print('--------------------------------------------s.e-----------------------------------------------------')
        time.sleep(0.4)
        print('                                       <ZipFileReader>                                              ')
        time.sleep(1)
        print('---> setuping...')
        time.sleep(1)
        print('---> module importing...')
        time.sleep(1)
        print('language setting: 한국어(ko) or English(en)')
        languageSV = input()

        while True:
            if languageSV == 'ko' or languageSV == 'en':
                break

            print('No command named "%s"! please try again!!' % (languageSV))
            print('language setting:(한국어 or English)')
            languageSV = input()

        if languageSV == 'ko':
            print('---환영합니다!---')
            MAIN_ZFR.currentLang = 'ko'
            MAIN_ZFR.main()

        elif languageSV == 'en':
            print('---Hello~!---')
            MAIN_ZFR.currentLang = 'en'
            MAIN_ZFR.main()




MAIN_ZFR.mainSetup()
