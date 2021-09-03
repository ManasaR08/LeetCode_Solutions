# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def recurse(l, r):
            if l>r:
                return [None]
            trees = []
            for i in range(l, r+1):
                lefts = recurse(l, i-1)
                rights = recurse(i+1, r)
                for left in lefts:
                    for right in rights:
                        tree = TreeNode(i)
                        tree.left = left
                        tree.right = right
                        trees.append(tree)
            return trees
        return recurse(1,n)
        