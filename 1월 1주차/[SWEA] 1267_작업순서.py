'''
3 2
2 1 1 3  # 2 1 3
4 3
1 4 2 3 4 2   # 1 4 2 3 
5 4
2 4 3 5 2 3 1 2   # 1 2 3 5 4 
'''
for t in range(1, 11):
    start, end = map(int, input().split())
    data = list(map(int, input().split()))
    adj = [[] for i in range(start + 1)]
    visit = [None] + [0] * start
 
    for i in range(0, len(data), 2):
        adj[data[i]].append(data[i + 1]) 
        visit[data[i + 1]] += 1
 
    # adj = [[], [3], [1], []]
    # visit = [None, 1, 0, 1]
 
    answer = ''
    for i in range(1, start+1):
        stack = [i]
        while stack:
            node = stack.pop()
            # print('node')
            # print(node)
            if visit[node] > 0:
                visit[node] -= 1
            elif visit[node] == 0:
                visit[node] = None
                answer += str(node) + ' '
                stack.extend(adj[node])
 
    print(f'#{t} {answer}')