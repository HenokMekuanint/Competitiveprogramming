# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
from collections import defaultdict
dictionary=defaultdict(int)
for i in range(0,n):
    inp=input()
    dictionary[inp]+=1
print(len(dictionary.keys()))
for key in dictionary:
    print(dictionary[key],end=" ")
