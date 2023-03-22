class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(left,right,arr):
            if left==right:
                return [arr[left]]
            mid=left+(right-left)//2
            left_half=mergeSort(left,mid,arr)
            right_half=mergeSort(mid+1,right,arr)
            return merge(left_half,right_half)
        def merge(left_half,right_half):
            ans=[]
            left=0
            right=0

            while left<len(left_half) and right<len(right_half):
                if left_half[left]>right_half[right]:
                    ans.append(right_half[right])
                    right+=1
                else:
                    ans.append(left_half[left])
                    left+=1
            ans.extend(left_half[left:])
            ans.extend(right_half[right:])
            return ans
        return mergeSort(0,len(nums)-1,nums)