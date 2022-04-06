value1=int(input("첫번쨰 양의 정수를 입력하시오."))
print("\n")
value2=int(input("두번쨰 양의 정수를 입력하시오."))
print("\n")
value3=int(input("세번쨰 양의 정수를 입력하시오."))
print("\n")

sum=value1+value2+value3

if(sum%2==0):
    max=value1
    if (max < value2):
        max = value2
        if (max < value3):
            max = value3
    elif (max < value3):
        max = value3
    print("가장 큰 수:", max, "\n")
else:
    print("합:",sum,"\n")




