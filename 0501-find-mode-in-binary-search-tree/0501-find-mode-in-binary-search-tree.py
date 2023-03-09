# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dicti=defaultdict(int)
        ans=[]
        def traverse(root):
            if root:
                traverse(root.left)
                if root.val!=None:
                    dicti[root.val]+=1
                traverse(root.right)
        traverse(root)
        comp=max(dicti.values())
        for num in dicti:
            if dicti[num]==comp:
                ans.append(num)
        return ans
            
        