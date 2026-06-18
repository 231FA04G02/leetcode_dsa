class Solution(object):
    def levelOrder(self, root):
        def solve(root):
            if root==None:
                return []
            hp=deque([root])
            res=[]
            while(hp):
                level=[]
                for i in range (len(hp)):
                    Node=hp.popleft()
                    level.append(Node.val)

                    if Node.left:
                        hp.append(Node.left)
                    if Node.right:
                        hp.append(Node.right)

                res.append(level)
            return res
        return solve(root) 
            