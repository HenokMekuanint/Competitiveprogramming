# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
array=list(map(int,input().split()))
from collections import defaultdict
dictionary=defaultdict(int)
for num in array:
    dictionary[num]+=1
for num1 in dictionary:
    if dictionary[num1]==1:
        print(num1)



