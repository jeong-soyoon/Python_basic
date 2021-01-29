10-1 예외처리 : 에러가 발생했을 때 처리
try: #try안에서 에러가 발생하면 그 에러에 해당하는 except를 찾아 실행한다. 
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    #nums.append(int(num[0]/num[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: 
    print("에러! 잘못된 값을 입력하였습니다.")
    # 에러! 잘못된 값을 입력하였습니다.
except ZeroDivisionErrror as err:
    print(err)
    # division by zero
except Exception as err: # 나머지 에러에 대해
    print("알 수 없는 에러가 발생하였습니다.")
    print(err) #에러메시지 

# 10-2 에러 발생시키기, 10-3 사용자 정의 예외처리
class bignumbererror(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1>=10 or num2>=10:
        raise bignumbererror(f"입력값 : {num1}, {num2}") # 에러를 발생시킴
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except bignumbererror as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally: 
    print("계산기를 이용해 주셔서 감사합니다.")
# 10,5 입력하면
# 에러가 발생하였습니다. 한 자리 숫자만 입력하세요.
# 입력값 : 10, 5
# 계산기를 이용해 주셔서 감사합니다. 출력됨

# 퀴즈 10
chicken = 10
waiting = 1
class SoldOutError(Exception):
    pass
while(True):
    try:
        print("남은 치킨 : {0}".format(chicken))
        order = int(input("치킨 몇 마리를 주문하시겠습니까?"))
        if order<1:
            raise ValueError
        elif order>chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting+=1
            chicken-=order
        if chicken==0:
            raise SoldOutError
    except ValueError: #1보다 작거나 숫자가 아닌 입력값
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError: #치킨이 소진되었을 때
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break #프로그램 종료