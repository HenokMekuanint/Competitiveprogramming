class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dect=defaultdict(int)
        for num in nums:
            dect[num]+=1
        counter=0
        for i in range(len(nums)):
            if dect[nums[i]]>0 and dect[k-nums[i]]>0:
                if nums[i]==k-nums[i] and dect[nums[i]]<=1:
                    continue
                else:
                    counter+=1
                    dect[nums[i]]-=1
                    dect[k-nums[i]]-=1
        return counter
                
        
            
        