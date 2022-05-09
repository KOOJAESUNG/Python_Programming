list = []
sum = 0
for i in range(5):
    print(i + 1, "번째 학생 성적 입력:", sep="", end="")
    score = int(input())
    list.append(score)
    sum += score
for i in range(5):
    print(i + 1, "번 학생 성적", list[i])
print("성적 합계:", sum)
print("성적 평균:", sum / 5)
