num = int(input("10진수를 입력하시오: "))
binary = ""
while (num / 2 != 0):
    binary = str(num % 2) + binary
    num = num // 2

print(binary)
