
def calcu(a, b):
    temp = b // a

    new_a = a * (temp + 1) - b
    new_b = b * (temp + 1)
    # print(new_a, new_b)
    
    if new_a == 1:
        return new_b
    else:
        return calcu(new_a, new_b)

T = int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split())
    print(f'#{t} {calcu(a, b)}')
