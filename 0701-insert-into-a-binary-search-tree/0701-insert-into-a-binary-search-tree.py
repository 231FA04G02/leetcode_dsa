class Solution:
    def insertIntoBST(self, root, target):
        newnode = TreeNode(target)
        
        if root is None:
            return newnode
        
        curr = root
        while True:
            if target < curr.val:
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = newnode
                    break
            else:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = newnode
                    break
        
        return root