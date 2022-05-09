score = []
_class = ["국어", "영어", "수학"]
sum = [0, 0, 0]

for i in range(3):
    kem = []
    for k in range(3):
        print(i + 1, "번 학생 ", _class[k], " 성적 입력:", sep="", end="")
        kem.append(int(input()))
        sum[k] += kem[k]
    score.append(kem)

print("번호  국어  영어  수학")
print("----------------------")
for i in range(3):
    print("%3d" % (i + 1), end="")
    for k in score[i]:
        print("%5d" % k, end="")
    print("")

print("----------------------")
print("평균", end="")
for i in sum:
    print("%5.1f" % (i / 3), end="")
