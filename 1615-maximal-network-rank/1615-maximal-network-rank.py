class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        dicti=defaultdict(list)
        for neigh1,neigh2 in roads:
            dicti[neigh1].append(neigh2)
            dicti[neigh2].append(neigh1)
        temp=list(dicti.keys())
        ans=0
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                cur=len(dicti[temp[i]])+len(dicti[temp[j]])
                if temp[i] in dicti[temp[j]]:
                    cur-=1
               
                ans=max(ans,cur)
                
        return ans
        
        