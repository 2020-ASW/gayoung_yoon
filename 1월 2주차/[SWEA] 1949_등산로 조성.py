'''
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2       
1 2 1     
2 1 2
1 2 1

6
3
'''


def dfs(x, y, flag, length): #(r,c)를 시작으로 등산로 최대 길이를 구하는 함수
    # flag가 1이미 이미 한 번 깎은 것.
    global max_length
    visit[x][y] = 1
 
    if max_length < length:
        max_length = length
 
    for a, b in [(-1, 0),(0,1),(1,0),(0,-1)]:
        xi = x + a
        yi = y + b
        if 0 <= xi < n and 0 <= yi < n and visit[xi][yi] == 0:
            if board[xi][yi] < board[x][y]:
                visit[xi][yi] = 1
                dfs(xi, yi, flag, length+1)
                visit[xi][yi] = 0
 
            elif flag == 0 and board[xi][yi] - K < board[x][y]:
                val = board[xi][yi]
                board[xi][yi] = board[x][y] - 1
                visit[xi][yi] = 1
                dfs(xi, yi, 1, length+1)
                visit[xi][yi] = 0
                board[xi][yi] = val
 

    return max_length
 

 
for t in range(1, int(input())+1):
    n, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
 
    mymax = 0
    for i in range(n):
        for j in range(n):
            if mymax < board[i][j]:
                mymax = board[i][j]

    max_ans = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == mymax:
                visit = [[0] * n for _ in range(n)]
                visit[i][j] = 1
                max_length = 0
                temp = dfs(i, j, 0, 1)
                visit[i][j] = 0
                if max_ans < temp:
                    max_ans = temp

    print(f"#{t} {max_ans}")