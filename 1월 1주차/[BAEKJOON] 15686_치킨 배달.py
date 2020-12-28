'''
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
'''

from itertools import combinations

def find_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            houses.append([i, j])
        elif board[i][j] == 2:
            chickens.append([i, j])

results = list(combinations(chickens, M))

mymin = 999999999999999999999999999999
for result in results:
    answer = 0
    for x, y in houses:
        temp = 9999999999999
        for a, b in result:
            distance = find_distance(x, y, a, b)
            if temp > distance:
                temp = distance
        
        answer += temp
    
    if mymin > answer:
        mymin = answer
print(mymin)

