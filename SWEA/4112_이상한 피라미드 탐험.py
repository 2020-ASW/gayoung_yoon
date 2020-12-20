def location(x):
    end = 0
    for i in range(1, 200):
        end += i

        if x <= end:
            return [i, x - end + i]

T = int(input())
for t in range(1, T + 1):
    a, b = map(int,input().split())

    if a > b:
        a, b = b, a

    ax, ay = location(a)
    bx, by = location(b)
    dx, dy = abs(ax - bx), abs(ay - by)

    time = max(dx, dy)
    print(f'#{t} {time}')