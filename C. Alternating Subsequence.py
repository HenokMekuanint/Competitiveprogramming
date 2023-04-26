for i in range(int(input())):
	n=int(input())
	L=list(map(int,input().split()))
	sum=0
	a=L[0]
	for i in L:
		if(a//i<0):
			sum+=a
			a=i
		if(a<i):
			a=i
 
	print(sum+a)
