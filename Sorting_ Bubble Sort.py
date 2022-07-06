def countSwaps(a):
    # Write your code here
    count=0
    for j in range(0,len(a)):
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                count+=1
                a[i],a[i + 1] =a[i + 1],a[i]
    print("Array is sorted in"+count+"swap")
    print("First Element:"+a[0])
    print("Last Element:"+a[len(a)-1])
