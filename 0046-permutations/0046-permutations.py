class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def bfs(arr,visited):
            if len(arr)==len(nums):
                ans.append(arr)
                return 
            else:
                for i in range(len(nums)):
                    if nums[i] not in visited:
                        arr.append(nums[i])
                        visited.add(nums[i])
                        bfs(arr[::],visited)
                        arr.pop()
                        visited.remove(nums[i])
        bfs([],set())
        return ans
                
            
        