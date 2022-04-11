user_str = input("문자열을 입력하시오: ")
reverse = ""
i = 0

while (i < len(user_str)):
    reverse = user_str[i] + reverse
    i += 1

if user_str == reverse:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
