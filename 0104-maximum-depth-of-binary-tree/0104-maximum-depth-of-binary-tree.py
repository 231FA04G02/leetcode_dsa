# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root==None:
                return 0
            leftheight=solve(root.left)
            rightheight=solve(root.right)
            return (max(leftheight,rightheight)+1)
        return solve(root)
        