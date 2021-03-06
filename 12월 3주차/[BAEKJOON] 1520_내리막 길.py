M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

near = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visit = [[-1] * N for _ in range(M)]

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if visit[x][y] == -1:
        # print('x, y')
        # print(x, y)
        # print(visit)
        visit[x][y] = 0
        for a, b in near:
            xi, yi = x + a, y + b
            if 0 <= xi < M and 0 <= yi < N and board[x][y] > board[xi][yi]:
                visit[x][y] += dfs(xi, yi)
    print(visit)
    return visit[x][y]

print(dfs(0, 0))

'''
x, y
0 0
[[-1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1]]
x, y
1 0
[[0, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1], 
 [-1, -1, -1, -1, -1], 
 [-1, -1, -1, -1, -1]]
x, y
2 0
[[0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [-1, -1, -1, -1, -1],
 [-1, -1, -1, -1, -1]]
x, y
3 0
[[0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [-1, -1, -1, -1, -1]]
x, y
3 1
[[0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1]]
x, y
3 2
[[0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1],
 [0, -1, -1, -1, -1], 
 [0, 0, -1, -1, -1]]
x, y
3 3
[[0, -1, -1, -1, -1],
 [0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1],
 [0, 0, 0, -1, -1]]

[[0, -1, -1, -1, -1],
 [0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [0, 0, 0, 1, -1]]

[[0, -1, -1, -1, -1],
 [0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [0, 0, 1, 1, -1]]

[[0, -1, -1, -1, -1],
 [0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [0, 1, 1, 1, -1]]

[[0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [1, 1, 1, 1, -1]]

[[0, -1, -1, -1, -1], 
 [0, -1, -1, -1, -1], 
 [1, -1, -1, -1, -1], 
 [1, 1, 1, 1, -1]]

[[0, -1, -1, -1, -1], 
[1, -1, -1, -1, -1], 
[1, -1, -1, -1, -1], 
[1, 1, 1, 1, -1]]

x, y
0 1
[[1, -1, -1, -1, -1], [1, -1, -1, -1, -1], [1, -1, -1, -1, -1], [1, 1, 1, 1, -1]]
x, y
0 2
[[1, 0, -1, -1, -1], [1, -1, -1, -1, -1], [1, -1, -1, -1, -1], [1, 1, 1, 1, -1]]
x, y
0 3
[[1, 0, 0, -1, -1], [1, -1, -1, -1, -1], [1, -1, -1, -1, -1], [1, 1, 1, 1, -1]]
x, y
1 3
[[1, 0, 0, 0, -1], [1, -1, -1, -1, -1], [1, -1, -1, -1, -1], [1, 1, 1, 1, -1]]
x, y
2 3
[[1, 0, 0, 0, -1], [1, -1, -1, 0, -1], [1, -1, -1, -1, -1], [1, 1, 1, 1, -1]]
[[1, 0, 0, 0, -1], [1, -1, -1, 0, -1], [1, -1, -1, 0, -1], [1, 1, 1, 1, -1]]
[[1, 0, 0, 0, -1], [1, -1, -1, 0, -1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]
[[1, 0, 0, 0, -1], [1, -1, -1, 1, -1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]

x, y
0 4
[[1, 0, 0, 1, -1], [1, -1, -1, 1, -1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]
x, y
1 4
[[1, 0, 0, 1, 0], [1, -1, -1, 1, -1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]
[[1, 0, 0, 1, 0], [1, -1, -1, 1, 0], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]
[[1, 0, 0, 1, 0], [1, -1, -1, 1, 1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]
[[1, 0, 0, 1, 1], [1, -1, -1, 1, 1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]
[[1, 0, 0, 2, 1], [1, -1, -1, 1, 1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]
[[1, 0, 2, 2, 1], [1, -1, -1, 1, 1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]
[[1, 2, 2, 2, 1], [1, -1, -1, 1, 1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]
[[3, 2, 2, 2, 1], [1, -1, -1, 1, 1], [1, -1, -1, 1, -1], [1, 1, 1, 1, -1]]
3
'''