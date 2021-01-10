def make_prime(n):
    a = [False,False] + [True]*(n-1)

    for i in range(2,n+1):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j] = False

    return a


n = int(input())
answer = ''  # answer를 초기화하자!!
if n < 8:
    print(-1)

if n >= 8 and n % 2 == 1:
    answer = '2 3 '
    n -= 5

elif n >= 8 and n % 2 == 0:
    answer = '2 2 '
    n -= 4
# print(n)
primes = make_prime(n)
# print(primes)
for i in range(2, n+1):
    if primes[i] and primes[n - i]:
        answer += str(i) + ' ' + str(n-i)
        print(answer)
        break