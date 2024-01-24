#함수는 여러번 재 사용의 목적으로 함
def add(a,b):       #add이름의 함수를 정의, 매개변수 a,b
    result = a+b    #return값에 a+b를 넣고
    return result   #return 값을 반환

print(add(5,3))     #add라는 함수를 호출, 5,3을 전달

def cal(a,b):
    a_sum = a+b
    b_sum = a-b
    c_sum = a*b
    d_sum = a/b
    return a_sum, b_sum, c_sum, d_sum

e_tuple = 8, 2, 15, 1.6 #변수 하나에 여러값을 입력하면 tuple로 입력 됨
print(e_tuple)

print(cal(5,3))
print(cal(15,7))
print(cal(100,4))
print(cal(1,7))

#가변적 매개변수
def cals(*args): #매개변수가 가변적
    total = 0
    for num in args:
        total += num
    return total

print(cals(1,2,3,4,5,6,7,8,9,10))

def a_cals(a,*args): #하나의 값은 고정, 이후 가변
    total = 0
    for num in args:
        total += num

    return a+total

print(cals(100,1,2,3,4,5,6,7,8,9,10))


#전역 변수 global

g_sum = 0

def gsum():
    global g_sum
    g_sum += 5

print(gsum())
print(gsum())
print(g_sum)