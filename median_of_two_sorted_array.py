def findMedianSortedArrays(self, nums1, nums2):

    for i in range(len(nums2)):
        nums1.append(nums2[i])
    
        #sort the current array
    nums1.sort()
        
        #if even, take left/right of the middle and return sum / 2
    if len(nums1) % 2 == 0:
        left = nums1[(len(nums1)/2)-1]
        right = nums1[(len(nums1)/2)]           
        return(float((left + right))/2)            
        #if odd, return middle
    else:
        return(nums1[len(nums1)/2])        
nums1 = [1,3] 
nums2 = [2]
print(findMedianSortedArrays(nums1,nums2))
