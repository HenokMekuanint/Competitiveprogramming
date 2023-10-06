class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo={}
        
        def dp(index1,index2):
            if index1>len(nums1)-1 or index2>len(nums2)-1:
                return 0
            
            if (index1,index2) in memo:
                return memo[(index1,index2)]
            
            if nums1[index1]==nums2[index2]:
                
                memo[(index1,index2)]=dp(index1+1,index2+1)+1
            else:
                 memo[(index1,index2)]=max(dp(index1+1,index2),dp(index1,index2+1))
            return memo[(index1,index2)]

            
    
        return dp(0,0)
                
        