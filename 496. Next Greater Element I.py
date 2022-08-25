class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        array=[-1 for i in range(len(nums1))]
        for i in range(len(nums2)):
            if nums2[i] not in nums1:
                continue
            else:
                for j in range(i+1,len(nums2)):
                    nextgreater=nums2[j]
                    if array[nums1.index(nums2[i])]==-1 and nums2[i]<nextgreater:
                        array[nums1.index(nums2[i])]=nextgreater
                        break
        return array
    
    
    class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        res=[-1 for i in range(len(nums1))]
        for i in range(len(nums2)):
            cur=nums2[i]

            while stack and cur>stack[-1]:
                val=stack.pop()
                res[nums1.index(val)]=cur
            if cur in nums1:
                stack.append(cur)
        return res

