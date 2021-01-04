'''
[풀이과정]
1. 사다리를 이용하지 않고 이동할 수 있는 곳을 표시한다.
2. 각 지형을 연결하는 사다리의 최솟값을 도출한다.
3. 모든 지형들이 연결되어있는지 확인
'''

# def solution(land, height):
#     answer = 0
#     return answer

# land = [[1, 4, 8, 10], [6, 6, 6, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
# height = 3  # result = 15

land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
height = 1  # result = 18

from collections import deque
import heapq

def bfs(land, height, visit, group, i, j):
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()  
        visit[x][y] = group
        for a, b in near:
            xi, yi = x + a, y + b
            if  0 <= xi < n and 0 <= yi < n and visit[xi][yi] == 0:
                if abs(land[xi][yi] - land[x][y]) <= height:
                    q.append([xi, yi])
                    visit[xi][yi] = group

n = len(land)
visit = [[0] * n for _ in range(n)]

near = [(0, -1), (0, 1), (1, 0), (-1, 0)]

# 1. 사다리를 이용하지 않고 이동할 수 있는 곳을 표시한다.
group = 1
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            bfs(land, height, visit, group, i, j)
            group += 1

'''
[[1, 1, 1, 1],
 [1, 1, 1, 1], 
 [2, 2, 2, 2], 
 [2, 2, 2, 3]]
'''

# 2. 각 지형을 연결할 수 있는 사다리의 최솟값 도출
check = {}  # {(1, 2): 5, (2, 3): 10} // {(1, 2): 8, (1, 3): 10, (2, 3): 19}
for i in range(n):
    for j in range(n):
        for a, b in near:
            xi, yi = i + a, j + b
            if 0 <= xi < n and 0 <= yi < n and visit[i][j] != visit[xi][yi]:
                if (visit[i][j], visit[xi][yi]) not in check and (visit[xi][yi], visit[i][j]) not in check:
                    check[(visit[i][j], visit[xi][yi])] = abs(land[i][j] - land[xi][yi])

                elif (visit[i][j], visit[xi][yi]) in check:
                    if check[(visit[i][j], visit[xi][yi])] > abs(land[i][j] - land[xi][yi]):
                        check[(visit[i][j], visit[xi][yi])] = abs(land[i][j] - land[xi][yi])

print(check)

# 3. 모든 지형들이 연결되어있는지 확인 + total 최솟값
# {(1, 2): 5, (2, 3): 10} // {(1, 2): 8, (1, 3): 10, (2, 3): 19}
def find_root(x, root):
    if x == root[x]: return x
    else:
        r = find_root(root[x], root)
        root[x] = r
        return r

def union_find(x, y, root):
    x_root = find_root(x, root)
    y_root = find_root(y, root)
    root[y_root] = x_root


def kruskal(ladders, group):
    sum = 0
    roots = {_:_ for _ in range(1, group)} # 정점들 root 표시
    for (x, y), value in ladders:
       if find_root(x, roots) != find_root(y, roots): # root가 같지 않을 경우
           union_find(x, y, roots) # root 연결
           sum += value # 값 갱신
       if len(roots.items()) == 1: return sum # 노드들이 전부 연결된 경우 리턴
    return sum

print(kruskal(check, group))


def find_ladder(check, land, N):
    direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    ladders = defaultdict(lambda: math.inf)
    
    for i in range(N):
        for j in range(N):
            current = check[i][j]
            for dx, dy in direction:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= N or check[nx][ny] == current: continue
                dist = abs(land[i][j] - land[nx][ny])
                ladders[(current, check[nx][ny])] = min(dist, ladders[(current, check[nx][ny])])
    return ladders
ladders = find_ladder(check, land, N)