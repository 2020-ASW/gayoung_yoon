def location(x):
    end = 0
    for i in range(1, 143):
        end += i

        if x <= end:
            return [i, x - end + i]

T = int(input())
for t in range(1, T + 1):
    a, b = map(int,input().split())

    if a == b:
        print(f'#{t} {0}')
    
    else:
        ax, ay = location(a)
        bx, by = location(b)
        dx, dy = ax - bx, ay - by
        if (dx < 0 and dy > 0) or (dx > 0 and dy < 0):
            time = abs(dx) + abs(dy)
        else:
            time = max(abs(dx), abs(dy))
        print(f'#{t} {time}')