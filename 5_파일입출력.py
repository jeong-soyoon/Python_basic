#8-1
print("python", "java","javascript", sep = " vs ")
# sep을 지정해주면 띄어쓰기 대신 sep값이 들어감
print("python", "java","javascript",end="?")
print("무엇이 더 재미있을까요?")
# end를 지정해주면 문장의 끝에 \n 대신 end값이 들어감

import sys 
print("python", "java", file = sys.stdout)
# 표준 출력
print("python", "java", file = sys.stderr)
# 표준 에러

scores = {"수학":90, "영어":50, "코딩":100}
for subject, score in scores.items(): 
    #dic.items() : key와 value를 쌍으로 나옴
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":")
    # rjust(n) : n개의 공간 확보 후 오른쪽 정렬
    # ljust(n) : n개의 공간 확보 후 왼쪽 정렬

#001, 002, 003 ...
for num in range(1,21):
    print("대기번호 : "+ str(num).zfill(3))
    # xfill(n) : n개의 공간 확보 후 빈 공간에 0

answer = input("아무값이나 입력하세요 : ")
# input() : 값을 문자열 형태로 입력받기 
print("입력하신 값은 "+answer+"입니다.")

8-2
# 10자리 공간 확보, 오른쪽 정렬, 빈 자리는 빈공간
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
왼쪽 정렬, 빈 자리는 _
print("{0:_<+10}".format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))
# 3자리마다 콤마를 찍어주기, 부호붙이기
print("{0:+,}".format(1000000000000))
# 3자리마다 콤마를 찍어주기, 부호붙이기, 자리수 확보, 빈자리는 웃는표시
print("{0:^<+30,}".format(1000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수까지만 표시
print("{0:.2f}".format(5/3))

8-3
score_file = open("score.txt", "w", encoding= "utf8")
# 파일 오픈, WRITE
print("수학 : 0",file = score_file)
print("영어 : 50",file= score_file)
# 파일에 쓰기(자동줄바꿈)
score_file.close()
# 파일 닫기

score_file = open("score.txt", "a", encoding= "utf8")
# 쓰기 용도가 아니라 APPEND로 이어쓰기 
score_file.write("과학 : 80\n") #print가 아니기 때문에 줄바꿈 해줘야 함
score_file.write("코딩 : 100")
score_file.close()

# 한꺼번에 읽기
score_file = open("score.txt", "r", encoding = "utf8")
# 파일 오픈, READ
print(score_file.read())
score_file.close()

# 몇줄인지 알때 줄별로 읽기
score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline(), end = "") #줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
score_file.close

# 몇줄인지 모를때 줄별로 읽기->반복문 이용
score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

# 몇줄인지 모를때 줄별로 읽기->리스트 형태로 저장 후 반복문 이용
score_file = open("score.txt", "r", encoding = "utf8")
lines= score_file.readlines() #리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

8-4
import pickle
profile_file = open("profile.pickle", "wb")
# wb : 바이너리 (피클을 쓰기 위해서는 바이너리 타입필요)
profile = {"이름":"정소윤", "나이":"22", "취미":["코딩", "독서", "산책"]}
print(profile)
pickle.dump(profile, profile_file)
# profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
# file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

8-5 with
import pickle
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# profile.pickle을 열어서 profile_file에 저장해두고
# file에 있는 정보를 불러와 출력

with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("안녕하세요 눈이 오네요")

# study.txt를 열어서 study_file에 저장해두고
# 내용 쓰기

with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file.read())

# with을 이용하면 간결한 코딩 가능하고 할 때마다 file.close() 안해도 됨

# 퀴즈 8
for i in range(1,6):
    report_file = open(f"{i}주차.txt", "w", encoding = "utf8")
    print(f"- {i}주차 주간 보고 -",file = report_file)
    print("부서 :",file = report_file)
    print("이름 :",file = report_file)
    print("업무 요약 :", file = report_file)
    report_file.close()

for i in range(1,51):
    with open(str(i)+"주차.txt", "w", encoding = "utf8") as report_file:
        report_file.write(f"- {i}주차 주간 보고 -")
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
    