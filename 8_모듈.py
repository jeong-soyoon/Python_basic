# 11 모듈 : 함수나 변수 또는 클래스를 모아놓은 파일
import theater_module
theater_module.price(3) # 3명이서 영화를 보러 갔을 때 가격
theater_module.price_morning(4)
theater_module.price_soldier(5)

import theater_module as mv # 모듈의 별명 붙여주기
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
# 앞에 theater_module. 없이 모듈 내 모든 것을 사용하겠다는 읨
price(3)
price_morning(4)
price_soldier(5)

# 3명 가격은 30000원입니다.
# 4명 조조할인 가격은 24000원입니다.
# 5명 군인 할인 가격은 20000원입니다.

from theater_module import price, price_morning
# import 뒤에 사용할 함수만 적어 불러올 수 있음
price(5)
price_morning(6)
# 5명 가격은 50000원입니다.
# 6명 조조할인 가격은 36000원입니다.

from theater_module import price_soldier as price
# 모듈 안의 함수에게 별명 붙여주기
price(5)

import travel.thailand
# 패키지 travel에 있는 모듈 thailand 불러오기
trip_to = travel.thailand.ThailandPackage()
# 모듈 thailand의 클래스 ThailandPackage 객체 생성
trip_to.detail()
#[태국 패키지 3박 5일] 방콕, 파타야 여행(야시장 투어) 50만원

from travel.thailand import ThailandPackage
# travel.thailand 모듈에서 ThailandPackage 클래스 불러오기
trip_to = ThailandPackage()
# 모듈 thailand의 클래스 ThailandPackage 객체 생성
trip_to.detail()
#[태국 패키지 3박 5일] 방콕, 파타야 여행(야시장 투어) 50만원

from travel import vietnam
# travel 패키지에서 vietnam 모듈 불러오기
trip_to = vietnam.VietnamPackage()
# vietnam 모듈의 VietnamPackage 클래스 객체 생성
trip_to.detail()
# [베트남 패키지 3박 5일] 다낭 효도 여행 60만원

# 11-3 __all__
# __init__.py 파일을 __all__ =["thailand"]로 수정
# __init__.py 파일에 __all__ 변수를 설정하고 import 할 수 있는 모듈을 정의
# __all__이 의미하는 것은 패키지에서 *기호를 사용하여 import할 경우
# 이곳에 정의된 모듈만 import된다는 의미이다.
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 11-5 패키지, 모듈 위치
import inspect
from travel import *
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))


# 11-6 pip install : pip로 패키지 설치
# pypi.org에서 다양한 패키지를 제공
# pip show beautifulsoup4 : 패키지의 정보들을 터미널에 보여줌

# input : 사용자 입력을 받는 함수
# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시

# 외장함수
# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
# os : 운영체제에서 제공하는 기본 기능
# import os

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # 폴더 삭제
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# # time : 시간 관련 함수
# import time
# print(time.localtime())
# #time.struct_time(tm_year=2021, tm_mon=1, tm_mday=18, tm_hour=23, tm_min=9, tm_sec=49, tm_wday=0, tm_yday=18, tm_isdst=0)

# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# # 2021-01-18 23:09:49
