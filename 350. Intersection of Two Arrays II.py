class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                array.append(nums1[i])
                nums2.remove(nums1[i])
        return array
