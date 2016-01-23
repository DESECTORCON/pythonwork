import sys, time
user_whis_list = []
points = 1000
event_t = '''--------------------s.e event--------------------------
            --1 안마 ==== 1개당 10원
            --2 커피 ==== 400원'''
event_point = {'안마':10, '커피':400}

event_points = open("event_points_demo", 'w')

print('당신은 s.e에 가입하셨습니까?(y or yes or n or no)')
user_i_input = input()
if user_i_input == 'n' or user_i_input == 'no':
    sys.exit()
elif user_i_input == 'y' or user_i_input == 'yes':
    while True:
        print('당신의 포인트는 ' + str(points))

        event_points.write(str(points))

        print('이밴트 항목을 프린트하겠습니다.')
        print(event_t)
        print('무슨 항목을 선택하시겠습니까?')
        user_event = input()
        if user_event in event_point:
            print('내. 지금 이밴트를 진행하겠습니다.')
            event_points.write('\n' + str(points - event_point[user_event]))
        user_whis_list.append(user_event)
        input_exit = input()
        if input_exit == 'T':
            break
        else:
            time.sleep(1.5)

print('user의 남은 포인트: ' + str(points))
print('user의 위시 리스트: ' + str(user_whis_list))