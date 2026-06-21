class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def solve(root):
            if root is None:
                return 0

            left = solve(root.left)
            right = solve(root.right)

            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return solve(root) != -1
        