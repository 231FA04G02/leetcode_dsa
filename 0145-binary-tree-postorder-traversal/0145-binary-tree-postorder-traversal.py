class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls=[]
        def postorder(root):
            if root==None:
                return 
            else:
                postorder(root.left)
                postorder(root.right)
                ls.append(root.val)
        postorder(root)
        return ls
        