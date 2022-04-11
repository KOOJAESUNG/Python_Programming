user_str = input("문자열을 입력하시오: ")
upper_str = ""
for i in user_str:
    upper_str = upper_str + chr(ord(i) - 32)

print(upper_str)
