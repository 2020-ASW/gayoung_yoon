n, m = map(int, input().split())

board = [list(map(int, input())) for _ in range(n)]

# n-1, m-1에서 시작하나, 0, 0에서 시작하나 상관없다.
for i in range(n-2, -1, -1):
    for j in range(m-2, -1, -1):
        if board[i][j] != 0:
            board[i][j] += min(board[i][j+1], board[i+1][j], board[i+1][j+1])

answer = 0
for i in board:
    answer = max(answer, max(i))

print(answer ** 2)



'''
4 4
0100
0111
1110
0010
[[0, 1, 0, 0],
 [0, 1, 1, 1], 
 [1, 1, 2, 0], 
 [0, 0, 1, 0]]
'''