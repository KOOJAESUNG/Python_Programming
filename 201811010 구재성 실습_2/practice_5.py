size=int(input("손가락 둘레를 입력하시오: "))

if(size>51 and size<=52):
    print("9호를 추천합니다.\n")
elif (size > 52 and size <= 53):
    print("10호를 추천합니다.\n")
elif (size > 53 and size <= 54):
    print("11호를 추천합니다.\n")
elif (size > 54 and size <= 55):
    print("12호를 추천합니다.\n")
else:
    print("제작 불가한 사이즈입니다.\n")
