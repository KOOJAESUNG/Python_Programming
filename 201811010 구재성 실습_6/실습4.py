def is_prime(x):
    for i in range(2,x):
        if x%i==0:
            print("소수가 아닙니다.")
            return 0
    print("소수입니다.")

x=int(input("정수를 입력하시오: "))
is_prime(x)
