animal = "강아지"
name = "연탄이"
age = 4
hobby= "산책"
is_adult = age>=3

print("우리집 "+animal+"의 이름은 " +name+"에요")
print(name+"는 "+str(age)+"살이며 "+hobby+"을 아주 좋아해요")
print(name+"어른일까요?"+str(is_adult))

station = "사당"
print(station+"행 열차가 들어오고 있습니다.")
station = "신도림"
print(station+"행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station+"행 열차가 들어오고 있습니다.")


from random import *

print(int(random()*45)+1) # 1~45 이하의 임의의 정수 생성
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)
print(int(random()*45)+1)

from random import *

date = randrange(4, 29) # 4~28까지의 정수 생성
print("오프라인 스터디 모임 날짜는 매월 "+str(date)+"일로 선정되었습니다.")

sentence = """
저는 경시대회 수상했어용
파이썬을 배우고 싶어요
"""
print(sentence)

jumin = "000409-1234567"

# 필요한 부분만 잘라서 사용하는 것을 슬라이싱이라고 합니다~~!

print("성별 : "+ jumin[7])
print("연 : "+jumin[0:2]) #0~2 직전까지(0,1)
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])
print("생년월일 : "+jumin[:6]) #처음부터 6 직전까지
print("뒤 7자리 : "+jumin[7:]) #7부터 끝까지
# print("뒤 7자리(뒤에부터) : "+jumin[-7:]) #맨 뒤에서 7번째부터 끝까지


python = "Python is amazing"
print(python.lower())
print(python.upper())
print(python[4].upper())
print(len(python))
print(python.replace("Python", "C"))
index = python.index("a")
print(index)
index = python.index("a", index+1)
print(index)

print("나는 %d살입니다"%21)
print("나는 %s를 좋아해요."%"치킨")
print("soyoon은 %c로 시작해요"%"s")
#%s
print("나는 %s살입니다."%21)
print("나는 %s색과 %s색을 좋아해요"%("파란", "흰"))
print("나는 {}살입니다.".format(21))
print("나는 {}색과 {}색을 좋아해요".format("파란", "흰"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "흰"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color = "파란", age = 21))
age = 21
color = "파란"
print(f"나는 {age}살이며, {color}색을 좋아해요")

print("백문이 불여일견 \n 백견이 불여일타")
print("Red apple\rpine")
print("pinee\bapple")
print("pine\tapple")

#site = "https://naver.com"
site = "https://daum.net"
# 슬라이싱
site= site[8:]
site = site[:site.index(".")]
password = site[:3] + str(len(site))+str(site.count("e"))+"!"
print(f"생성된 비밀번호 : {password}")
# 문자열 처리 함수 replace() 사용
site = site.replace("https://","")
site = site.replace(".com","")
password = site[:3] + str(len(site))+str(site.count("e"))+"!"
print(f"생성된 비밀번호 : {password}")