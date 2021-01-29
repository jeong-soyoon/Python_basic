cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
# print(cabinet.get(3))

menu = {"커피", "우유", "주스"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu

from random import *
users = list(range(1,21)) 
shuffle(users)  #리스트 섞는 함수 shuffle()
winners = sample(users, 4) #리스트에서 정해진 개수만큼 랜덤으로 뽑음
print("** 당첨자 발표 **")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print("** 축하합니다 **")
