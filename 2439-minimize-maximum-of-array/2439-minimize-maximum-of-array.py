class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        low=min(nums)
        high=max(nums)
        
        def check(mid):
            cur = 0
            for index in range(len(nums)-1, -1, -1):
                cur = max(0, cur + nums[index] - mid)
            return cur == 0
        
                  
        while low < high:
            mid = (low + high)>>1
            if check(mid):
                high = mid 
            else:
                low = mid + 1
        return high
    
            
            
        