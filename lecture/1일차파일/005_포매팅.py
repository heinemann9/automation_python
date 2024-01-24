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
print(f"=={name:+^10}==") #중앙정렬