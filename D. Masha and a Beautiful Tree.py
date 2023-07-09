for _ in range(int(input())):
    n=int(input())
    p=[*map(int,input().split())]
    j,ans,f=1,0,0
    while j<n:
        for i in range(0,n,j*2):
            if abs(p[i]-p[i+j])!=j : f=1
            if p[i]>p[i+j]: p[i],p[i+j],ans=p[i+j],p[i],ans+1
        j<<=1
    print([ans,-1][f])
