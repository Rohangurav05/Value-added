def findLcm(n1, n2):
    max1 = max(n1, n2)

    for i in range(1, n1 * n2 + 1):
        num = max1 * i

        if num % n1 == 0 and num % n2 == 0:
            return num
