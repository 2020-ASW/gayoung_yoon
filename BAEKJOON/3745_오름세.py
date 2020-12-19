# 최장 증가 부분 수열(LIS)
'''
푸는방법1. DP이용
  - i번째 인덱스에서 끝나는 최장증가부분수열의 마지막에 arr[k]를 추가했을 때의 LIS길이와
    추가하지 않고 기존의 length[k]값 중에 더 큰값으로 length[k]를 갱신
  - 시간복잡도 O(n^2)
푸는방법2. 이분탐색
  - 시간복잡도 O(log n)
  - 
'''

def move(i):
    if dp[-1] < i:
        dp.append(i)
        # print('dp_start')
        # print(dp)
        return dp

    start, end = 0, len(dp)
    while start <= end:
        mid = (start + end) // 2
        # print(start, mid, end)
        if dp[mid] < i:
            start = mid + 1
        
        else:
            end = mid - 1
    dp[start] = i
    # print('dp_final')
    # print(start,end)
    # print(dp)

while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [0]

        for i in arr:
            move(i)
            # print(i)
            # print(move(i))
            # print('-------------------------------')
        print(len(dp)-1)
    
    except:
        break
    

'''
6
5 2 1 4 5 3
5
dp_start
[0, 5]
[0, 5]
-------------------------------
2
0 1 2
0 0 0
dp_final
[0, 2]
None
-------------------------------
1
0 1 2
0 0 0
dp_final
[0, 1]
None
-------------------------------
4
dp_start
[0, 1, 4]
[0, 1, 4]
-------------------------------
5
dp_start
[0, 1, 4, 5]
[0, 1, 4, 5]
-------------------------------
3
0 2 4
0 0 1
1 1 1
dp_final
[0, 1, 3, 5]
None
-------------------------------
'''