n = int(input("숫자를 입력하시오: "))
sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum += i

print(sum)
