"""
[로또번호 생성기]
1. 1~45사이에 6개의 랜덤 숫자를 만들어 준다.

2. 6개 모두 생성이 되면 아래와 같은 화면으로 출력한다.
로또번호 : [1, 3, 9, 14, 22, 38]
"""
import random
"""
print(random.randrange(1,10)) #1부터 10미만의 숫자랜덤
print(random.randint(1,10)) #1부터 10까지 범위내의 숫자 랜덤
print(random.choice("happy")) #happy 문자열 문자 랜덤
print(random.choice([3,7,13,45])) #리스트 랜덤
"""

lotto_list = []

for i in range(1,7): #6개의 숫자 생성을 위한 반복
    value = 0
    print(i,"번째 숫자 생성")
    while True: #랜덤 숫자 반복 생성
        value = random.randrange(1,46) #랜덤 숫자 생성
        if lotto_list.count(value) == 0:
            print("새로운 숫자는 :",value)
            lotto_list.append(value)
            break #중복이 아니면 반복 중단

        print("중복숫자 :",value)

print("로또번호 :",lotto_list)
