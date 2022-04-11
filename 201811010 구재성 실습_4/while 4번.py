user_str = input("문자열을 입력하시오: ")
reverse = ""
i = 0

while (i < len(user_str)):
    reverse = user_str[i] + reverse
    i += 1

print(reverse)
