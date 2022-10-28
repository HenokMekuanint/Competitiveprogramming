class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # [[2,1,5],[3,3,7]] capacity = 4
        #                    find the max to
        # [0,-3,0,0,2,0,3,0]
        # start=3 end=7 numspass=3
        #startindex=2 endindex=6
        maxtrip=0
        for i in range(len(trips)):
            if trips[i][2]>maxtrip:
                maxtrip=trips[i][2]
        res=[0 for i in range(maxtrip)]
        
        
        for i in range(len(trips)):
            start=(trips[i][1])-1
            end=(trips[i][2])-1
            numberofpassenger=(trips[i][0])
            res[end-1]+=numberofpassenger    
            if start>0:
                res[start-1]-=numberofpassenger
        total=0
        for i in range(len(res)-1,-1,-1):
            total+=res[i]
            if total>capacity:
                return False
            res[i]=total
            
        return True
            
            
                
        
