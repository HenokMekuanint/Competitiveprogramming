array=[1,2,4,5,6,7,5,3,3,2,1]

def merge_sort(array):
    if len(array)>1:
        left_arr=array[:len(array)//2]
        right_arr=array[len(array)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i=0
        j=0
        k=0

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k]=left_arr[i]

                i+=1
                k+=1

            else:
                array[k]=right_arr[j]
                j+=1
                k+=1
        while i<len(left_arr):
            array[k]=left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            array[k]=right_arr[j]
            j+=1
            k+=1
    return array


def selection_sort(array):
    for i in range(0,len(array)):
        for j in range(i,len(array)):
            if array[i]>array[j]:
                array[i],array[j]=array[j],array[i]
    return array

def quick_sort(arr,left,right):
    if left<right:
        partition_pos=partition(arr,left,right)
        quick_sort(arr,left,partition_pos-1)
        quick_sort(arr,partition_pos+1,right)
    return arr
def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]

    while i<j:
        while i <right and arr[i] <pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1

        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i
def insertion_sorting(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            arr[j] = key
            
            j -= 1

    return arr

print(insertion_sorting(array))
