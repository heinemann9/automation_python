#파이썬 사칙연산

a = 5
b = 3
c = a + b

print(c)
print("a+b =",a+b)
print("a-b =",a-b)
print("a*b =",a*b)
print("a/b =",a/b)
print("a%b =",a%b)
print("a**b =",a**b)

d = (a+b)*b
e = a+b*b
print(d,e)

#등식,부등식
print("a == b :",a == b)
print("a != b :",a != b)
print("a < b :",a < b)
print("a >= b :",a >= b)

#수정대입연산자

f = 1
print("f :",f)
f = f + 1
f += 1  #코드를 줄여서 사용 (윗줄과 동일)
print("f :",f)
f *= 3
print("f :",f)

"""
여러줄 주석을 만들 수 있음.
"""
'''
여러줄 주석이 됩니다.
'''
g = """여러줄의 문자열을 입력할 때도 
사용됩니다.
"""
print("g :",g)


#자료형
h = 5
i = -365
j = 3.141592
k = "문자열"
l = "100"

print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(int(l)))

print("h+i=",h+i)
print("h+j=",h+j)
print("h+l=",h+int(l)) #자료형을 바꿔서 연산 가능
print("h*k=",h*k) #문자열과 곱셈을 할 경우는 반복 출력
print("k+l=",k+l)
print("'2'+'2'=",'2'+'2') #문자열끼리 덧셈은 합쳐서 출력

print("값","Hello") #콤마를 통해 출력 스페이스 공백 추가
print("값"+"Hello") #문자열끼리 덧셈은 빈 공백 없이 합침

m = [1,2,3,"a"] #<class 'list'>
o = (1,2,3,"a") #<class 'tuple'>
p = {"name":"홍길동","age":24} #<class 'dict'>
q = {1,2,3,4} #<class 'set'>
r = True #<class 'bool'> True, False 만 사용 (대문자 시작)
s = "True"
print(type(m))
print(type(o))
print(type(p))
print(type(q))
print(type(r))
print(type(s))


#문자열
t = "Spider-Man's best friend is Ned Leeds"
u = """ "Spider-Man's best friend" is Ned Leeds' """
v = 'Spider-Man\'s best friend is Ned Leeds'
w = 'Spider-Man\'s\n best friend\n is Ned\t Leeds'
print(t)
print(u)
print(v)
print(w)

