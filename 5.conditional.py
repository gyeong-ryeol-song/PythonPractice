# 조건문
# 조건문은 프로그램의 흐름을 제어하는 문법
# ex)

x=15
if x>=10:
    print("x>=10")
if x>=0:
    print("x>=0")

# 들여쓰기
# 파이썬에서 코드의 블록을 들여쓰기로 지정
# 파이썬 스타일 가이드라인에서는 4개의 공백문자를 사용하는 것을 추천

# 조건문의 기본형태
# 기본적 형태는 if ~ elif ~ else

a=5

if a>=0:
    print("a>=0")
elif a>= -10:
    print("0>a>=-10")
else:
    print("-10 > a")


# 비교연산자
# 같은지 다른지 비교 ->    == , !=
# 클 때 작을 때 ->    > , <
# 크거나 같을 때 작거나 같을 때 ->  >= , <=

#논리연산자
# X and Y : X,Y 모두 참일 때 True
# X or Y : X,y 중 하나만 참이어도 True
# not X : X가 거짓일 때 True

if True or False :
    print("Yes")

a= 15
if a<=20 and a>=0:
    print("Yes")


# 파이썬 기타 연산자
# 다수의 데이터를 담는 자료형을 위해 in 연산자와 not in 연산자가 제공됨
# 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용 가능
# ex)
# X in 리스트 : 리스트안에 X가 들어있을 때 True
# X not in 문자열 : 문자열에 X 가 들어있지 않을 때 True

# 파이썬의 pass 키워드
# 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용
# ex) 디버깅 과정에서 일단 조건문의 형태만 만들어놓고 조건문 처리부분을 비워두고 싶을 때
# ex)

score=85
if score>=80:
    pass
else:
    print("성적이 80점 미만입니다.")

print("프로그램을 종료합니다")


# 조건문의 간소화
# 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄 바꿈을 하지 않고도
# 간략하게 표현 가능
# ex)

score=85

if score>=80 : result="Success"
else: result = "Fail"
print(result)

# 조건부 표현식은 if ~ else문을 한 줄에 작성할 수 있도록 해줌
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

# 파이썬 조건문 내에서의 부등식
# 파이썬은 다른 언어와 다르게 조건문 안에서 수학 부등식을 그대로 사용할 수 있음
# ex)

x= 15
if x>0 and x<20:
    print("X는 0 이상 20 미만의 수입니다. ")

x = 15
if 0<x<20:
    print("x는 0 이상 20 미만의 수입니다. ")
