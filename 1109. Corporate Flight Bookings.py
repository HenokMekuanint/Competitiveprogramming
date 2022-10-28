class Solution:
    def corpFlightBookings(self, booking: List[List[int]], n: int) -> List[int]:
        # [[1,2,10],[2,3,20],[2,5,25]], n = 5
        # 
        res=[0 for i in range(n)]                               
    
        for i in range(len(booking)):
            start=booking[i][0]
            end=booking[i][1]
            seats=booking[i][2]


            res[end-1]+=seats
            if start>1:
                res[start-2]-=seats

        for i in range(n-2,-1,-1):
            res[i]+=res[i+1]

        return res
