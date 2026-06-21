from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def solve(root):
            if root==None:
                return []
            res=[]
            hp=deque([root])

            while(hp):
                level=[]
                for i in range(len(hp)):
                    node=hp.popleft()
                    level.append(node.val)
                    
                    if node.left:
                        hp.append(node.left)
                    if node.right:
                        hp.append(node.right)
                
                res.append(level)
            
            return res
        return solve(root)
    