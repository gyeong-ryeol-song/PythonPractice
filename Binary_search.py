# 이진 탐색 알고리즘
"""
순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    -> 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정
"""

# 이진 탐색의 시간 복잡도
"""
단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log_2(N)에 비례합니다
이진 탐색은 탐색 범위를 절반씩 줄이며, 시간복잡도는 O(logN)을 보장합니다.
"""

# 이진 탐색 소스코드 : 재귀적 표현
"""
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int,input().split()))
# 전체 원소 입력 받기
array = list(map(int,input().split()))

# 이진 탐색 수행 결과 출력ㄴ
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
"""




# 이진 탐색 소스코드: 반복문 구현
"""
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int,input().split()))
# 전체 원소 입력 받기
array = list(map(int,input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
"""

# 파이썬 이진 탐색 라이브러리
"""
bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
"""

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# ex) 값이 특정 범위에 속하는 데이터 개수 구하기

# 값이 [lef_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a,4,4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a,-1,3))

# 파라메트릭 서치(Parametric Search)
"""
파라메트릭 서치란: 최적화 문제를 결정 문제(yes or no)로 바꾸어 해결하는 기법
    ex) 특정한 조건을 만족하는 가장 알맞는 값을 빠르게 찾는 최적화 문제
일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있습니다.
"""

"""
<문제> 떡볶이 떡 만들기
떡볶이 떡의 길이는 일정하지 않습니다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줍니다.
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단합니다. 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고,
낮은 떡은 잘리지 않습니다.
예를 들어, 높이가 19, 14, 10, 17인 떡이 있고 절단기의 높이가 15라면 자른 뒤 떡의 높이는
15, 14, 10, 15가 될 것입니다. 잘린 떡의 길이는 차례대로 4, 0, 0, 2입니다. 손님은 6만큼의 길이를 가져갑니다.
손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을
구하는 프로그램을 작성하세요.

(입력 조건)
첫째 줄에 떡의 개수 N(1<=N<=1000000)과 요청한 떡의 길이 M(1<=M<=2000000000)
둘째 줄에는 떡의 개별 높이가 주어집니다. 떡 높이의 총합은 항상 M 이상이므로, 
손님은 필요한 양만큼 떡을 사갈 수 있습니다. 높이는 10억이하의 양의 정수 또는 0입니다.

(출력 조건)
적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력합니다.
"""

# my answer

"""
n,m = map(int,input().split())

d = list(map(int,input().split()))


for i in range(0, max(d)):
    rest = 0
    for j in d:
        if j - i >= 0:
            rest += (j-i)

    if rest < m:
        h = before_h
        break;
    else:
        before_h = i

print(h)
"""


# 문제 해결 아이디어
"""
적절한 높이를 찾을 때 까지 이진 탐색을 수행하여 높이 H를 반복 조정하면 됩니다.
"현재 이 높이로 자르면 만족할 수 있는가?" 를 확인한 뒤 조건의 만족여부에 따라 탐색 범위를 좁혀서
해결할 수 있습니다.
절단기의 높이는 0부터 10억까지 정수 중 하나이므로 이렇게 큰 탐색 범위를 보면 가장 먼저 
이진 탐색을 떠올려야 합니다.
"""

# lecture answer
"""
n,m = map(int,input().split())

array = list(map(int,input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if mid < i:
            total += i-mid

    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)

"""


"""
<문제> 정렬된 배열에서 특정 수의 개수 구하기
N 개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이 때 이 수열에서
x가 등장하는 횟수를 계산하세요.
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간초과 판정을 받습니다.

(입력조건)
첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다(1<=N<=1000000), (-10^9<=x<=10^9)
둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다(-10^9<=각 원소의 값<=10^9)

(출력조건)
수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다. 단, 값이 x인 원소가 하나도 없다면 -1을 출력합니다.
"""
# my answer
"""
from bisect import bisect_left, bisect_right

n,x = map(int,input().split())
array = list(map(int,input().split()))


a = bisect_left(array,x)
b = bisect_right(array,x)
if b-a>0:
    result = b - a
else:
    result = -1

print(result)
"""

n,x = map(int,input().split())
array = list(map(int,input().split()))

def binary(array,x,start,end,count):
    while (start <= end):
        if start >end:
            return None


