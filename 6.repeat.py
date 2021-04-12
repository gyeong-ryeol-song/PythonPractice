# 반복문
# 특정한 소스코드를 반복적으로 실행하고자 할 때 사용
# while, for 둘다 사용해도 되는데, 코딩테스트 실제 사용 예시를
# 확인해보면 for문이 더 간결한 경우가 많음

#ex)

i =1
result = 0

while i<=9:
    result+=i
    i+=1

print(result)

i = 1
result =0

while i<=9:
    if i%2 == 1:
        result+=i
    i+=1
print(result)


# 무한루프
# 무한루프란 끊임없이 반복되는 구문을 의미
# 코딩 테스트에서는 무한 루프를 구현할 일이 거의 없으니 유의해야 함
# 반복문을 작성한 뒤에는 항상 반복문을 탈출할 수 있는지 확인

x=10
while x>5:
    print(x)


# 반복문 : for 문
# for 문 구조는 특정한 변수를 이용하여 'in' 뒤에 오는 데이터(리스트, 튜플 등)에
# 포함되어 있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문
# ex)
# for 변수 in 리스트:
#   실행할 소스코드
# ex)

array=[9,8,7,6,5]
for x in array:
    print(x)

array=(9,8,7,6,5)
for x in array:
    print(x)


# for문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용
# 이 때 range(시작, 끝 +1) 형태로 사용해야함
# 인자를 하나만 넣으면 자동으로 시작 값은 0이 됨
# ex)

result =0
for i in range(1,10):
    result+=i
print(result)

# continue
# 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때
# ex)

result = 0
for i in range(1,10):
    if i%2 ==0:
        continue
    result +=i
print(result)

# break
# 반복문을 즉시 탈출하고자 할 때
# ex)

i = 1
while True:
    print("현재 i 값은 : ",i)
    if i==5:
        break
    i+=1

# ex)

scores = [90,85,77,65,97]

for i in range(5):
    if scores[i] >= 80:
        print(i+1,"번 학생은 합격입니다.")

scores = [90,85,77,65,97]
cheating_student_list = {2,4}

for i in range(5):
    if i+1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i+1,"번 학생은 합격입니다.")

# 중첩 반복문
# ex)

for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
    print() # 개행

