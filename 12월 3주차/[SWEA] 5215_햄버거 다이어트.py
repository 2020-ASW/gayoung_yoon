# dfs(+재귀)를 이용해 풀었다.
# 동적 프로그래밍으로도 풀 수 있다.https://blog.naver.com/PostView.nhn?blogId=ebchoi227&logNo=222114867672&categoryNo=14&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView

T = int(input())

def find(idx, sum_flavor, sum_kcal):
    global max_flavor

    if sum_kcal > L:
        return

    if max_flavor < sum_flavor:
        max_flavor = sum_flavor

    if idx == N:
        return

    flavor, kcal = kcal_list[idx]

    find(idx + 1, sum_flavor + flavor, sum_kcal + kcal)  # 다음거 선택
    find(idx + 1, sum_flavor, sum_kcal)  # 다음거 선택안함

for t in range(1, T+1):
    N, L = map(int, input().split())
    kcal_list = [list(map(int, input().split())) for _ in range(N)]  # 점수, 칼로리
    max_flavor = 0
    find(0,0,0)
    print('#{} {}'.format(t, max_flavor))

'''
1
5 1000
100 200
300 500
250 300
500 1000
400 400
'''

'''
sum_flavor, flavor
0 100
sum_kcal, kcal
0 200
------------------------------------
select_next
sum_flavor, flavor
100 300
sum_kcal, kcal
200 500
------------------------------------
select_next
sum_flavor, flavor
400 250
sum_kcal, kcal
700 300
------------------------------------
select_next
sum_flavor, flavor
650 500
sum_kcal, kcal
1000 1000
------------------------------------
select_next
not_select_next
sum_flavor, flavor
650 400
sum_kcal, kcal
1000 400
------------------------------------
select_next
not_select_next
not_select_next
sum_flavor, flavor
400 500
sum_kcal, kcal
700 1000
------------------------------------
select_next
not_select_next
sum_flavor, flavor
400 400
sum_kcal, kcal
700 400
------------------------------------
select_next
not_select_next
not_select_next
sum_flavor, flavor
100 250
sum_kcal, kcal
200 300
------------------------------------
select_next
sum_flavor, flavor
350 500
sum_kcal, kcal
500 1000
------------------------------------
select_next
not_select_next
sum_flavor, flavor
350 400
sum_kcal, kcal
500 400
------------------------------------
select_next
not_select_next
not_select_next
sum_flavor, flavor
100 500
sum_kcal, kcal
200 1000
------------------------------------
select_next
not_select_next
sum_flavor, flavor
100 400
sum_kcal, kcal
200 400
------------------------------------
select_next
not_select_next
not_select_next
sum_flavor, flavor
0 300
sum_kcal, kcal
0 500
------------------------------------
select_next
sum_flavor, flavor
300 250
sum_kcal, kcal
500 300
------------------------------------
select_next
sum_flavor, flavor
550 500
sum_kcal, kcal
800 1000
------------------------------------
select_next
not_select_next
sum_flavor, flavor
550 400
sum_kcal, kcal
800 400
------------------------------------
select_next
not_select_next
not_select_next
sum_flavor, flavor
300 500
sum_kcal, kcal
500 1000
------------------------------------
select_next
not_select_next
sum_flavor, flavor
300 400
sum_kcal, kcal
500 400
------------------------------------
select_next
not_select_next
not_select_next
sum_flavor, flavor
0 250
sum_kcal, kcal
0 300
------------------------------------
select_next
sum_flavor, flavor
250 500
sum_kcal, kcal
300 1000
------------------------------------
select_next
not_select_next
sum_flavor, flavor
250 400
sum_kcal, kcal
300 400
------------------------------------
select_next
not_select_next
not_select_next
sum_flavor, flavor
0 500
sum_kcal, kcal
0 1000
------------------------------------
select_next
sum_flavor, flavor
500 400
sum_kcal, kcal
1000 400
------------------------------------
select_next
not_select_next
not_select_next
sum_flavor, flavor
0 400
sum_kcal, kcal
0 400
------------------------------------
'''