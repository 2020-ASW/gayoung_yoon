'''
Union find 문제 -> disjoint set 알고리즘
친구 네트워크의 숫자를 위해 하나의 거대한 union network의 parent에 몇명의 친구가 있는지 저장하는 number 딕셔너리를 정의

[풀이 로직]
1. 두 사람의 이름을 입력받은 후, 딕셔너리 parents에 없는 이름이라면 추가해준다.
2. 두 이름을 합쳐 친구관계를 만든다.
3. 현재까지 해당 친구관계를 포함하여 같은 집합에 있는 원소의 개수를 출력한다.

[코드]
1. getParent
   - parents 딕셔너리를 참조해 부모 노드를 알 수 있다.
   - 입력받는 노드가 부모노드이면 그대로 반환하지만, 그렇지 안으면 재귀를 이용해 부모노드를 찾는다.
2. unionParent
   - 두 노드를 합치는 역할
   - 두 노드가 속한 집합의 부모 노드를 찾아 비교. 부모노드를 갖지 않으면 x를 기준으로 두 집합을 합친다.(이때 cnt+=1)
'''

'''
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
'''
import sys
input = sys.stdin.readline

def getParents(parents, x):
    if parents[x] == x:
        return x
    
    p = getParents(parents, parents[x])
    parents[x] = p
    return p


def unionParents(parents, x, y, cnt):
    a = getParents(parents, x)
    b = getParents(parents, y)

    if a != b:
        parents[b] = a
        cnt[a] += cnt[b]


def findParents(parents, x):
    if parents[x] == x:
        return x
    
    return findParents(parents, parents[x])

for i in range(int(input())):
    parents = {}
    cnt = {}
    for _ in range(int(input())):
        x, y = input().split()

        if x not in parents:
            parents[x] = x
            cnt[x] = 1

        if y not in parents:
            parents[y] = y
            cnt[y] = 1

        
        unionParents(parents, x, y, cnt)
        print(cnt[findParents(parents, x)])