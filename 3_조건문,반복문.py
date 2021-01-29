weather = input("오늘 날씨는 어때요? ")
if weather == "비":
    print("우산을 챙기세요")
elif weather =="미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비믈이 필요없어요")

temp = int(input("기온은 어때요? "))
if temp>=30 : 
    print("너무 더워요 나가지 마세요")
elif temp>=10 and temp<30:
    print("괜찮은 날씨에요")
elif temp>=0 and temp<10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")

students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

students = ["iron man", "thor", "i am groot"]
students = [len(i) for i in students]
print(students)

students = ["iron man", "thor", "i am groot"]
students = [i.upper() for i in students]
print(students)

for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

from random import *
total=0
for customer in range(1,51):
    time = randint(5,50)
    if 5<=time<=15:
        total+=1
        print(f"[o] {customer}번째 손님 (소요시간 : {time}분) ")
    else:
        print(f"[ ] {customer}번째 손님 (소요시간 : {time}분) ")

print("총 탑승 승객 : {0}분".format(total))
