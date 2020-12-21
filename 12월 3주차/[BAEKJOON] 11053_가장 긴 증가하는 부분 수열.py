# LIS(3745위한 연습1)

# 1. dp 이용
x = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(x)]

for i in range(x):
    for j in range(i):
        # print(i, j)
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
            # print(dp)
print(max(dp))
'''
6
10 20 10 30 20 50
1 0
[1, 2, 1, 1, 1, 1]
2 0
2 1
3 0
[1, 2, 1, 2, 1, 1]
3 1
[1, 2, 1, 3, 1, 1]
3 2
[1, 2, 1, 3, 1, 1]
4 0
[1, 2, 1, 3, 2, 1]
4 1
4 2
[1, 2, 1, 3, 2, 1]
4 3
5 0
[1, 2, 1, 3, 2, 2]
5 1
[1, 2, 1, 3, 2, 3]
5 2
[1, 2, 1, 3, 2, 3]
5 3
[1, 2, 1, 3, 2, 4]
5 4
[1, 2, 1, 3, 2, 4]
'''
