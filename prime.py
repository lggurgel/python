def prime(k):
    for n in range(2, k):
        for x in range(2, n):
            if n % x == 0:
                #print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is a prime number')


prime(10000)