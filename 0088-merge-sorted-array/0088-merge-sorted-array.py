class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        nums1 = [1,2,3,3,5,6],
                   C1  E
        m = 3, 
        nums2 = [2,5,6], 
        n = 3    C2
        """
        # [ 1, 2 , 2 , 3 , 5, 6]
        #   C1  E
        # [ 2 , 5 , 6 ]
        #C2
        end=len(nums1)-1
        cur1=m-1
        cur2=n-1
        while end>=0 and cur2>=0:
            if nums1[cur1]>nums2[cur2]:
                nums1[end]=nums1[cur1]
                cur1-=1
                end-=1
            else:
                nums1[end]=nums2[cur2]
                cur2-=1
                end-=1
        while cur2>=0:
            nums1[cur2]=nums2[cur2]
            cur2-=1
        
        
        