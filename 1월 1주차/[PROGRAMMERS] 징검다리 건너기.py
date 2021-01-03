def solution(stones, k):
    answer = 0
    left, right = 0, max(stones)
    while left <= right:
        mid = (left + right) // 2
        cnt = 0  # 몇칸 띌 것인가 -> k랑 비교
        for stone in stones:
            '''
            니니즈 친구들이 돌을 건널 때, 돌의 높이 = 지나가는 인원 - 돌의 높이
            인원 - 돌의 높이 <= 0가 k이상이 되면 친구들의 인원을 줄이고, k미만이면 돌을 지나는 인원 수를 늘림
            이분탐색의 결과 : 최대로 강을건널 수 있는 인원
            '''
            if stone < mid:
                '''
                stone - mid가 0이면 이번에는 건널 수 있다는 것이다.
                즉, stone < mid이면 전 사람이 건널 때 0이 되어 건너지 못하게 되었다는 것
                건너 뛰는 값을 +1해준다.
                '''
                cnt += 1
                if cnt >= k:  # 만약에 연속으로 0이 k번 이상 나타나면
                    right = mid - 1  # 더 작은 구간에서 찾아야한다.
                    break
            else:
                cnt = 0
        else:
            answer = mid
            left = mid + 1

    # print(answer)
    return answer