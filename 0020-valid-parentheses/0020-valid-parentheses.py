class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2==1:
            return False
        st=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                st.append(i)
            else:
                if len(st)==0:
                    return False
                top=st.pop()
                if i ==')' and top!='(':
                    return False
                if i =='}' and top!='{':
                    return False
                if i ==']' and top!='[':
                    return False
        if len(st)==0:
            return True
        else:
            return False