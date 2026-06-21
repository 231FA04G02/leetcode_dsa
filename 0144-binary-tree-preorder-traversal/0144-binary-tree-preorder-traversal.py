
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls=[]
        def preorder(root):
            if root==None:
                return 
            ls.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ls