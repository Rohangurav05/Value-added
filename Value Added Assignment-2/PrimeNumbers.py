def isPrime(n):
    root = int(n ** 0.5)

    if n < 2:
        return False

    if n >= 2:
        for i in range(2, root + 1):
            if n % i == 0:
                return False

        return True
