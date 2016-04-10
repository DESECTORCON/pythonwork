''':param
my Functions file.'''
import time

def mylicense(licq=True,licq2=False):
    print('s.e license:')
    print('s.e ver-11.4')
    print('s.e new update finding...')
    time.sleep(3)
    print('s.e update info:')
    print(' s.e updateing...')
    o = open('updatefile.txt', 'r')
    updateinfo = o.read()
    print(' updateinfo:')
    print(' ' + updateinfo)
    print(' update OK~!')
    print()

mylicense()