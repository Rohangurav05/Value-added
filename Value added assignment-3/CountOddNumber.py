def countOddNumbers(n, array):
    count = 0
    for i in range(len(array)):
        if array[i] % 2 != 0:
            count += 1
    return count
