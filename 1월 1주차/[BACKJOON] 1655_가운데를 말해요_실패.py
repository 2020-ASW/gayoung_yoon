# # 시간초과
# from bisect import bisect_left  # 이진탐색할 때 사용

# n = int(input())
# check = []
# number = int(input())
# check.append(number)
# print(number)

# len_check = 1

# for i in range(n-1):
#     number = int(input())
    
#     idx = bisect_left(check, number)
#     check.insert(idx, number)

#     len_check += 1

#     if len_check % 2 == 0:
#         print(min(check[len_check//2-1], check[len_check//2]))
#     else:
#         print(check[len_check//2])


# # 힙정렬 -> 시간초과
# import heapq

# n = int(input())
# heap = []

# for _ in range(n):
#     number = int(input())
#     heapq.heappush(heap, number)
#     temp = list(heap)
#     # heap에서 그대로 heappop을 해버리면 갯수가 줄어든 채로 계속 진행이 된다. temp로 복사한 다음에 temp에서만 heappop진행해야함.
#     # print(temp)
#     # print(heap)
#     for i in range((len(temp)+1)//2 - 1):
#         heapq.heappop(temp)
#     print(temp[0])
#     # print('-------------------------------------------------')


'''
- 중앙값을 기준으로 큰 값은 오른쪽(min_heap)에, 작은 값은 왼쪽(max_heap)에 저장한다.
- 중앙값은 max_heap의 맨 첫번째 값이 되도록 구성
1. 왼쪽과 오른쪽 원소의 길이가 같으면, 왼쪽에 새 값을 저장
2. 만약 오른쪽 heap의 값보다 왼쪽heap이 더 크면, 왼쪽과 오른쪽 원소값을 바꾼다.
# '''
import heapq

n = int(input())

max_heap = []  # 최대 힙 -> 중앙값은 max_heap의 첫번째 값
min_heap = []  # 최소 힙(중앙값보다 ㅈ)

# max = left, min = right

for i in range(1, n+1):
    number = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-number, number))  # max_heap
    else:
        heapq.heappush(min_heap, (number, number))  # min_heap

    if min_heap and max_heap[0][1] > min_heap[0][1]:
        new_max = heapq.heappop(max_heap)[1]
        new_min = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-new_min, new_min))
        heapq.heappush(min_heap, (new_max, new_max))

    if i % 2 == 1:
        print('answer')
        print(max_heap[0][1])
    else:
        print('answer')
        print(min(max_heap[0][1], min_heap[-1][1]))


# 통과 코드
# import sys
# import heapq

# def push_heap(left_heap, right_heap, num, n):
#     # 숫자의 개수가 홀수이면 오른쪽에 넣고, 짝수면 왼쪽에 넣기
#     if n % 2 == 1:
#         heapq.heappush(right_heap, num)
#     else:
#         heapq.heappush(left_heap, -num)


# def make_mid_heap(left_heap, right_heap):
#     # 레프트의 최대값이 라이트의 최소값보다 크면 위치 교환
#     if left_heap:  # 라이트만 있을 수 있기 때문에 if문 처리
#         left_max = -left_heap[0]
#         right_min = right_heap[0]
#         if left_max > right_min:
#             heapq.heappush(left_heap, -heapq.heappop(right_heap))
#             heapq.heappush(right_heap, -heapq.heappop(left_heap))


# def get_mid_number(left_heap, right_heap, n):
#     # 숫자의 개수가 홀수이면, 라이트에서 최소값을 반환
#     # 숫자의 개수가 짝수이면, 레프트 최대와 라이트 최소를 비교하여 최소값 반환
#     if n % 2 == 1:
#         return right_heap[0]
#     else:
#         return min(-left_heap[0], right_heap[0])


# N = int(input())  # 숫자의 개수
# left_numbers = []  # 최대 힙(최대값을 음수로 넣어 최대값이 0번에 오게 한다)
# right_numbers = []  # 최소 힙

# for i in range(1, N + 1):
#     number = int(input())
#     push_heap(left_numbers, right_numbers, number, i)
#     make_mid_heap(left_numbers, right_numbers)
#     print(left_numbers)
#     print(right_numbers)
#     print('------------------------------------------------')
# print('===============================================')
    # answer = get_mid_number(left_numbers, right_numbers, i)
    # print(answer)


