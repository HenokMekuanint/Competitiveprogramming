class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # [1,1,2,1,1]
        # [1,1,0,1,1]  k=3
        # [1,2,2,3,4]
        #  
        #  {
        # 0:1
        # 1:1
        # 2:2
        # 3:1
        # }                
        # [0,0,0,1,1,1,2,2,2,2]
        for i in range(len(nums)):
            nums[i]=nums[i]%2
        total=0
        counter=0
        predict=defaultdict(int)
        predict[0]=1
        for i in range(len(nums)):
            total+=nums[i]
            counter+=predict.get(total-k,0)
            predict[total]+=1
        return counter
            
                
            
