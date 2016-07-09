import os, zipfile, pprint, time, datetime, sys
import MAINCODE_Function_ZFR

class MAIN_ZFR():


    # main한 - this code is 한.
    def main한():

        while True:
            print('zip파일을 여시겠습니까 아니면 아카이브 파일을 푸시겠습니까?')
            userV = input()

            if userV == '열기':
                PATH = input('파일의 경로를 입력해 주십시오.')
                if os.path.exists(PATH) == True:
                    contens = MAINCODE_Function_ZFR.reader(PATH)
                    print(contens)
                else:
                    print('입력하신 파일의 경로는 존재하지 않습니다! 다시 입력해 주십시오.')


            elif userV == '파일풀기':
                PATH = input('파일의 경롤르 입력해 주십시오.')
                if os.path.exists(PATH) == True:
                    contens = MAINCODE_Function_ZFR.Extracter(PATH)
                    print('파일이 풀어졌습니다.')


            elif userV == '종료':
                USERV = input('진짜 작업을 종료하시겠습니까?')
                if USERV == '예':
                    print('안녕히 계십시오.')
                    sys.exit(10)







    def mainE():
        while True:
            print('Do you want to read a zipfile or make a zipfile?')
            userV = input()
            if userV == 'read':
                PATH = input('Please type a path.')
                if os.path.exists(PATH) == True:
                    contens = MAINCODE_Function_ZFR.chipPicer.Zreader(PATH)
                    print(contens)
                else:
                    print('The path you typed dase not exites.')


            elif userV == 'extract':
                PATH = input('Please type a path.')
                if os.path.exists(PATH) == True:
                    contens = MAINCODE_Function_ZFR.chipPicer.Extracter(PATH)
                    print('the file has extracted.')


            elif userV == 'OFF':
                USERV = input('Do you relay want to sleep?')
                if USERV == 'yes':
                    print('Bye~!')
                    sys.exit(10)




    # main - this code do the setup.(language setting)
    def main():
        print('--------------------------------------------s.e-----------------------------------------------------')
        time.sleep(0.4)
        print('                                       <ZipFileReader>                                              ')
        time.sleep(1)
        print('---> setuping...')
        time.sleep(1)
        print('---> module importing...')
        time.sleep(1)
        print('language setting:(한국어 or English)')
        languageSV = input()

        while True:
            if languageSV == '한국어' or languageSV == '한' or languageSV == 'English' or languageSV == 'E':
                break

            print('No command named "%s"! please try again!!' % (languageSV))
            print('language setting:(한국어 or English)')
            languageSV = input()

        if languageSV == '한국어' or languageSV == '한':
            print('---환영합니다!---')
            MAIN_ZFR.main한()

        elif languageSV == 'English' or languageSV == 'E':
            print('---Hello~!---')
            MAIN_ZFR.mainE()




MAIN_ZFR.main()