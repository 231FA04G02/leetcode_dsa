class Solution(object):
    def levelOrder(self, root):

        def solve(root):
            if root==None:
                return []
            hp=deque([root])
            res=[]
            while(hp):
                level=[]
                for i in range(len(hp)):
                    node = hp.popleft()
                    level.append(node.val)
                    if node.left:
                        hp.append(node.left)
                    if node.right:
                        hp.append(node.right)
                res.append(level)
            return res
        return solve(root)