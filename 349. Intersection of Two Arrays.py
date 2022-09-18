class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        array=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]==nums2[j]:
                    if nums1[i] not in array:
                        array.append(nums1[i])
        return array
                    
