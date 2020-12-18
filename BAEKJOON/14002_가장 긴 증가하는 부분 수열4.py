# LIS(3745위한 연습2)

# 2. 이분탐색 이용
def move(i):
    return 0

n = int(input())
arr = list(map(int,input().split()))
dp = [0]
for i in arr:
    if i > dp[-1]:
        dp.append(i)
    print('dp_start')
    print(dp)
    start, end = 0, len(dp)
    while start <= end:
        mid = (start + end) // 2
        print(start, mid, end)
        if i > dp[mid]:
            start = mid + 1
        else:
            end = mid - 1
    dp[start] = i
    print('dp_final')
    print(dp)

'''
6
10 20 10 30 20 50
dp_start
[0, 10] 
0 1 2   
0 0 0
dp_final
[0, 10]
dp_start
[0, 10, 20]
0 1 3
2 2 3
dp_final
[0, 10, 20]
dp_start
[0, 10, 20]
0 1 3
0 0 0
dp_final
[0, 10, 20]
dp_start
[0, 10, 20, 30]
0 2 4
3 3 4
dp_final
[0, 10, 20, 30]
dp_start
[0, 10, 20, 30]
0 2 4
0 0 1
1 1 1
dp_final
[0, 10, 20, 30]
dp_start
[0, 10, 20, 30, 50]
0 2 5
3 4 5
3 3 3
dp_final
[0, 10, 20, 30, 50]
'''