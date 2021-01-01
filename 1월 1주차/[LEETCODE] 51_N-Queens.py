
'''
- N-Queens는 백트래킹의 대표적인 문제!
- dfs를 이용
- 퀸을 놓을 때마다, 가능한지 확인하면서 backtracking
- 가능여부 확인할 때, 세로, 대각선(\, /) 확인
- [x, y] -> 세로 : [y], 대각선(\) : [n+x-y-1], 대각선(/) : [x+y]
'''
n = 4  # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

from copy import deepcopy
def solveNQueens(self, n):

    def nqueen(i):
        if i == n:
            # board는 완성이 된다 -> 하지만 계속 참조되기도 함
            # 따라서 deepcopy를 해줘서 board를 멈춰야한다.
            temp = deepcopy(board)
            answer.append(temp)
            return
        
        for j in range(n):  # j는 y
            if not a[j] and not b[n+i-j-1] and not c[i+j]:
                a[j] = b[n+i-j-1] = c[i+j] = True
                board[i][j] = 'Q'
                nqueen(i+1)
                board[i][j] = '.'
                a[j] = b[n+i-j-1] = c[i+j] = False

    a = [False] * n  # 세로
    b = [False] * (2 * n - 1)  # 대각선(\)
    c = [False] * (2 * n - 1)  # 대각선(/)

    board  = [['.'] * n for _ in range(n)]

    answer = []
    nqueen(0)
    results = []
    for ans in answer:
        result = []
        for i in range(len(ans)):
            print(''.join(ans[i]))
            result.append(''.join(ans[i]))
        results.append(result)
    return results