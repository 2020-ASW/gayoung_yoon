from collections import deque

def numIslands(self, grid):

    n, m = len(grid), len(grid[0])

    visit = [[0] * m for _ in range(n)]

    cnt = 0
    near = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1" and not visit[i][j]:
                visit[i][j] = 1
                cnt += 1
                q = deque([[i, j]])
                while q:
                    x, y = q.popleft()
                    
                    for a, b in near:
                        xi, yi = x + a, y + b
                        if 0 <= xi < n and 0 <= yi < m and grid[xi][yi] == "1" and not visit[xi][yi]:
                            visit[xi][yi] = 1
                            q.append([xi, yi])
                
    return cnt