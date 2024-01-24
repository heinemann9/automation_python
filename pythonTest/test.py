#문자열 포매팅
print("안녕","하세요")
print("안녕"+"하세요")
print("저는",7,"번 입니다")

age = 30
w = 70

# %s
print("제 나이는 %s세이고 몸무게는 %skg입니다" % (age,w))

#format
print("제 나이는 {a}세이고 몸무게는 {b}kg입니다.".format(b=w,a=age))
print("제 나이는 {age}세이고 몸무게는 {w}kg입니다.".format(age=age,w=w))

#f (파이썬 3.6버전 이상)
print(f"제 나이는 {age}세이고 몸무게는 {w}kg입니다.")

name = "happy"
print(f"=={name}==")
print(f"=={name:10}==") #범위의 너비를 10이라는 공간을 할당 (정렬:기본-좌측)
print(f"=={name:>10}==") #우측정렬
print(f"=={name:<10}==") #좌측정렬
print(f"=={name:^10}==") #중앙정렬
print(f"=={name:+^10}==") #문자를 추가하면 빈 공간을 문자로 대체

#리스트 
a = [1,2,3,4,5] 
#    0 1 2 3 4 위치(index)값
b = ["a","b","c"]

print(a[1])
print(a[:2]) #0의 위치에서 2 이전의 위치까지 보여주기
print(a+b)
print(a*2)
print(len(a)) #a 리스트 길이
print(type(a))

a[2] = 6    #리스트 값 수정
del a[1]    #리스트 값 삭제
print("a :",a)

a.append(7) #a.append(값) 리스트에 값 추가 - 맨 뒤로 붙어
print("a.append(7) :",a)
a.reverse() #뒤집기 (역순정렬 아님)
print("a.reverse() :",a)
a.sort() #정렬(순차정렬)
print("a.sort() :",a)
a.sort(reverse=True) #정렬(역순정렬)
print("a.sort(reverse=True) :",a)

print(a.index(5)) #인덱스 값 반환
a.insert(4,5)
print("a.insert(4,5) :",a) #위치에 값 삽입 a.insert(위치,삽입할 값)
a.remove(5)
print("a.remove(5) :",a) #찾는 값 삭제 - 처음 나오는 값
print("a.pop()은 요소 추출 반환 :",a.pop())
print("a.pop() :",a) #요소 추출(삭제 및 반환)
print("a.pop(1)은 요소 추출 반환 :",a.pop(1))
print("a.pop() :",a) #위치 요소 추출(삭제 및 반환)

print(a.count(7)) #값을 찾아 카운팅
a.extend(b) #a 리스트에 b를 추가 확장
print("a.extend(b) :",a)

#=================================
a_list = []
for i in range(1,11): #1부터 10까지
    a_list.append(i)
    
    
#딕셔너리 - 키값(key)과 값(value)을 쌍으로 가짐
#           키(key)값은 변하지 않는 값으로 설정이 가능
a_dict = {"a":"apple", "b":"반하나", 1:"하나", "둘":2, (1,2,3):"일,이,삼"}
print(a_dict["a"]) #a_dict[키값]
print(a_dict["b"])
print(a_dict[1])
print(a_dict[(1,2,3)])

print(a_dict.keys())
print(a_dict.values())

a_list_dict = list(a_dict.keys())
print(a_list_dict)

a_dict.clear() #딕셔너리 초기화
print(a_dict)