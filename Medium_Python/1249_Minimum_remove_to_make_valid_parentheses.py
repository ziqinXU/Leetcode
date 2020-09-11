class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pos=[]
        stack=[]
        s=list(s)
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(s[i])
                pos.append(i)
            if s[i]==")":
                stack.append(s[i])
                pos.append(i)
                if len(stack)>=2:
                    if stack[-1]==")" and stack[-2]=="(":
                        stack.pop()
                        stack.pop()
                        pos.pop()
                        pos.pop()
        for i in reversed(range(len(pos))):#倒序删除
            #print(pos[i])
            del s[pos[i]]
        return "".join(s)
