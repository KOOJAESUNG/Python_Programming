fact_num = int(input("양의 정수를 입력하시오: "))
fact = 1
while (fact_num >= 1):
    fact = fact * fact_num
    fact_num = fact_num - 1

print("입력한 정수의 factorial값은", fact, "입니다.")
