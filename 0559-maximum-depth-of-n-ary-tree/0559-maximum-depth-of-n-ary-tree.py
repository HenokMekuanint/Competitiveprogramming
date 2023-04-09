"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:        
        visited=set()
        ans=[0]
        def dfs(vertex,depth):
            if not vertex:
                return
            visited.add(vertex.val)
            ans[0]=max(ans[0],depth)
            for child in vertex.children:
                dfs(child,depth+1)
        dfs(root,1)
        return ans[0]
        