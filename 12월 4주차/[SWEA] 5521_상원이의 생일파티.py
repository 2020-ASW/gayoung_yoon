'''
2
6 5
2 3
3 4
4 5
5 6
2 5
6 5
1 2
1 3
3 4
2 3
4 5
'''
from collections import deque

def bfs():
    q = deque([1])
    cnt = 0
    depth = 0
    while q:
        s = len(q)
        for i in range(s):
            x = q.popleft()
            for j in check[x]:
                if not visit[j]:
                    q.append(j)
                    visit[j] = 1
                    cnt += 1
        depth += 1

        if depth == 2:
            break
    return cnt

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    check = {i:[] for i in range(N+1)}
    for i in range(M):
        a, b = map(int, input().split())
        check[a].append(b)
        check[b].append(a)
    # print(check)  # {1: [2, 3], 2: [1, 3], 3: [1, 4, 2], 4: [3, 5], 5: [4]}
    
    visit = [0] * (N+1)
    visit[1] = 1  # 상원이는 초대장 받지 않음

    print(f'#{t} {bfs()}')