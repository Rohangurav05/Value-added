def gcdOfTwoNumbers(n1, n2):
    min1 = min(n1, n2)
    gcd = 0

    for i in range(1, min1 + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i

    return gcd
