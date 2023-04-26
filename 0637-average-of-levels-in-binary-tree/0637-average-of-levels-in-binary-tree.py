# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans=[]
        dicti=defaultdict(list)
        def traverse(node,level):
            if not node:
                return
            dicti[level].append(node.val)
            traverse(node.left,level+1)
            traverse(node.right,level+1)
        traverse(root,0)
        for key in dicti:
            ans.append(sum(dicti[key])/len(dicti[key]))
        return ans
        
            
        
            
        