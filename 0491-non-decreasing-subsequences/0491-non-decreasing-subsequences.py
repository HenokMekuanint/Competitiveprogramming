class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def back_track(arr,index):
            if len(arr)>1 and (arr==sorted(arr)) and (arr not in ans):
                ans.append(arr)
            if index==len(nums):
                return
            else:
                for i in range(index,len(nums)):
        
                    back_track(arr+[nums[i]],i+1)
               
        back_track([],0)
        return ans
                        
        