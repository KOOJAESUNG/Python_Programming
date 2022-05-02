def square(X, Y):
    result = 1
    for i in range(Y):
        result *= X
    return result


X = int(input("밑:"))
Y = int(input("지수:"))
print("거듭제곱값: %d" % square(X, Y))
