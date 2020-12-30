'''
2
4
Fred B
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
'''

# def find_friend(friend):
#     if friend

# T = int(input())
numbers = int(input())
check = {}
for number in range(numbers):
    x, y = input().split()
    if x not in check and y not in check:
        check[x] = [y]
        check[y] = [x]
    elif x in check and y not in check:
        check[x].append(y)
        check[y] = [x]
    elif x not in check and y in check:
        check[y].append(x)
        check[x] = [y]
    else:
        check[x].append(y)
        check[y].append(x)
    
    answer = check[x]
    print(answer)
    # for friend in check[x]:
    #     print(check[friend])  # 이렇게 되면 2개밖에 갈 수 없다.
    



'''
3
Fred Barney
{'Fred': ['Barney'], 'Barney': ['Fred']}
Barney Betty
{'Fred': ['Barney'], 'Barney': ['Fred', 'Betty'], 'Betty': ['Barney']}
Betty Wilma
{'Fred': ['Barney'], 'Barney': ['Fred', 'Betty'], 'Betty': ['Barney', 'Wilma'], 'Wilma': ['Betty']}
'''