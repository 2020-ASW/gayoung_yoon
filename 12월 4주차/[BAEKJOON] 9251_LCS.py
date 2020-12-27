# SWEA 1264를 위한 공부
'''
x = ACAYKP
y = CAPCAK
answer = ACAK
------------------------------------------------------
[풀이방법]
x = A
y = C -> LCS길이 = 0

x = A
y = CA -> LCS길이 = 1

x = A
y = CAP -> LCS길이 = 1

x = A
y = CAPC -> LCS길이 = 1

x = A
y = CAPCA -> LCS길이 = 1

x = A
y = CAPCAK -> LCS길이 = 1
============================
x = AC
y = C -> LCS길이 = 1

x = AC
y = CA -> LCS길이 = 1

x = AC
y = CAP -> LCS길이 = 1

x = AC
y = CAPC -> LCS길이 = 2

x = AC
y = CAPCA -> LCS길이 = 2

x = AC
y = CAPCAK -> LCS길이 = 2
...
------------------------------------------------------
[표로 나타내기]
   0  C  A  P  C  A  K (y)
0  0  0  0  0  0  0  0 
A  0  0  1  1  1  1  1
C  0  1  1  1  2  2  2
A  0  1  2  2  2  3  3
Y  0  1  2  2  2  3  3
K  0  1  2  2  2  3  4
P  0  1  2  3  3  3  4
(x)
x와 y에 가장최근에 추가된 글자가 서로 같으면 board[i][j] = board[i-1][j-1]+1
x와 y에 가장최근에 추가된 글자가 서로 다르면 board[i][j] = max(board[i-1][j], board[i][j-1])
'''

# x = 'ACAYKP'
# y = 'CAPCAK'

x = input()
y = input()
len_x = len(x)
len_y = len(y)

board = [[0] * (len_y+1) for _ in range(len_x+1)]

for i in range(1, len_x + 1):
    for j in range(1, len_y + 1):
        if x[i-1] == y[j-1]:
            board[i][j] = board[i-1][j-1]+1
        else:
            board[i][j] = max(board[i-1][j], board[i][j-1])

print(board[-1][-1])