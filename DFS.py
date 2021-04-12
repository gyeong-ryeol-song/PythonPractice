# DFS(Depth-First Search)
"""
DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘입니다.
DFS는 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고
방문 처리합니다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.
"""

# DFS 소스코드 예제

# DFS 메서드 정의


def dfs(graph,v,visited):
    # 현재 노드를 방문 처리
    visited[v]= True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False]*9
dfs(graph,1,visited)


# BFS(Breadth-First Search)
"""
BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가장 가까운 노드부터 우선적으로 탐색하는 알고리즘입니다.
BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리 합니다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고
방문 처리합니다.
3. 더 이상 2번의 과정을 수행할 수 없을 때 까지 반복합니다.
"""

# BFS 소스코드 예제
from collections import deque


# BFS 메서드 정의
def bfs(graph,start,visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    visited[start] = True
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v,end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽임
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

bfs(graph,1,visited)

"""
<문제> 음료수 얼려먹기
NxM 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는
부분은 1로 표시됩니다. 구멍이 뚫려있는 부분끼리 상,하,좌,우로 붙어 있는 경우
서로 연결되어 있는 것으로 간주합니다.
이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.

입력조건
첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다(1<=N,M<=1000)
두 번째 줄부터 N+1 번째 줄까지 얼음 틀의 형태가 주어집니다.
이 때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.

출력조건
한 번에 만들 수 있는 아이스크림의 개수를 출력합니다
"""
# answer

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y]==0:
        # 해당 노드 방문 처리
        graph[x][y]=1
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n,m = map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

result =0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j)==True:
            result+=1

print(result)


"""
<문제> NxM 크기의 직사각형 형태의 미로에 갇혔습니다. 미로에는 여러 마리의 괴물이 있어
이를 피해 탈출해야 합니다
현 위치는 (1,1) 이며 출구는 (N,M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
이 때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다. 미로는 반드시
탈출할 수 있는 형태로 제시됩니다.
이 때 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요. 칸을 셀 때는 
시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

입력조건
첫째 줄에 두 정수 N,M(4<=N,M<=200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(0 or 1)로
미로의 정보가 주어집니다. 각각의 수들은 공백 없이 붙어서 입력으로 제시됩니다. 또한
시작칸과 마지막 칸은 항상 1입니다.

출력조건
첫째 줄에 최소 이동 칸의 개수를 출력합니다.
"""

# lecture answer


from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(5):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때 까지 반복하기
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny= y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0,0))

