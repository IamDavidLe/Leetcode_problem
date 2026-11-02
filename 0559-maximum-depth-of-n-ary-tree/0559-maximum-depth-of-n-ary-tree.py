"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        maxHeight = 0
        for child in root.children:
            maxHeight = max(maxHeight, self.maxDepth(child))
        
        return 1 + maxHeight