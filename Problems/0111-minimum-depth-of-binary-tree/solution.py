# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = float('inf')
        def dfs(node, depth):
            nonlocal min_depth
            if not node:
                return
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
            depth += 1 
            dfs(node.left, depth)
            dfs(node.right, depth)
        
        dfs(root, 1)
        return min_depth if root else 0