from collections import deque

def find_cost(now_dir, next_dir, cost):
    if (now_dir == 'right' or now_dir == 'left') and (next_dir == 'left' or next_dir == 'right'):  
        return cost + 100
    if (now_dir == 'down' or now_dir == 'up') and (next_dir == 'down' or next_dir == 'up'):  
        return cost + 100
    if (now_dir == 'right' or now_dir == 'left') and (next_dir == 'down' or next_dir == 'up'):  
        return cost + 600
    if (now_dir == 'down' or now_dir == 'up') and (next_dir == 'right' or next_dir == 'left'):  
        return cost + 600

    
def bfs(x, y, cost, direct, board):
    queue = deque([(x, y, cost, direct)])
    check = [[0 for _ in range(N)] for _ in range(N)]
    check[x][y] = 1

    while queue:
        x, y, cost, cur_dir = queue.popleft()
        if x == N-1 and y == N-1:
            answer.append(cost)

        for a, b, d in[(0, 1, 'right'), (1, 0, 'down'), (0, -1, 'left'), (-1, 0, 'up')]:
            new_x, new_y, new_cost = x+a, y+b, find_cost(cur_dir, d, cost)

            if 0 <= new_x < N and 0 <= new_y < N and not board[new_x][new_y]:
                if not check[new_x][new_y] or check[new_x][new_y] > new_cost:
                    check[new_x][new_y] = new_cost
                    queue.append((new_x, new_y, new_cost, d))


def solution(board):
    global N, answer

    answer = []
    N = len(board)

    bfs(0, 0, 0, 'right', board)
    bfs(0, 0, 0, 'down', board)

    return min(answer)

board=[[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))