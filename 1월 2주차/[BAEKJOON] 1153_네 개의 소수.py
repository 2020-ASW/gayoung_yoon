def make_prime(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False

    return primes


n = int(input())
if n < 8:
    print(-1)

if n >= 8 and n % 2 == 0:
    answer = '2 3 '
    n -= 5

elif n >= 8 and n % 2 == 1:
    answer = '2 2 '
    n -= 4

primes = make_prime(n)

for i in range(2, n+1):
    if i in primes and (n - i) in primes:
        answer += str(i) + ' ' + str(n-i)
        print(answer)
        exit()
