class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j=0
        for i in range(len(nums1)-1,len(nums1)-n-1,-1):
            nums1[i]=nums2[j]
            j+=1
        return nums1.sort()
        