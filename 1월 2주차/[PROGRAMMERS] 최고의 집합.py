def solution(n, s):
    if n > s:
        return [-1]

    a, b = divmod(s, n)
    temp = [a] * n
    for i in range(1, b + 1):
        temp[i-1] += 1

    temp = sorted(temp)
    return temp

# n, s = 2, 1
n, s = 3, 11
# n, s = 2, 8

'''
원소의 곱이 최대가 되기 위해서는 분산이 가장 작아야한다.
'''


