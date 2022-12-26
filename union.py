# Enter your code here. Read input from STDIN. Print output to STDOUT
size1=input()
english=set(input().split())
size2=input()
french=set(input().split())
print(len(english.union(french)))
