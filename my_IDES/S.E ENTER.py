import sys
f = open("S-E.text", 'w')
f.close()
print('')
f = open("S-E.text", 'w')
print(f)

for i in range(3):
    user_data = input('사용자 이름을 입력하시오:')

    base_data = '사용자%d:%s' % (i, user_data)
    f.write(base_data)
    user_password = input(user_data + ' 님.비밀번호를 입력해 주세요:')

    base_data2 = '사용자%d비밀번호:%d\n' % (user_password)
    f.write(base_data2)

def __login__():
    f1 = open("S-E.text", 'r')
