# 실전에서 유용한 표준 라이브러리
# 내장함수 : 기본 입출력 함수부터 정렬 함수까지 기본적이 함수들 제공
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들 제공
# heapq : 힙 자료구조를 제공, 일반적으로 우선순위 큐 기능을 구현하기 위해 사용됨
# bisect : 이진탐색 기능을 제공
# collections : 덱, 카운터 등의 유용한 자료구조를 포함
# math : 필수적인 수학적 기능을 제공, 팩토리얼, 제곱근, 최대공약수, 삼각함수 부터 파이같은 상수도 포함

# sum()
result = sum([1,2,3,4,5])
print(result)

# min(), max()
min_result = min(7,3,5,2)
max_result = max(7,3,5,2)
print(min_result,max_result)

# eval() 계산 결과를 실제 수로 반환
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9,1,8,5,4])
reverse_result = sorted([9,1,8,5,4],reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array=[('홍길동',35),('이순신',75),('아무개',50)]
result = sorted(array, key=lambda x: x[1],reverse=True)
print(result)

# 순열 nPr
from itertools import permutations
data = ['A','B','C']
result = list(permutations(data,3))
print(result)

# 조합 nCr
from itertools import combinations
data = ['A','B','C']
result = list(combinations(data,2))
print(result)

# 중복 순열과 중복 조합
from itertools import product
data = ['A','B','C']

result = list(product(data,repeat=2)) # 2개를 뽑는 모든 순열 구하기
print(result)

from itertools import combinations_with_replacement

data = ['A','B','C']

result = list(combinations_with_replacement(data,2))
print(result)

# Counter
# 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공
# 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려줌

from collections import Counter

counter= Counter(['red','blue','red','green','blue','blue'])

print(counter['blue']) # 블루가 등장한 횟수 출력
print(counter['green']) # 그린이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형을 반환
print(counter)

# 최대 공약수 최소 공배수
import math

def lcm(a,b):
    return a*b/math.gcd(a,b)

a=21
b=14

print(math.gcd(21,14))
print(lcm(21,14))
