value1=int(input("첫번째 양의 정수를 입력하시오: "))
print("\n")
value2=int(input("두번째 양의 정수를 입력하시오: "))
print("\n")
value3=int(input("세번째 양의 정수를 입력하시오: "))
print("\n")

max=value1

if(max<value2):
    max=value2
    if(max<value3):
        max=value3
elif(max<value3):
    max=value3

print("가장 큰 수:",max,"\n")


