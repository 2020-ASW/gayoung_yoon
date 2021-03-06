'''
10
10
RBKBGRBGGG
BGKRBRKBGB
20
BGBBRRKKRRGGRRBGGRBK
BGBGBKGBBKKRKGBBKGRR
30 
BGBBRRKKRRGGRRBGGRBKBGBGBKGBBK
KRKGBBKGRRGGKKBBBBKBGRBGRRRBGR
40
RGGRRBGGRBKBGBGBKGBBKKRKGBBKGRRGGKKBBBBK
BGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGB
50 
BGGRBKBGBGBKGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRGRB
RGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBG
80
BBKGRRGGKKBBBBKBGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBG
RRGBBBBKBKKRRGRBBRKBGRRRRRKKBGRRBBGRBBRRKGRBRBKBBRBBGGRRBGBGGBBBKKKRRRKRKBBKBGGB
100
GBKGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBGRRGBBBBKB
KKRRGRBBRKBGRRRRRKKBGRRBBGRBBRRKGRBRBKBBRBBGGRRBGBGGBBBKKKRRRKRKBBKBGGBKRRRRRKKRRRKGRRBRKRRKBRBBGRGB
150
BGBBRRKKRRGGRRBGGRBKBGBGBKGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBGRRGBBBBKBKKRRGRBBRKBGRRRRRKKBGRRBBGR
BBRRKGRBRBKBBRBBGGRRBGBGGBGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRRRRRGRBRGGGBBRBBKRKRKBKKRRKRGGGBBRBBGBGGBRBGRBKBBKRBGBRBGBRBRBRBRBRBGBRBBBRRRBGRBRGRRGBRR
200
BKGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBGRRGBBBBKBKKRRGRBBRKBGRRRRRKKBGRRBBGRBBRRKGRBRBKBBRBBGGRRBGBGGBBBKKKRRRKRKBBKBGGBKRRRRRKKRRRKGRRBRKRRKBRBBGRGBK
KBBKRKRRGBRKRRGBRBRKRKGBRBRKRBGBRBGBRBRBRBRBRBGBRBBBRRRBGRBRGRRGBRRBBBKBRBRBGBRBRBGBKBRBBKRRBBBBBRBBBKBRRBGRKBBBGRRRBBBBRBRBBBRBBRBBKBRKRKBBBRBBRBBRRRRKBRKRBGKRRBKRRBGKKGKBRRGGBBRKGRBBKRKKBBBBBRBBRKBB
500
BGBBRRKKRRGGRRBGGRBKBGBGBKGBBKKRKGBBKGRRGGKKBBBBKBGRBGRRRBGRRGRBRGGBBBKRRKBKKRKRGGBBRBBGBGGBRBGRBKBBRRKKRRRRRBGRBGRRGBBBBKBKKRRGRBBRKBGRRRRRKKBGRRBBGRBBRRKGRBRBKBBRBBGGRRBGBGGBBBKKKRRRKRKBBKBGGBKRRRRRKKRRRKGRRBRKRRKBRBBGRGBKKBBKRKRRGBRKRRGBRBRKRKGBRBRKRBGBRBGBRBRBRBRBRBGBRBBBRRRBGRBRGRRGBRRBBBKBRBRBGBRBRBGBKBRBBKRRBBBBBRBBBKBRRBGRKBBBGRRRBBBBRBRBBBRBBRBBKBRKRKBBBRBBRBBRRRRKBRKRBGKRRBKRRBGKKGKBRRGGBBRKGRBBKRKKBBBBBRBBRKBBRBBRBBRRBRBBGBBGBRBBRKBBKKBBGRRRRRRBRBGBKBRRRGRGBKKBRRBBBGGRBBBBKBBBBKKBKKBR
RKBBKRKBGBKKBGKGKKBGKBBBKKBRRKGKRKKRBKGKBRRBRKRKKRGKBBBKRBBGKBBGBBGKBGKGKBRBBGKBKGKRBGGRRKGBBBBKRGBGKGBKRBKRBKKBGGGRBRRRKBRRRGRKBRRGBKRKKRGBBBKRBBBGRGGKBBBBKBKBGKGBGBBGRKRRRRGRGGRKRGRBKRRKKRBRBKRKKBGGKKRRRKGRRBRKRRKBRBBGRGBKKBBKRKRRGBRKRRGBRBRKRKGBRBRKRBGBRBGBRBRBRBRBRBGBRBBBRRRBGRBRGRRGBRRBBBKBRBRBGBRBRBGBKBRBBKRRBBBBBRBBBKBRRBGRKBBBGRRRBBBBRBRBBBRBBRBBKBRKRKBBBRBBRBBRRRRKBRKRBGKRRBKRRBGKKGKBRRGGBBRKGRBBKRKKBBBBBRBBRKBBRBBRBBRRBRBBGBBGBRBBRKBBKKBBGRRRRRRBRBGBKBRRRGRGBKKBRRBBBGGRBBBBKBBBBKKBKKBR
'''

'''
10
RBKBGRBGGG
BGKRBRKBGB
'''

'''
LCS(최장 공통부분 수열)
 - 2개의 문자열을 비교하면서 부분 수열 중에서 공통된 가장 긴 부분수열을 골라내면 되는 문제
 -> 9251_LCS 문제로 가기
'''
T = int(input())
for t in range(1, T+1):
    N = int(input())
    x = input()
    y = input()

    board = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if x[i-1] == y[j-1]:
                board[i][j] = board[i-1][j-1]+1
            else:
                board[i][j] = max(board[i-1][j], board[i][j-1])
    answer = board[-1][-1] / N * 100
    print(f'#{t} {answer:.2f}')
