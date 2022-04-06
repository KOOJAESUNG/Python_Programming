print("덧셈을 하고 싶은 양의 정수들을 입력하세요. 0입력시 종료: ")
sum = 0
while (True):
    num = int(input())
    if num == 0:
        break
    sum += num

print("총 합은", sum, "입니다.")
