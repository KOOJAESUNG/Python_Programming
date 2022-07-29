file = open("./movie_data.txt", "r", encoding='cp949')

mov = {}
label = ["Company", "Release date", "Country", "Total screen", "Profit", "Total num", "Grade"]

for line in file.readlines():
    line = line.strip()
    mov_data = line.split("|")
    mov[mov_data[2]] = [mov_data[3], mov_data[4], mov_data[5], mov_data[6], mov_data[7], mov_data[8],
                        mov_data[9]]

while True:
    mov_name = input("영화 이름 입력(종료 0):")

    if mov_name == "0":
        print("프로그램을 종료합니다")
        break

    if mov_name in mov.keys():
        data = mov[mov_name]
        for i in range(7):
            print("%s : %s" % (label[i], data[i]))
        print("----------------------------------------")
    else:
        print("데이터베이스에 없는 영화입니다.")
