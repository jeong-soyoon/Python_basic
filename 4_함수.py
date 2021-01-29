# 7- 함수
def introduce(name, age, main_lang):
    print("제 이름은 {0}이고 나이는 {1}살이고 주 사용언어는 {2}입니다"\
        .format(name,age,main_lang))

introduce(main_lang= "C", age=22, name ="정소윤")
# 매개변수 순서대로 안해도 키워드값으로 전달

#전역변수 사용x -> 잘못된 예시
gun = 10
def checkpoint(soldiers):
    gun = gun- soldiers 
    #gun은 checkpoint 함수 안에서 만들어진 지역변수
    print("[함수 내] 남은 총 : {0}".format(gun))
print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

#전역변수 사용
gun = 10
def checkpoint(soldiers):
    global gun # 전역공간에 있는 gun 사용
    gun = gun- soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

# 전역변수 사용 안하고 같은 결과
gun = 10

def checkpoint_ret(gun, soldiers):
    gun =  gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))


def introduce(name, age, *language):
    print("제 이름은 {0}이고 나이는 {1}살이고 주 사용언어는"\
        .format(name, age), end = " ")
    for lang in language:
        print(lang, end=' ') 
        #end =' ' 이거 붙이면 붙여서 출력됨
    print()
introduce("정소윤", "21", "C", "python")
introduce("정히히", "20","java","kotlin", "swift")

def std_weight(height, gender):
    if gender == "여자":
        return height*height*21
    return height*height*22

height = 175
gender = "남자"
weight = round(std_weight(height/100,gender),2) 
# round(a,2)는 소수 둘째자리까지 반올림
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg입니다")
