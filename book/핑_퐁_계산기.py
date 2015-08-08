def convert_in2cm(inches):
    return inches * 2.54


def convert_lb2kg(pounds):
    return pounds / 2.2

height_in = int(input("자기의 키를 인치 단위로 입력하십시오:"))
weight_lb = int(input("자기의 몸무게를 파운드 단위로 입력하십시오:"))

height_cm = convert_in2cm(height_in)
weight_kg = convert_lb2kg(weight_lb)

ping_pong_tall = round(height_cm / 4)
ping_pong_heavy = round(weight_kg * 1000 / 2.7)

feet = height_in // 12
inch = height_in % 12

print("키는", feet, "피트", inch, "인치이고,무게는",weight_lb, "파운드입니다.")
print("키는 핑퐁볼로", ping_pong_tall, "이고,")
print("몸무게는 ", ping_pong_heavy, "개의 핑퐁볼무게랑 똑같슴니다!!!") 