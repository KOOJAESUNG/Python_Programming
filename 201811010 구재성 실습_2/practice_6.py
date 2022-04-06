print('''1.덧셈
2.뺄셈
3.곱셈
4.나눗셈''')

num=int(input("원하는 연산의 번호를 입력하시오:"))
print("\n")
if(not(num==1 or num==2 or num==3 or num==4)):
    print("잘못 입력했습니다.\n")
else:
    value1 = int(input("첫번째 양의 정수를 입력하시오: "))
    print("\n")
    value2 = int(input("두번째 양의 정수를 입력하시오: "))
    print("\n")
    if (num == 1):
        print(value1, "+", value2, "=", value1 + value2, "\n")
    if (num == 2):
        print(value1, "-", value2, "=", value1 - value2, "\n")
    if (num == 3):
        print(value1, "*", value2, "=", value1 * value2, "\n")
    if (num == 4):
        print(value1, "/", value2, "=", value1 / value2, "\n")
