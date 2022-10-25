class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        
#         [100,40,17,9,73,75]    3
#              L
#                    R 
        
#         TOTAL=40
#         WINDOWLEN=LEN(CARDPOINTS)-K
#         MAX=0
#         cursum
#         MAX=TOTAL-CURSUM
        
        total=sum(cardPoints)
        if k==len(cardPoints): return total
        windowlen=len(cardPoints)- k
        maximum=0
        left=0
        cursum=0
        windowsum=0
        for right in range(len(cardPoints)):
            windowsum+=cardPoints[right]
            while (right-left+1)==windowlen:
                cursum=total-windowsum
                maximum=max(maximum,cursum)
                windowsum-=cardPoints[left]
                left+=1
        return maximum
