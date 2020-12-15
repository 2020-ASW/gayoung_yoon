# DFS랑 DP 사용

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

near = [(0, 1), (0, -1), (1, 0), (-1, 0)]

visit = [[0] * N for _ in range(M)]
visit[0][0] = 1

x, y = 0, 0
def dfs(x, y):
    if x == M - 1 and y == N - 1:
        print(1)

    if visit[x][y] == 0:
        visit[x][y] = 1
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < M and 0 <= yi < N and board[x][y] > board[xi][yi]:
                visit[x][y] += dfs(xi, yi)
                
    return visit

print(visit)
