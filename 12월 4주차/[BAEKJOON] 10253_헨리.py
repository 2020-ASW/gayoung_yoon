# 실패
def calcu(a, b):
    temp = b // a

    new_a = a * (temp + 1) - b
    new_b = b * (temp + 1)
    
    if new_a == 1:
        return new_b
    else:
        return calcu(new_a, new_b)

# T = int(input())
# for t in range(1, T + 1):
#     a, b = map(int, input().split())
#     print(f'#{t} {calcu(a, b)}')


# new
def calcu_new(a, b):
    if a == 1:
        return b

    temp = b // a

    while True:
        new_a = a * temp - b
        new_b = b * temp
        print(new_a, new_b)
        if new_a < 0:
            temp += 1
        elif new_a == 0:
            return new_b
        else:
            return calcu(new_a, new_b)
        print(temp)
        print('------------')
T = int(input())
for t in range(1, T + 1):
    a, b = map(int, input().split())
    # print(f'#{t} {calcu(a, b)}')
    print(f'#{t} {calcu_new(a, b)}')

