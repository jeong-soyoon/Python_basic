# 9-1 클래스
# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린" # 유닛 이름
hp = 40 # 유닛 체력
damage = 5 #유닛 공격력

# 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데 일반/시즈
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

def attack(name, location, damage):
    print("{0} : {1}방향으로 적군을 공격합니다. [공격력 : {2}]".foramt(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 많은 유닛들을 만들어야 하기 떄문에 클래스 필요
# 클래스를 붕어빵 틀에 비교
# 클래스 : 연관이 있는 변수와 함수의 집합 

class Unit: # init 메서드의 첫번째 매개변수 self에는 해당 메서드를 호출한 객체가 전달됨
    def __init__(self, name, hp, damage): # __init__ : 파이썬에서 쓰이는 생성자(객체가 생성될 때 자동으로 호출되는 메서드)
        # 객체에 초깃값을 설정해야 할 필요가 있을 때는 생성자를 구현
        self.name = name # 객체에 객체변수 name이 생성되고 값이 저장된다.
        self.hp = hp # 객체에 객체변수 hp가 생성되고 값이 저장된다.
        self.damage = damage # 객체에 객체변수 damage이 생성되고 값이 저장된다.
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5) # Unit 클래스로 만든 객체 marine1 (marine1은 Unit의 인스턴스)
marine2 = Unit("마린", 40,5) # Unit 클래스로 만든 객체 marine2
tank = Unit("탱크", 150, 35) # Unit 클래스로 만든 객체 tank

# 레이스 : 공중 유닛, 비행기, 
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith.damage))
# 마인드 컨트롤 : 상대방 유닛 내것으로 
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True # 외부에서 객체변수를 만들 수 있음(독립적으로)

if wraith2.clocking==True: 
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

from random import *
class Unit: # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name 
        self.hp = hp 
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0}  : {1} 방향으로 이동합니다. [속도 : {2}]"\
            .format(self.name,location, self.speed))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp<=0:
            print("{0} : 파괴되었습니다.".format(self.name)) 

class AttackUnit(Unit): # 공격 유닛(Unit 상속)
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) 
            # self. 붙어 있는 것은 기존의 멤버변수, 없는 것은 전달받음
# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    # 스팀팩 : 이동, 공격 속도 증가, 체력 10 감소 
    def stimpack(self):
        if self.hp>10:
            self.hp -=10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 더 높은 파워로 공격, 이동은 하지 않음
    seize_developed = False # 시즈모드 개발 여부
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_developed==False:
            return 
        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode==False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage*=2
            self.seize_mode = True 
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage/=2
            self.seize_mode = False
# 드랍쉽 : 공중 유닛, 수송기, 공격기능x
# 날 수 있는 기능을 가진 클래스
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
            .format(name,location,self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 레이스
class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20 , 5)
        self.clocked = False # 클로킹모드 (해제 상태)
    def clocking(self):
        if self.clocked ==True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

 # 실제 게임 진행
game_start() 
m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = wraith()
 
 # 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

 # 전군 이동
for units in attack_units:
    units.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (탱크 : 시즈모드, 레이스 : 클로킹, 마린 : 스팀팩)
for unit in attack_units:
    # isinstance(object, class) : 특정 클래스의 인스턴스인지 확인하는 함수
    if isinstance(unit, Marine)==True:
        unit.stimpack()
    elif isinstance(unit, Tank)==True:
        unit.set_seize_mode()
    elif isinstance(unit, wraith)==True:
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,20))

# 게임 종료
game_over()
