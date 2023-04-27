class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans=[0 for i in range(len(nums))]
        for i in range(len(nums)):
            nums[i]=(nums[i],i)
        def merge_sort(arr,left,right):
            if left==right:
                return [arr[left]]
            mid=(right+left)//2
            left_half=merge_sort(arr,left,mid)
            right_half=merge_sort(arr,mid+1,right)
            return merge(left_half,right_half)
        def merge(left_part,right_part):
            temp=[]
            curpos,right=len(right_part)-1,len(right_part)-1
            for left in range(len(left_part)-1,-1,-1):
                while right>-1 and right_part[right][0]>=left_part[left][0]:
                    right-=1
                ans[left_part[left][1]]+=(right+1)
                cur_pos=right
            ptr1=0
            ptr2=0
            while ptr1<len(left_part) and ptr2<len(right_part):
                if left_part[ptr1][0]>right_part[ptr2][0]:
                    temp.append(right_part[ptr2])
                    ptr2+=1
                else:
                    temp.append(left_part[ptr1])
                    ptr1+=1
            temp.extend(left_part[ptr1:])
            temp.extend(right_part[ptr2:])
            return temp
        merge_sort(nums,0,len(nums)-1)
        return ans
                    
            
        