# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        dicti=defaultdict(list)
        def dfs(node,level):
            if not node:
                return
            
            dicti[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        if not dicti:
            return []
        ans=[]
        for i in range(max(dicti),-1,-1):
            ans.append(dicti[i])
        return ans
            
        
        