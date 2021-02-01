import cProfile


def version1(n):
    i = 2
    sieve = []
    result = False
    while not result:
        if i != 2:
            for j in sieve:
                if i % j == 0:
                    break
            else:
                sieve.append(i)
        else:
            sieve.append(i)
        i += 1
        result = len(sieve) == n
    return sieve[-1]
# 100
# 1000 loops, best of 5: 218 usec per loop
# 644 function calls in 0.000 seconds


# 500
# 1000 loops, best of 5: 4.99 msec per loop
# 4074 function calls in 0.006 seconds


# 1000
# 1000 loops, best of 5: 20.9 msec per loop
# 8922 function calls in 0.022 seconds


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def version2(n):
    result = False
    i = 1
    counter = 0
    while not result:
        i += 1
        if isPrime(i):
            counter += 1
        result = counter == n
    return i
# 100
# 1000 loops, best of 5: 174 usec per loop
# 544 function calls in 0.000 seconds


# 500
# 1000 loops, best of 5: 1.68 msec per loop
# 3574 function calls in 0.002 seconds

# 1000
# 1000 loops, best of 5: 4.44 msec per loop
# 7922 function calls in 0.006 seconds


# cProfile.run('version1(1000)')
# cProfile.run('version2(1000)')
