class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        "   1   1   0   "
        [1,1,3]
        
        """
        ans=[]
        for i in range(len(boxes)):
            counter=0
            for j in range(len(boxes)):
                if i!=j and boxes[j]=="1":
                    counter+=abs(i-j)
            ans.append(counter)
        return ans
                
            
            