# 함수
# 특정한 작업을 하나의 단위로 묶어 놓는 것을 의미
# 내장함수 : 파이썬이 기본적으로 제공하는 함수
# 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수
# 함수를 사용하면 소스코드의 길이를 줄일 수 있음
# 매개변수 : 함수 내부에서 사용할 변수
# 반환 값 : 함수에서 처리 된 결과를 반환

def add(a,b):
    return a+b

print(add(3,7))

def add(a,b):
    print("함수의 결과: ",a+b)
a=3
b=7
add(a,b)

# 파라미터 지정
# 파라미터의 변수를 직접 지정할 수 있음
# 이 경우 매개변수의 순서가 달라져도 상관 없음
# ex)

def add(a,b):
    print("함수의 결과: ",a+b)

add(b=3,a=7)

# global 키워드
# global 키워드로 변수를 지정하면 해당 함수에서는 지역변수를 만들지 않고,
# 함수 바깥에 선언된 변수를 바로 참조하게 됨

a=0

def func():
    global a
    a+=1

for i in range(10):
    func()

print(a)

# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있습니다.
#ex)

def operator(a,b):
    add_var = a+b
    subtract_var = a-b
    multiply_var = a*b
    divide_var = round(a/b,1)
    return add_var, subtract_var, multiply_var, divide_var

a,b,c,d=operator(7,3)
print(a,b,c,d)

# 람다 표현식
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징
# ex)

print((lambda a,b : a+b)(3,7))

# ex) 내장함수에서 자주 사용되는 람다함수
array = [('홍길동',50),('이순신',32),('아무개',74)]

def my_key(x):
    return x[1]

print(sorted(array,key=my_key))
print(sorted(array, key=lambda x:x[1]))

# ex)
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a,b : a+b, list1,list2)

print(list(result))