# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root==None:
            return []
        output=[]
        mylist=[]
        mylist.append(root)
        while mylist:
            level_sum=0
            level=len(mylist)
            for i in range(level):
                node=mylist.pop(0)
                level_sum+=node.val
                if node.left:
                    mylist.append(node.left)
                if node.right:
                    mylist.append(node.right)
            output.append(level_sum/level)
        return output
