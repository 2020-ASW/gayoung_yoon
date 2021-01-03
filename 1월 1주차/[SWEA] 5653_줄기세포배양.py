'''
2 2 10
1 1
0 2
5 5 19
3 2 0 3 0
0 3 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 2
9 10 37
0 0 0 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 5 3
0 0 2 0 0 0 0 4 0 0
3 0 0 0 0 0 4 0 0 0
0 0 0 0 0 3 5 0 0 2
0 0 0 0 0 0 0 0 0 5
0 0 0 0 0 0 0 0 2 3
0 0 0 0 0 0 0 0 0 0
0 0 2 2 0 0 0 0 0 0
'''

from collections import deque
from pprint import pprint

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    first_status = [list(map(int, input().split())) for _ in range(N)]
    board = [[0 for _ in range(M + K + 100)] for _ in range(N + K + 100)]  # 시간이 줄어드는 것 표현
    visit = [[0] * (M + K + 100) for _ in range(N + K + 100)]  # 지나간 자리
    q = deque()  # 죽지 않은 애들

    for i in range(N):
        for j in range(M):
            if first_status[i][j] > 0:  # 초기상태 값들
                temp = first_status[i][j]
                board[i + K // 2][j + K // 2] = temp
                q.append((i + K // 2, j + K // 2, temp))
                visit[i + K // 2][j + K // 2] = True

    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    def spread():
        for _ in range(len(q)):
            x, y, time = q.popleft()

            if board[x][y] > 0:  # 비활성 상태
                board[x][y] -= 1
                if board[x][y] == 0:
                    board[x][y] = -1
                q.append((x, y, time))

            elif time > 0:  # 활성 상태가 된 애들
                for a, b in near:
                    xi, yi = x + a, y + b
                    if board[xi][yi] == 0:
                        if visit[xi][yi] == 0:  # 아직 번지지 않은 부분
                            new.append([xi, yi])
                            visit[xi][yi] = time  # visit : 최대값 넣기 위함
                        else:
                            if visit[xi][yi] < time:
                                visit[xi][yi] = time
                
                if time != 1:
                    q.append((x, y, time - 1))

        for n in range(len(new)):
            x, y = new.popleft()
            board[x][y] = visit[x][y]
            q.append((x, y, board[x][y]))        


    for k in range(K):
        new = deque()
        spread()
    print(f'#{t} {len(q)}')

