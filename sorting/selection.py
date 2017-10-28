def selection(arr):
    i = 0
    length = len(arr)

    while i != length - 1:
        min_index = arr[i]
        for j in range(i, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        i += 1
    return arr
