# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, sumNode):
            if not node:
                return False
            
            sumNode += node.val
            if not node.left and not node.right:
                return sumNode == targetSum
            
            return (dfs(node.left, sumNode) or dfs(node.right, sumNode))
        
        return dfs(root, 0)