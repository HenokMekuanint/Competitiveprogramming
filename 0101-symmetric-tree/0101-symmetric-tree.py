# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        dicti=defaultdict(list)
        def traverse(root,level):
            if root:
                traverse(root.left,level+1)
                dicti[level].append(root.val)
                traverse(root.right,level+1)
            else:
                dicti[level].append(None)
        traverse(root,0)
        dicti=dict(sorted(dicti.items(),key=lambda x:x[0]))
        temp=list(dicti.keys())
        
        for i in range(len(temp)-1):
            order=dicti[temp[i]]
            left=0
            right=len(order)-1
            while left<right:
                if order[left]==order[right]:
                    left+=1
                    right-=1
                else:
                    return False
        return True
        
                
                
        