class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        ans=[nums1[i]-nums2[i] for i in range(len(nums1))]
        count=[0]
        def merge_sort(arr,left,right):
            if left==right:
                return [arr[left]]
            mid=left+(right-left)//2
            left_part=merge_sort(arr,left,mid)
            right_part=merge_sort(arr,mid+1,right)
            merged=merge(left_part,right_part)
            return merged
          
        dif=[diff]  
        def merge(left_part,right_part)->list:
            ptr1=0
            ptr2=0
            temp=[]
            right=0
            for left in range(0,len(left_part)):
                while right<len(right_part) and left_part[left]>right_part[right]+dif[0]:
                    right+=1
                count[0]+=(len(right_part)-right)
                
            while ptr1<len(left_part) and ptr2<len(right_part):
                if left_part[ptr1]<right_part[ptr2]:
                    temp.append(left_part[ptr1])
                    ptr1+=1
                else:
                    temp.append(right_part[ptr2])
                    ptr2+=1
            temp.extend(left_part[ptr1:])
            temp.extend(right_part[ptr2:])
            return temp
        merge_sort(ans,0,len(ans)-1)
        return count[0]
            
#         [1,0,4]


        