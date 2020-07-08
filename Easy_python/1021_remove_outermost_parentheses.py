class Solution:
    #queue，一旦闭合括号，去掉，记住0位置和对应闭合的位置，标记为1，在原string中去掉对应位置
    def removeOuterParentheses(self, S: str) -> str:
        Slist=list(S)
        pos=[0]*len(S)
        newlist=[]
        j=0
        for i in range(len(Slist)):
            newlist.append(Slist[i])
            if j==0:
                pos[i]=1
            if j<len(Slist) and j>=0 and len(newlist)>=3 and newlist[j]==')' and newlist[j-1]=='(':
                newlist.pop()
                newlist.pop()
                j=j-2
            if j<len(Slist) and j>=0 and len(newlist)==2 and newlist[j]==')' and newlist[j-1]=='(':
                pos[i]=1
                newlist.pop()
                newlist.pop()
                j=j-2
            j=j+1
        i=0
        j=0
        while i < len(Slist):
            if pos[j]==1:
                del Slist[i]
                i=i-1
            i=i+1
            j=j+1
        return "".join(Slist)

                

       
