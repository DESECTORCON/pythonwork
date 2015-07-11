import turtle

t = turtle.Pen()
# 얼만큼 동그라미를 그릴건지 물어봄.
number_of_circles = int(turtle.numinput("동그라미의 수",
                                        "얼만큼 동그라미를 그려주기를 원함니까?",6))
for x in range(number_of_circles):
    t.circle(100)
    t.left(360 / number_of_circles)

input("")