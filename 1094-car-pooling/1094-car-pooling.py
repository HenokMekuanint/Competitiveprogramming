class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        size=0
        for i in range(len(trips)):
            size=max(trips[i][2],size)
        location=[0 for i in range(size+1)]
        for numpassenger,start,end in trips:
            location[start]+=numpassenger
            location[end]-=numpassenger
        total=0
        for i in range(len(location)):
            total+=location[i]
            if total>capacity:
                return False
            location[i]=total
        return True
            