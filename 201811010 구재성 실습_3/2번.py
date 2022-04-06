num = int(input("양의 정수를 입력하시오: "))
i = 0
sum = 0
while (i <= num):
    if i % 2 == 0:
        sum += i
    i += 1

print("짝수의 합:", sum)
