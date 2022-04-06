apple=int(input("사과 수: "))
grape=int(input("포도 수: "))
pear=int(input("배 수: "))
mandarin=int(input("귤 수: "))

sum=apple+grape+pear+mandarin

if(grape>=3):
    sum*=0.9

print("가격:",sum)