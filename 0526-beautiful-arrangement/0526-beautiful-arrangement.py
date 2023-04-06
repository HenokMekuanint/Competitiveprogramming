class Solution:
    def countArrangement(self, n: int) -> int:
        ans=[]
        nums=[i for i in range(1,n+1)]
        def bfs(arr,visited):
            if len(arr)==len(nums):
                ans.append(arr)
                return 
            else:
                for i in range(len(nums)):
                    if nums[i] not in visited:
                        if nums[i]%(len(arr)+1)==0 or (len(arr)+1)%nums[i]==0: 
                            arr.append(nums[i])
                            visited.add(nums[i])
                            bfs(arr[::],visited)
                            arr.pop()
                            visited.remove(nums[i])
        bfs([],set())
        return len(ans)