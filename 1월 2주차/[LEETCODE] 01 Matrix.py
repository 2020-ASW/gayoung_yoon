# def updateMatrix(self, matrix):

# matrix = [[0,0,0], [0,1,0], [0,0,0]]
matrix = [[0,0,0], [0,1,0], [1,1,1]]

n, m = len(matrix),len(matrix[0])
dp = [[float('Inf')] * m for _ in range(n)]

# 왼쪽 위부터 돌면서 minimum값 찾기
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            dp[i][j] = 0
        else:
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1]+1)

# 오른쪽 아래부터 돌면서 minimum값 찾기
# 처음에 이것만 했더니 [[0, 0, 0], [0, 1, 0], [inf, inf, inf]]이런 결과 나옴
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if matrix[i][j] == 0:
            dp[i][j] = 0
        else:
            if i < n-1:
                dp[i][j] = min(dp[i][j], dp[i+1][j]+1)
            if j < m-1:
                dp[i][j] = min(dp[i][j], dp[i][j+1]+1)

print(dp)