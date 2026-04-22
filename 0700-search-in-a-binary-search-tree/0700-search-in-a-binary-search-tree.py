class Solution:
    def searchBST(self, root, target):
        if root is None:
            return None
        curr=root
        while curr!=None:
            if curr.val==target:
                return curr
            elif curr.val >target:
                curr=curr.left
            else:
                curr=curr.right
            
        return None

        