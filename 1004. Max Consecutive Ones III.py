class Solution:
    def longestOnes(self, nums: List[int], K: int) -> int:
        i=0;n=len(nums);j=0
        countk=K;res=float('-inf')
        while j<n and i<n:
            if nums[j]==1:
                pass
            else:   
                if countk>0:
                    countk-=1
                else:
                    while countk<0 or nums[i]==1:
                        if nums[i]==0:
                            countk+=1
                        i+=1
                    i+=1
            res=max(res,j-i+1)  
            j+=1
        return res 
