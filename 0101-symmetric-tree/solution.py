# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        branch1 = branch2 = root
        def dfs(b1, b2):
            if not b1 and not b2:
                return True
            
            if (not b1 and b2) or (not b2 and b1):
                return False
            
            if b1.val != b2.val:
                return False
            
            return dfs(b1.left, b2.right) and dfs(b1.right, b2.left)
        
        return dfs(branch1, branch2)