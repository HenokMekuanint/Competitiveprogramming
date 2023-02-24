class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans=[-1 for i in range(len(nums1))]
        dicti={value:index for index,value in enumerate(nums1)}
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                popped=stack.pop()
                ans[dicti[popped]]=nums2[i]
            if nums2[i] in nums1:
                stack.append(nums2[i])
        return ans
        