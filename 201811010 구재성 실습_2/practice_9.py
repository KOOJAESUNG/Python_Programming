value1=int(input("첫번쨰 양의 정수를 입력하시오."))
print("\n")
value2=int(input("두번쨰 양의 정수를 입력하시오."))
print("\n")
value3=int(input("세번쨰 양의 정수를 입력하시오."))
print("\n")

if(value1+value2>value3)or(value1+value3>value2)or(value2+value3>value1):
    if(value1==value2==value3):
        print("정삼각형입니다.\n")
    elif(value1+value2==value3)or(value1+value3==value2)or(value2+value3==value1):
        print("이등변삼각형입니다.\n")
    elif (value1**2+value2**2==value3**2) or (value2**2+value3**2==value1**2) or (value1**2+value3**2==value2**2):
        print("직각삼각형입니다.\n")
    elif(value1==value2)or(value2==value3)or(value1==value3):
        print("일반삼각형입니다.\n")
else:
    print("삼각형이 아닙니다.")