import sys

def OFF(number=130):
    print('Do you really want to exit?')
    USRV = input()
    if USRV == 'y' or USRV == 'yes':
        sys.exit(number)