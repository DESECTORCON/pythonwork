import sys, time # 필요한 모듈 인푸트
user_whis_list = [] # 사용자가 원하는 이밴트
points = 1000 # 사용자가 가지고 있는 포인트
event_t = '''--------------------s.e event--------------------------
            --1 안마 ==== 1개당 10원
            --2 커피 ==== 400원''' # 이밴트 항목(프린트물)
event_point = {'안마':10, '커피':400} # 이밴트 항목 딕셔너리

event_points = open("event_points_demo", 'w') # 파일 만들기

# s.e 회원 인지 물어봄. 
print('당신은 s.e에 가입하셨습니까?(y or yes or n or no)')
user_i_input = input()
if user_i_input == 'n' or user_i_input == 'no':
    sys.exit() # 회운이 아니면 프로그램 종료.
elif user_i_input == 'y' or user_i_input == 'yes':
    
    #회원이면 하고싶은 이밴트를 골르게 하고 그 이밴트의 가격을 points 에서 뺀다.
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
        
        # user_whis_list 을 리해드하는곳
        input_exit = input()
        if input_exit == 'T':
            break
        else:
            print('user의 남은 포인트:' + str(points))
            time.sleep(1.5)

# 리해드를 했을때 프린트를 하는곳
print('user의 남은 포인트: ' + str(points))
print('user의 위시 리스트: ' + str(user_whis_list))
