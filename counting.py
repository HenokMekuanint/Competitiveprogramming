def countingSort(arr):
    # Write your code here
    newarray=[0 for i in range(100)]
    for i in arr:
        newarray[i]+=1
    return newarray
