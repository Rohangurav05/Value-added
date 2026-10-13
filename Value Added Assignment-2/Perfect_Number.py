def isPerfectNumber(n):
    if n <= 1:
        return False

    root = int(n ** 0.5)
    sum1 = 1

    for i in range(2, root + 1):
        if n % i == 0:
            sum1 += i

            if i != n // i:
                sum1 += n // i

    return sum1 == n
