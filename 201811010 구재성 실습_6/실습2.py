def ticket(area):
    if area=="춘천":
        return 5000
    elif area=="부산":
        return 30000
    elif area=="대구":
        return 20000
    elif area=="수원":
        return 10000

print("춘천(운임:5000원)/부산(운임:30000원)/대구(운임:20000원)/수원(운임:10000원)")
area=input("목적지를 입력하시오: ")
print("%s까지의 금액은 %d원입니다."%(area,ticket(area)))