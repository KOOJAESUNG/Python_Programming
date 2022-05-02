def calculator(x, y, case):
    if case == 1:
        return x + y, "+"
    elif case == 2:
        if x > y:
            return x - y, "-"
        else:
            return y - x, "-"
    elif case == 3:
        return x * y, "*"
    elif case == 4:
        return x / y, "/"


while True:
    case = int(input("1.덧셈 2.뻴셈 3.곱셉 4.나눗셈 5.종료"))
    if case == 5:
        break
    num1 = float(input("정수 1:"))
    num2 = float(input("정수 2:"))
    if case == 4 and num2 == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        result, a = calculator(num1, num2, case)
        if case == 2 and num1 < num2:
            print("%.2f %s %.2f = %.2f" % (num2, a, num1, result))
        else:
            print("%.2f %s %.2f = %.2f" % (num1, a, num2, result))
