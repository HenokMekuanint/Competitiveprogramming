class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        for node1,node2 in adjacentPairs:
            graph[node1].append(node2)
            graph[node2].append(node1)
        leaves=[key for key in graph if len(graph[key])==1] 
        leaves.sort()
        def bfs():
            nonlocal leaves
            ans=[0 for i in range(len(adjacentPairs)+1)]
            queue=deque(leaves)
            visited=set(leaves)
            left,right=0,len(ans)-1
            while left<right:
                ans[left]=leaves[0]
                ans[right]=leaves[1]
                left+=1
                right-=1
                new_leaves=[]
                for leaf in leaves:
                    for new_leaf in graph[leaf]:
                        if new_leaf not in visited:
                            new_leaves.append(new_leaf)
                            visited.add(new_leaf)
                leaves=new_leaves
            if leaves:
                ans[left]=leaves[0]
            return ans
        return bfs()
            
            
            
        