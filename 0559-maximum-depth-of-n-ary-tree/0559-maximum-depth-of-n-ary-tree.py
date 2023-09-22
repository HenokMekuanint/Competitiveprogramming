"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def dfs(node,depth):
            cur_depth=0
            if not node.children:
            
                return depth
            
            for children in node.children:

                cur_depth=max(dfs(children,depth+1),cur_depth)
                
            return cur_depth
        
        return dfs(root,1)
            
        