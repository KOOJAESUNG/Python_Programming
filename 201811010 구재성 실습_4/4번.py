user_str = input("문자열을 입력하시오: ")
reverse = ""

for i in user_str:
    reverse = i + reverse

if user_str == reverse:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
