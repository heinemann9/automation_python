print("Hello") # print함수에 아래의 end="\n"옵션이 생략 되어 표현
print("Hello", end="\n") 


#반복문 While
count = 1
while count <= 10: #count가 10이하 일 경우에 반복해.
    print(count, end=" ")
    count += 1  #count = count + 1 

print("\n")

counta = 1
while True: #무조건 반복해
    if counta > 10:  #count가 10이상이면
        break       #반복을 중단해
    else:           #그렇지 않으면
        print(counta, end=" ")
    counta += 1

print("\n")

countb = 0
while countb < 10: #count가 10이하 일 경우에 반복해.
    countb += 1  #count = count + 1 
    if countb % 2 == 0: #countb를 2로 나누어 몫이 0인 경우 = 짝수
        continue #현재 반복을 중단하고 다음 반복으로 이동.
    else:
        print(countb, end=" ")

print("\n")

#for 반복문
    
fruits = ["사과", "바나나", "체리"]

for fruit in fruits: #fruit 리스트 내의 값을 순차적으로 fruit에 반환
    print(fruit, end=" ")

print("\n")

for i in range(5): #range(5) / range(0,5)는 0부터 5이전까지 순차적으로 반환
    print(i, end=" ")

print("\n")

for j in range(2, 5):
    print(j, end=" ")

print("\n")

for j in range(1, 10, 2): #range(시작,종료,간격)
    print(j, end=" ")

print("\n")

#for range 용법

for i in range(len(fruits)): #fruit 리스트 내의 값을 순차적으로 fruit에 반환
    print(fruits[i], end=" ")
