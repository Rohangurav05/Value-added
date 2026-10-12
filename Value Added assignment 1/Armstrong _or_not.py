def isArmstrong(n):
    arm = 0
    org = n
    power = len(str(n))

    while n > 0:
        rem = n % 10
        arm = rem ** power + arm
        n = n // 10

    return arm == org
