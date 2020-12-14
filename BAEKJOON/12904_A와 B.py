# S = "B"
# T = "ABBA"

# S = "AB"
# T = "ABB"

'''
문자열의 뒤에 A를 추가한다.
문자열을 뒤집고 뒤에 B를 추가한다.
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