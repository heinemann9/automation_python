#문자열
a = " Ho bby "
c = "abcdefg hijk lmn opqr st u vw xyz"
#    01234567  위치(index)값
#                 - 마이너스 위치  321
b ="h,o,b,b,y"


print(len(a)) #문자열 길이
print(a.count("b")) #문자 개수
print(a.find("b")) #문자 위치 찾기 (찾는 문자 없으면 -1 반환)
print(a.index("b")) #문자 위치 찾기 (찾는 문자 없음, 에러)
print(a.upper()) #대문자 변환
print(a.lower()) #소문자 변환
print("=="+a.rstrip()+"==") #우측 공백 지우기
print("=="+a.lstrip()+"==") #좌측 공백 지우기
print("=="+a.strip()+"==") #양측 공백 지우기
print(a.replace("Ho","To")) #문자열 바꾸기 (찾는값,바꿀값)
print(a.replace(" ",""))
print(b.split(",")) #문자열 분리를 해서 리스트에 입력
print(",".join(a)) #구분자 넣기

print(",".join(a.replace(" ","")))

print("a[1] =",a[1]) #문자 출력[인덱스]
print("a[1:3] =",a[1:3]) #문자 출력[시작 인덱스, 끝 인덱스(이전까지보임)]
print("a[4:7] =",a[4:7])
print("c[-3:] =",c[-3:])
print("a[-4:-1] =",a[-4:-1])
print("c[:7] =",c[:7])
print(a[1]+a[6])


#if 조건문 (조건이 하나일 때)
age = 18
if age >= 18: #나이가 18세 이상일 경우
    print("18세 이상 성인입니다.")
else: #그렇지 않으면 (18세 미만일 경우)
    print("미성년자 입니다.")

#if 조건문 (조건이 여러개일때)
score = 70
if score >= 90:  #점수가 90점 이상일 경우
    grade = "A"
elif score >= 80:  #점수가 80점 이상일 경우
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:   #위의 모든 조건이 아닌 경우
    grade = "F"

print("성적 :", grade)

#if문 and, or 
pocket = "card"
money = 5000
if pocket == "card" or money > 6000:
    print("택시타")
    print("빠르게 갈꺼야")
else:
    print("걸어가")

if pocket == "card" and money > 6000:
    print("택시타")
else:
    print("걸어가")

mypocket = ["paper", "cellphone", "money"] #리스트
if "money" in mypocket: #리스트 안에 money라는 값이 있다면
    print("택시타")
else:
    if money > 4000:
        print("버스타")
    else:
        print("걸어가")


#match (case)
value = 8

match value: #value 값에 해당하는 수행 (파이썬 3.10버전 이상)
    case 1: #value == 1 이라면
        print("1이야")
    case 2: #value == 2 이라면
        print("2이야")
    case 3:
        print("3이야")
    case 4:
        print("4이야")
    case _: #value가 위의 케이스에 없다면
        print("우리 case 중엔 없어")