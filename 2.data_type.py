# 자료형
# 정수형(integer) : 정수를 다루는 자료형
# 실수형(Real number) :소수점 아래의 데이터를 포함하는 수 자료형
#                    : 파이썬에서는 변수에 소수점을 붙인 수를 대입하면 실수형 변수로 처리됨
#                    : 소수부가0이거나 정수부가 0인 소수는 0을 생략하고 작성 가능
#ex)

a = 5.
print(a)

# 지수 표현방식 : 기본적으로 실수형 데이터
# 1e9 = 1000000000
# 최댓값이 10억 미만이면 무한대 값으로 1e9 사용 가능
#ex)

b = 1e9
print(b)

# 실수형 더 알아보기 : 실수형을 저장하기 위해 4바이트,8바이트의 고정된 크기의 메모리를 할당하므로,
#                     컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 가짐
#ex)


c = 0.3 + 0.6
print(c)

if c == 0.9:
    print(True)
else:
    print(False)
# 해결법 -> round()  함수 이용, round(값, 소수 몇째 자리까지 반올림)
print(round(c,1))

if round(c,1) == 0.9:
    print(True)
else:
    print(False)

# 수 자료형 연산
# 나누기연산(/) 결과는 실수형으로 반환
# 나머지연산자 = %
# 몫 연산자 = //
# 거듭 제곱 연산자 = **

# 리스트 자료형 : 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
# c나 자바에서의 배열(array)의 기능 및 연결 리스트와 유사한 기능을 지원
# 리스트 대신 배열 혹은 테이블이라고 부르기도 함

# 리스트 초기화
# 리스트는 대괄호([])안에 원소를 넣어 초기화, 쉼표(,)로 원소를 구분
# 비어있는 리스트를 선언하고자 할 때 list() 혹은 [] 를 이용할 수 있음
# 리스트의 인덱스는 0부터 시작

d = [1,2,3,4,5,6,7,8,9]
print(d)
print(d[3])

n=10
a=[0]*n # 크기가 n이고 모든 값이 0인 1차원 리스트 초기화
print(a)

# 인덱싱
# 음의 정수를 넣으면 원소를 거꾸로 탐색

print(d[-1])
print(d[-3])

# 슬라이싱 : 연속적인 위치를 갖는 원소들을 가져와야 할 때
# :을 이용해서 설정
# 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정

print(d[1:4])

# 리스트 컴프리헨션
# 리스트를 초기화 하는 방법 중 하나, 대괄호 안에 조건문과 반복문을 적용하여 리스트 초기화

array = [i for i in range(10)] # 반복문을 먼저 설정하는 것을 추천

print(array)

array = [i for i in range(20) if i%2 == 1]
print(array)


# 리스트 컴프리헨션은 2차원 리스트를 초기화할 때 효과적으로 사용됨
# NxM 크기의 2차원 리스트를 한번에 초기화 할 때 매우 유용

n=4
m=3
array = [[0]*m for _ in range(n)]
print(array)

# 파이썬에서 반복을 수행하되 반복을 위한 변수값을 무시하고 싶을 때 언더바(_)를 사용함
# ex)

for _ in range(5):
    print("Hello World")

# 리스트 관련 기타 메서드
# append() : 리스트에 원소를 하나 삽입할 떄 (복잡도 O(1))
# sort() : 기본 정렬 기능으로 오름차순으로 정렬, reverse=True 설정하면 내림차순 (복잡도 O(NlogN))
# reverse() : 리스트의 원소의 순위를 모두 뒤집음 (복잡도 O(N))
# insert(삽입할 위치 인덱스, 삽입할 값) : 특정 인덱스 위치에 원소 삽입(복잡도 O(N))
# count(특정값) : 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 (복잡도 O(N))
# remove(특정값) : 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거 (복잡도 O(N))
# ex)

list = [1,2,3,4,5,5,5]
remove_set = {3,5} # 집합 자료형

result = [i for i in list if i not in remove_set]
print(result)

