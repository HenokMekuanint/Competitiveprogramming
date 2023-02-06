class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [ 1, 2 ]
          L R
            
        """
     
        k=k%len(nums)
        nums.reverse()
        nums[:k]= reversed( nums[:k])
        nums[k:]= reversed( nums[k:])