def returnLargestDigit(n):
    large_digit = 0

    while n > 0:
        rem = n % 10

        if large_digit < rem:
            large_digit = rem

        n = n // 10

    return large_digit
