def reverseArray(arr):
    rev = []
    i = len(arr) - 1

    while i >= 0:
        rev.append(arr[i])
        i -= 1

    return rev
