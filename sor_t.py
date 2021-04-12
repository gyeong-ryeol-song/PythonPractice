# 정렬
"""
정렬이란 : 데이터를 특정한 기준에 따라 순서대로 나열하는 것
일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됨
"""

# 선택정렬
# ex)


array=[7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index=i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index=j
        array[i],array[min_index] = array[min_index],array[i]

print(array)





# 삽입정렬
"""
처리되지 않은 데잍를 하나씩 골라 적절한 위치에 삽입
선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작
"""

# ex)

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:
            break

print(array)


# 퀵 정렬
"""
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)로 설정
"""

# ex)
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array,start,end):
    # 원소가 한 개인 경우 종료
    if start >= end:
        return
    # 피벗은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        while(right > start and array[right] >= array[pivot]):
            right-=1
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았따면 작은 데이터와 큰 데이터를 교체
        else:
            array[left],array[right] = array[right],array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

# 파이썬의 장점을 살린 퀵 정렬

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_py(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 리스트
    # 분할된 왼쪽 부분
    left_side = [x for x in tail if x <= pivot]
    # 분할된 오른쪽 부분
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)

print(quick_sort_py(array))

# 계수 정렬
"""
특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도 수행시간 O(N+K)를 보장
"""
# ex)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

# 문제 풀이

"""
<문제> 두 배열의 원소 교체

두 개의 배열 A,B는 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수입니다.
최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와
배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말합니다.
최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것입니다.
N,K 그리고 배열 A,B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는
배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하세요

출력 조건 : 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의
최댓값을 출력합니다.
"""

# my answer


n,k = map(int, input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

count=0
while count < k:
    min_a_index=0
    max_b_index=0
    for i in range(n):
        if a[min_a_index] > a[i]:
            min_a_index=i

        if b[max_b_index] < b[i]:
            max_b_index = i

    if a[min_a_index] < b[max_b_index]:
        a[min_a_index],b[max_b_index]=b[max_b_index],a[min_a_index]
        count+=1
    else:
        break

print(sum(a))

# 주의) 이 답안은 시간초과 판정을 받을 수 있음



# lecture answer

n,k = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# a는 오름차순, b는 내림차순
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))