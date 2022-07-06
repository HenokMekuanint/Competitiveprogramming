def selectionSort():
    arr = [4, 1, 3, 7, 9]
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return(arr)
selectionSort()
