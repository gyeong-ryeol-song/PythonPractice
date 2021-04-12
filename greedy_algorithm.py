# 그리디 알고리즘은 현재 상황에서 지금 당장 좋은 것만 고르는 방법
# 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
# 그리디 해법은 그 정당성 분석이 중요
# -> 단순히 가장 좋아보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토

# 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 때가 많음
# 코딩테스트에서의 대부분의 그리디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서,
# 이를 추론할 수 있어야 풀리도록 출제됩니다.

# ex) 거스름돈 문제
# 가지고 있는 동전 중 가장 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을
# 종합해 다른 해가 나올 수 없기 때문

# 그리디 알고리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고
# 이게 정당한지 검토할 수 있어야 함

# ex)

n = int(input())
count =0

array = [500,100,50,10]

for coin in array:
    count+=n//coin
    n%=coin

print(count)


# <문제> 1이 될 때까지
# 어떠한 수 N이 1이 될때까지
# 1. N에서 1을 뺍니다
# 2. N을 K로 나눕니다.
# my answer

import time

n,k = map(int,input().split())
start_time = time.time() # 시간 측정 시작
count=0

while n!=1:
    if n%k == 0:
        n/=k
        count+=1
    else:
        n-=1
        count+=1

print(count)
end_time=time.time() # 측정 종료
print("time: ",end_time - start_time) # 수행시간 출력



# lecture answer

n,k=map(int,input().split())
result=0

while True:
    #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k)*k
    result +=(n-target) # 반복 여러번 할 거 없이 -1 연산 모두 더하기
    n=target

    if n<k:
        break

    result+=1
    n//=k

result+=(n-1)
print(int(result))
# 시간복잡도를 줄이기 위한 테크닉


# <문제> 곱하기 혹은 더하기
# 각자리가 숫자(0 to 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩
# 모든 숫자를 확인하여 숫자사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를
# 구하는 프로그램을 작성하세요
# 단 모든 연산은 왼쪽에서 순서대로(사칙연산 허용x)

s= input()
n=len(s)

sum=int(s[0])

for i in range(n-1):
    if(int(s[i]) == 0 or int(s[i] == 1)):
        sum+=int(s[i+1])
    else:
        sum*=int(s[i+1])

print(sum)


# <문제> 모험가 길드: 문제 설명
# 한 마을에 모험가가 N명 있음. 모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데,
# '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어짐
# 모험가 길드장은 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는
# 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규제함
# 최대 몇 개의 모험가 그룹을 만들 수 있는지 궁금함. N명의 모험가에 대한
# 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹의 최댓값을 구하는 프로그램을 작성하시오

# lecture answer

n=int(input())
adv=list(map(int,input().split()))
adv.sort()

result=0 # 그룹수
count=0 # 현재 그룹에 포함된 모험가의 수

for i in adv: # 공포도 낮은 것부터 하나씩 확인하기
    count+=1 # 현재 그룹에 해당 모험가를 포함시키기
    if count>=i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result+=1
        count=0

print(result)


