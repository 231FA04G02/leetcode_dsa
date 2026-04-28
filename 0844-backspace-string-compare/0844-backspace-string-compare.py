class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)

        if n==0 and m==0:
            return True


        s1=[]
        t1=[]
        for i in list(s):
            if i!='#':
                s1.append(i)
            elif len(s1)>0:
                s1.pop()


        for i in list(t):
            if i!='#':
                t1.append(i)
            elif len(t1)>0:
                t1.pop()
        return t1==s1


       
        