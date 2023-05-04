# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ad_list=defaultdict(list)
        ans=[]
        def traverse(node):
            if node and not node.left and not node.right:
                return
            if node and node.left:
                ad_list[node.val].append(node.left.val)
                ad_list[node.left.val].append(node.val)
            if node and node.right:
                ad_list[node.val].append(node.right.val)
                ad_list[node.right.val].append(node.val)
            if node and node.left:traverse(node.left)
            if node and node.right:traverse(node.right)
        traverse(root)
        def bfs(target,k):
            queue=deque([(0,target)])
            visited=set([target])
            while queue:
                distance,node=queue.popleft()
                if distance==k:
                    ans.append(node)
                for neighbour in ad_list[node]:
                    
                    if neighbour not in visited:
                        queue.append((distance+1,neighbour))
                        visited.add(node)
        bfs(target.val,k)
        return ans
                    
                
                
        
        
        