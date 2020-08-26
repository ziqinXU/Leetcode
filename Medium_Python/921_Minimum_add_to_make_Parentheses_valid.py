#栈的思想，LIFO
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack=[]
        for i in range(len(S)):
            if S[i]==')':
                if len(stack)>=1 and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(S[i])
            else:
                stack.append(S[i])
        return len(stack)
