for i in range(1,len(arr)):
    current=arr[i]
    j=i-1
    while j>=0 and arr[j]>current:
        arr[j+1]=arr[j]
        j=j-1
        for i in arr:
            print(i,end=" ")
        print(" ")
    arr[j+1]=current
for i in arr:
    print(i,end=" ")
