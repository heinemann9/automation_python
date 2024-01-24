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


#튜플 자료형 - 수정이 안된다
a_tuple = (1,2,3)
print(a_tuple, type(a_tuple))
print(tuple(a_list))

print(a_tuple[1])

#튜플 데이터 가져오기
e,f,g = a_tuple #변수를 설정해서 튜플의 데이터 꺼내서 대입
print(e,f,g)

h_list = list(a_tuple) #튜플 데이터를 리스트로 변환
print(h_list)



#집합 자료형 - 순서가 없다.
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2) #교집합
print(s1 | s2) #합집합
print(s1 - s2) #차집합


#불 자료형
b1 = True
b2 = False

print(b1)
if b1 == "True":
    print("참")
else:
    print("거짓")