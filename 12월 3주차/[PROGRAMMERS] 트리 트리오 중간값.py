from collections import deque

def bfs(graph, start):
    dist = []
    queue = deque([[start, 0]])
    visit = {start: 1}
    # print('queue')
    # print(queue)

    while queue:
        cur_mode, cur_dist = queue.popleft()
        # print(cur_mode, cur_dist)
        dist.append([cur_mode, cur_dist])

        for val in graph[cur_mode]:
            # print('graph[cur_mode]')
            # print(graph[cur_mode])
            # print('val')
            # print(val)
            if val not in visit:
                queue.append([val, cur_dist + 1])
                # print('queue')
                # print(queue)
                # print('------------------------')
                visit[val] = 1
    # print('==========================================')
    return dist


def solution(n, edges):
    graph = {i + 1: [] for i in range(n)}
    for cur in edges:
        graph[cur[0]].append(cur[1])
        graph[cur[1]].append(cur[0])
    # print(graph)
    start = bfs(graph, 1)
    # print(start)
    check1, check2 = start[-2][1], start[-1][1]
    end = bfs(graph, start[-1][0])
    if check1 == check2:
        return end[-1][1]
    else:
        return end[-2][1]


# n = 4
# edges = [[1,2],[2,3],[3,4]]  # 2

n = 5
edges = [[1,5],[2,5],[3,5],[4,5]]  # 2





'''
{1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
queue
deque([[1, 0]])
1 0
graph[cur_mode]
[2]
val
2
queue
deque([[2, 1]])
------------------------
2 1
graph[cur_mode]
[1, 3]
val
1
graph[cur_mode]
[1, 3]
val
3
queue
deque([[3, 2]])
------------------------
3 2
graph[cur_mode]
[2, 4]
val
2
graph[cur_mode]
[2, 4]
val
4
queue
deque([[4, 3]])
------------------------
4 3
graph[cur_mode]
[3]
val
3
==========================================
[[1, 0], [2, 1], [3, 2], [4, 3]]
'''

'''
{1: [5], 2: [5], 3: [5], 4: [5], 5: [1, 2, 3, 4]}
queue
deque([[1, 0]])
1 0
graph[cur_mode]
[5]
val
5
queue
deque([[5, 1]])
------------------------
5 1
graph[cur_mode]
[1, 2, 3, 4]
val
1
graph[cur_mode]
[1, 2, 3, 4]
val
2
queue
deque([[2, 2]])
------------------------
graph[cur_mode]
[1, 2, 3, 4]
val
3
queue
deque([[2, 2], [3, 2]])
------------------------
graph[cur_mode]
[1, 2, 3, 4]
val
4
queue
deque([[2, 2], [3, 2], [4, 2]])
------------------------
2 2
graph[cur_mode]
[5]
val
5
3 2
graph[cur_mode]
[5]
val
5
4 2
graph[cur_mode]
[5]
val
5
==========================================
[[1, 0], [5, 1], [2, 2], [3, 2], [4, 2]]
'''
