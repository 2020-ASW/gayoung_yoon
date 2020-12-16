# S = "B"
# T = "ABBA"

# S = "AB"
# T = "ABB"

'''
조건1 문자열의 뒤에 A를 추가한다.
조건2 문자열을 뒤집고 뒤에 B를 추가한다.
S -> T를 확인하기 위해 T -> S로 변경가능한지 check!
'''
S = list(input())
T = list(input())

while True:
    if len(S) == len(T):
        break

    if T[-1] == 'A':
        T.pop()

    else:
        T.pop()
        T = T[::-1]

if S == T:
    print(1)
else:
    print(0)