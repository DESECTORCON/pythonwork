import time

def stopwatch():
    print('press ENTER ot start!')
    input('')
    timeV = 0
    try:
        while True:
            time.sleep(1)
            timeV += 1
            print('%s sec!' % (timeV))
    except KeyboardInterrupt:
        print('Interrupted!')
        return