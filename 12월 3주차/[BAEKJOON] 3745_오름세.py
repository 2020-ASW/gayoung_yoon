# 최장 증가 부분 수열(LIS)
'''
푸는방법1. DP이용
  - i번째 인덱스에서 끝나는 최장증가부분수열의 마지막에 arr[k]를 추가했을 때의 LIS길이와
    추가하지 않고 기존의 length[k]값 중에 더 큰값으로 length[k]를 갱신
  - 시간복잡도 O(n^2)
푸는방법2. 이분탐색
  - 시간복잡도 O(log n)
  - 이분탐색으로 중앙(mid)에서 그것보다 큰것중에 가장 작은거 찾아서 갱신
'''

def move(i):
    if dp[-1] < i:
        dp.append(i)
        return dp

    start, end = 0, len(dp)
    while start <= end:
        mid = (start + end) // 2

        if dp[mid] < i:
            start = mid + 1
        else:
            end = mid - 1

    dp[start] = i

while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [0]

        for i in arr:
            move(i)
        print(len(dp)-1)
    
    except:
        break
    

'''
6
5 2 1 4 5 3
i       
5       
move(i) 
dp_start
[0, 5]  
[0, 5]
-------------------------------
i
2
move(i)
==========================
come
[0, 5]
start, mid, end
0 1 2
end
0
start, mid, end
0 0 0
start
1
dp_final
1 0
[0, 2]
None
-------------------------------
i
1
move(i)
==========================
come
[0, 2]
start, mid, end
0 1 2
end
0
start, mid, end
0 0 0
start
1
dp_final
1 0
[0, 1]
None
-------------------------------
i
4
move(i)
dp_start
[0, 1, 4]
[0, 1, 4]
-------------------------------
i
5
move(i)
dp_start
[0, 1, 4, 5]
[0, 1, 4, 5]
-------------------------------
i
3
move(i)
==========================
come
[0, 1, 4, 5]
start, mid, end
0 2 4
end
1
start, mid, end
0 0 1
start
1
start, mid, end
1 1 1
start
2
dp_final
2 1
[0, 1, 3, 5]
None
-------------------------------
3
'''

def move(i):
    if dp[-1] < i:
        dp.append(i)
        # print('dp_start')
        # print(dp)
        return dp

    start, end = 0, len(dp)
    # print('==========================')
    # print('come')
    # print(dp)
    while start <= end:
        mid = (start + end) // 2
        # print('start, mid, end')
        # print(start, mid, end)
        if dp[mid] < i:
            start = mid + 1
            # print('start')
            # print(start)
        else:
            end = mid - 1
            # print('end')
            # print(end)
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
            # print("i")
            # print(i)
            # print('move(i)')
            # print(move(i))
            # print('-------------------------------')
        print(len(dp)-1)
    
    except:
        break
    