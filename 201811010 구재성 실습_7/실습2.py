print("친구 이름 등록 프로그램")
print("0을 입력하면 입력 종료")
list = []
while (True):
    friend = input("친구 이름 입력:")
    if friend == '0':
        break
    list.append(friend)
print("등록완료")
print("입력된 순서:", list)
list.sort()
print("정렬된 순서:", list)
