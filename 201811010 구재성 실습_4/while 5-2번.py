binary_num = str(input("2진수를 입력하시오: "))
num = 0
k = len(binary_num)
i = 0
while (i < len(binary_num)):
    if binary_num[i] == '1':
        num = num + 2 ** (k - 1)
    k -= 1
    i += 1

print(num)
