print("===좋아하는 과일 등록 프로그램===")
print("0을 입력하면 입력 종료")
list = []
while (True):
    fruit = input("과일명 입력: ")
    if fruit == '0':
        break
    list.append(fruit)
print("당신이 좋아하는 과일들:", list)
