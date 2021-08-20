# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        def dfs_sum(node):
            if not node:
                return 0
            else:
                return node.val + dfs_sum(node.left) + dfs_sum(node.right)
        total_sum = dfs_sum(root)
            
        self.output = 0
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.output = max(self.output, (total_sum-l)*l, (total_sum-r)*r)
            return node.val+l+r
        dfs(root)
        return self.output % (10**9+7)
        