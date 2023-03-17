# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root == None: return 0
        result = 1
        Q = [[root, 0]]
        while len(Q) > 0:
            count = len(Q)
            start = Q[0][1]
            end = Q[-1][1]
            result = max(result, end-start+1)
            for i in range(count):
                p = Q[0]
                idx = p[1] - start
                Q.pop(0)
                if (p[0].left != None): Q.append([p[0].left, 2*idx+1])
                if p[0].right != None: Q.append([p[0].right, 2*idx+2])
            
        return result