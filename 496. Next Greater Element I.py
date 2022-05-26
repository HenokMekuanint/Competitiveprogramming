class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict 
        ans = []
        st = []
        nextGreatestPairs = defaultdict(int)
        
        for i in range(len(nums2)):
            if len(st) == 0:
                st.append(nums2[i])
            else:
                if nums2[i] > st[-1]:
                    while st:
                        u= st[-1]
                        if nums2[i] <= u:
                            break
                        greatest = st.pop()
                        nextGreatestPairs[greatest] = nums2[i]
                    st.append(nums2[i])
                else:
                    st.append(nums2[i])

        for i in nums1 :
            if i in nextGreatestPairs.keys():
                ans.append(nextGreatestPairs[i])
            else: 
                ans.append(-1)

        return ans
