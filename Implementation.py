"""
구현 유형의 예시
1. 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
2. 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
3. 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
4. 적절한 라이브러리를 찾아서 사용해야 하는 문제
"""

# 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬(Matrix)의 의미로 사용됨

for i in range(5):
    for j in range(5):
        print('(',i,',',j,')',end=' ')
    print()

# ex)
# 동, 북, 서, 남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 현재 위치
x, y = 2, 2

for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    print(nx,ny)

"""
<문제> 상하좌우
여행가 A는 NxN 크기의 정사각형 공간위에 서 있습니다.
이 공간은 1x1 크기의 정사각형으로 나누어져 있습니다.
가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는 (N,N)에 해당합니다.
A는 상하좌우로 움직일 수 있으며, 시작좌표는 (1,1)입니다. 
다음은 A가 이동할 계획서입니다.
계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D 중 하나의 문자가 반복적으로
적혀있습니다.
L:왼쪽으로 한 칸 이동
R:오른쪽으로 한 칸 이동
U:위로 한 칸 이동
D:아래로 한 칸 이동
이 때 A가 NxN 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다. 
ex) (1,1) 위치에서 L 혹은 U를 만나면 무시됩니다.

문제 조건
첫째 줄에 공간의 크기를 나타내는 N(1<=N<=100)이 주어짐
A가 이동할 계획서 내용이 주어짐(1<=이동횟수<=100)

출력조건
첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X,Y)를 공백을 기준으로 구분하여 출력
"""

# answer

n=int(input())
plan=input().split()

x,y = 1,1

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for p in plan:
    for i in range(len(move_types)):
        if p==move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]

        if nx<1 or ny<1 or nx>n or ny>n:
            continue

        x,y=nx,ny

print(x,y)






"""
<문제> 시각
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각중에서
3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요
ex)1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다
00시 00분 03초
00시 13분 30초

입력조건
첫째 줄에 정수 N이 입력됩니다.(0<=N<=23)

출력조건
00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
모든 경우의 수를 출력합니다.
"""
# 이러한 유형은 완전탐색(Brute Forcing) 문제 유형이라고 불립니다.
# 완전탐색은 가능한 경우의 수를 모두 검사해보는 탐색 방법을 의미합니다.

# my answer


n=int(input())
count_3=0

for hour in range(n+1):
    for minute in range(60):
        for second in range(60):
            time = str(hour)+str(minute)+str(second)
            for i in range(len(time)):
                if time[i]=='3':
                    count_3+=1
                    break

print(count_3)



# lecture answer

h=int(input())
count=0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k): # for문 없이도 가능
                count+=1

print(count)


"""
<문제> 왕실의 나이트
왕국의 왕실 정원은 체스판과 같은 8x8 좌표 평면입니다. 왕실 정원의 특정한 한 칸에
나이트가 서 있습니다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마합니다.
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 
정원 밖으로는 나갈 수 없습니다.
나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있습니다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

입력조건
첫째 줄에 8x8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는
두 문자로 구성된 문자열이 입력된다. 입력문자는 a1처럼 열과 행으로 이루어진다

출력조건 
첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오

"""

# my answer

spot = input()

row=[1,2,3,4,5,6,7,8]
col=['a','b','c','d','e','f','g','h']
col_1=[1,2,3,4,5,6,7,8]

x=int(spot[1])

for i in range(len(col)):
    if spot[0]==col[i]:
        y=col_1[i]

dx=[2,2,-2,-2,1,1,-1,-1]
dy=[1,-1,1,-1,2,-2,2,-2]
count=0

for i in range(len(dx)):
    nx=x+dx[i]
    ny=x+dy[i]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    count+=1

print(count)


# lecture answer


input_data=input()
row = int(input_data[1])
col = int(ord(input_data[0]))-int(ord('a'))+1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    next_row = row+step[0]
    next_col = col+step[1]

    if next_row>=1 and next_row<=8 and next_col>=1 and next_col<=8:
        result+=1

print(result)


"""
<문제> 문자열 재정렬
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
이 때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든
숫자를 더한 값을 이어서 출력합니다.
ex) K1KA5CB7 이라는 값이 들어오면 ABCKK13을 출력함

입력조건
첫째 줄에 하나의 문자열 S가 주어집니다(1<=S의 길이<=10000)

출력조건
첫째 줄에 문제에서 요구하는 정답을 출력합니다.
"""


word=input()
int_part=0
result=[]
for x in word:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        int_part+=int(x)
# 알파벳 오름차순 정렬
result.sort()

if int_part!=0:
    result.append(str(int_part))

# 최종결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))




