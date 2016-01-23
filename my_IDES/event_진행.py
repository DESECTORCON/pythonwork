import sys, time
now = time.localtime()
coupon_main_data = '과자 -100%- 할인쿠폰|커피 -100%- 할인쿠폰'
coupon_1 = '''|---------------------------------------------------------|'''
coupon_2 = '''|==================s.e coupon room========================|'''
coupon_3 = '|' * 9
coupon_tk_i1 = {'과자':500, '커피':400, '심부름':1000}
coupon_tk_i = ['과자', '커피', '심부름']
event_tk = '''--------------------s.e event--------------------------
            --1 과자 ==== 500원
            --2 커피 ==== 400원
            --3 심부름 ==== 1000원'''
event_tk_i1 = {'과자':500, '커피':400, '심부름':1000, '쿠폰방':0, 'coupon':0}
event_tk_i = ['과자', '커피', '심부름']
e = open('event_point_loker', 'w')
point = 1000
demo_data = [1000 ,0, 0]
domo_data = "<<<|%04d-%02d-%02d %02d:%02d:%02d|%s|%s|%s|>>>" % (now.tm_year,
                now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec,
                demo_data[0], demo_data[1], demo_data[2])


def coupon_data_maker(data_list):
    now = time.localtime()
    data_demo = "<<<|%04d-%02d-%02d %02d:%02d:%02d|%s|>>>" % (now.tm_year,
                now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec,
                data_list)
    return data_demo


def buy_data_maker(data1, data2, data3):
    now = time.localtime()
    data_demo = "<<<|%04d-%02d-%02d %02d:%02d:%02d|%s|%s|%s|>>>" % (now.tm_year,
                now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec,
                data1, data2, data3)
    return data_demo


def end_plus_points_or_plus_points(i_use_points1):
    return i_use_points - 150


def test(i_use_points, event_tk_i1):

    i_use_points = end_plus_points_or_plus_points(i_use_points)
    if user_input == 'y' or user_input == 'yes':
        i_use_points - i
    res = int(points1_split[2]) - i_use_points
    e = open('event_point_loker', 'w')
    e.write(buy_data_maker(res, i_use_points, points1_split[2]))
    print('---결제 정보--')
    print('쓴 돈: %s' % (i_use_points))
    print('남아있던돈: %s' % (points1_split[2]))
    print('지금 남아있는 돈: %s' % (res))
    print()


e.write(domo_data)
e.close()
print('당신은 s.e에 가입하셨습니까?(y or yes or n or no)')
user_i_input = input()

if user_i_input == 'n' or user_i_input == 'no':
    print('s.e에 가입하세요!')
    print('progame exit')
    sys.exit()

elif user_i_input == 'y' or user_i_input == 'yes':
    while True:
        e = open('event_point_loker', 'r')
        points = e.readline()
        points1 = ''

        for p in points:
            points1 += points
        e.close()

        points1_split = points1.split('|')
        print('당신은 지금 %s 포인트가 남아 있어요.' % (points1_split[2]))

        while True:
            print(event_tk)
            print('여기서 할 이밴트를 선택하시오')
            user_input = input()

            if user_input in event_tk_i:
                if event_tk_i1[user_input] <= int(points1_split[2]):
                    break
            elif user_input == 'no':
                break
            elif user_input == 'coupon' or user_input == '쿠폰방':
                c = open('coupon_files', 'w')
                coupon_data = coupon_main_data.split('|')
                coupon_data2 = coupon_main_data.split('-')
                c.write(coupon_data[0] + '\n')
                c.write(coupon_data[1])
                print(coupon_data2)
                print(coupon_1)
                print(coupon_2)
                print('   ', coupon_data[0], '\n', '  ', coupon_data[1])
                print('쿠폰을 적용하새겠습니까?')
                user_coupon_input = input()
                if user_coupon_input == 'y' or user_coupon_input == 'yes':
                    print('무슨 쿠폰을 적용하시겠습니까?')
                    user_coupon_input2 = input()
                    if user_coupon_input2 in coupon_data2:
                        for coupon in range(100000):
                            if coupon_data2[coupon] == '100%':
                                i1 = event_tk_i1[user_input]
                                i - i1
                                print('무료할인이 되었어요!')
                                break
                            elif coupon_data2[coupon] == '50%':
                                i = event_tk_i1[user_input]
                                i - 500
                                print(i, ' 원 할인이 되었어요!')
                                break
                            elif coupon_data2[coupon] == '30%':
                                i = event_tk_i1[user_input]
                                i - 100
                                print(i, ' 원 할인이 되었어요!')
                                break
                            elif coupon_data2[coupon] == '%':
                                i = event_tk_i1[user_input]
                                i - 50
                                print(i, ' 원 할인이 되었어요!')
                                break
                            else:
                                NameError('no 100% s')
                                print('adf')

                else:
                    break

            else:
                continue
        if user_input == 'no':
            print('opening data...')
            print('(This will take a few seconds...)\n')
            time.sleep(1)
            f = open('event_point_loker',  'r')
            line = f.readline()
            print(line)
            f.close()

            sys.exit()

        else:
            i_use_points = event_tk_i1[user_input]
            test(i_use_points, event_tk_i1)