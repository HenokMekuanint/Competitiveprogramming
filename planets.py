def planets(com,orbits):
    from collections import defaultdict
    dicti=defaultdict(int)
    ans=0
    for i in orbits:
        dicti[i]+=1
    for j in dicti:
        if dicti[j]>=com:
            ans+=com
        else:
            ans+=dicti[j]
    return ans
        
for i in range(int(input())):
    size,com=map(int,input().split())
    orbits=list(map(int,input().split()))
    print(planets(com,orbits))
