#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        if len(arr)<1:return 1
        left=0
        right=1
        while right<len(arr):
            if arr[left]<=arr[right]:
                left+=1
                right+=1
            else:
                return 0
        return 1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends