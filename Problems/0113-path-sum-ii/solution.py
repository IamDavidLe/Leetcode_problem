# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, curSum, lis):
            nonlocal res
            if not node:
                return 
            
            lis.append(node.val)
            curSum += node.val
            if not node.left and not node.right:
                if curSum == targetSum:
                    res.append(lis[:])
            
            else:
                dfs(node.left, curSum, lis)
                dfs(node.right, curSum, lis)
            
            lis.pop()
        
        dfs(root, 0, [])
        return res