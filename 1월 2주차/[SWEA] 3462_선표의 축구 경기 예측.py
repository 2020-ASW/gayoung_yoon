'''
3
50 50
70 20
100 100
'''

# 적어도 한 팀이 소수로 득점 = 1 - 모든 팀이 소수로 득점하지 않음

T = int(input())

def factorial(n):
    if n == 1:
        return 1
    else: 
        return n * factorial(n-1)
 
def make_val(x, y):
    return factorial(x) / (factorial(x-y) * factorial(y))

for t in range(1, T + 1):
    a, b = map(int, input().split())
    temp = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    a, b = a/100, b/100
    ans_a, ans_b = 0, 0
    for i in range(len(temp)):
        aa, bb = 1, 1
        aa *= make_val(30, temp[i]) * (a ** temp[i]) * ((1-a) ** (30-temp[i]))
        bb *= make_val(30, temp[i]) * (b ** temp[i]) * ((1-b) ** (30-temp[i]))
        ans_a += aa
        ans_b += bb

    answer =round(1- (1-ans_a)*(1-ans_b), 5)
    print(f'#{t} {answer:.5f}')  # 0인 경우 0.0으로 나타남