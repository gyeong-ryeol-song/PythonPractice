
"""
탐색이란 : 많은양의 데이터 중에서 원하는 데이터를 찾는 과정
대표적인 그래프 탐색 알고리즘으로는 DFS, BFS가 있음
"""

# 스택 자료구조
"""
먼저 들어 온 데이터가 자웅에 나가는 형식(선입후출)의 자료구조
입구와 출구가 동일한 형태로 스택을 시각화 할 수 있음
파이썬은 스택구조를 사용하기 위해 단순히 리스트 자료형을 사용하면 됨
"""

stack=[]
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 최상단 원소부터 출력
print(stack[::-1])
# 최하단 원소부터 출력
print(stack)

# 큐 자료구조
"""
먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조입니다.
큐는 입구와 출구가 모두 뚫려있는 터널과 같은 형태로 시각화할 수 있습니다.
파이썬에서 큐를 사용하려면 collections의 deque를 import
리스트로도 사용가능하지만 처리시간때문에 불리
"""
from collections import deque
# 큐(Queue) 구현을 위해 deque라이브러리 사용
queue=deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# 먼저 들어온 순서대로 출력
print(queue)
# 역순으로 바꾸기
queue.reverse()
print(queue)


# 재귀함수
"""
재귀 함수란 자기 자신을 다시 호출하는 함수를 의미합니다.

유의사항
재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있음
단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중하게 사용해야함
모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있음
재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있음
컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓임
그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신 재귀 함수를 이용하는 경우가 많음
"""


def recursive_function(i):
    if i==100:
        return
    print(i,"번째 재귀함수에서",i+1,"번째 재귀함수를 호출합니다.")
    recursive_function(i+1)
    print(i,"번째 재귀함수를 종료합니다.")


recursive_function(1)


# 팩토리얼 문제
def factorial_iterative(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result

def factorial_recursive(n):
    if n<=1:
        return 1

    return n*factorial_recursive(n-1)

print("반복문으로 구현",factorial_iterative(5))
print("재귀함수로 구현",factorial_recursive(5))

#최대 공약수 계산(유클리드 호제법)예제
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)

print(gcd(192,162))

