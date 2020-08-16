def n_primos(x):
    n = n1 =  2
    primo = 0
    while n <= x:

        if n % n1 == 0 and n != n1:
            n = n + 1
            n1 = 2
            
        elif n == n1:
            primo = primo + 1
            n = n + 1
            n1 = 2
            
        else:
            n1 = n1 + 1

    return primo

