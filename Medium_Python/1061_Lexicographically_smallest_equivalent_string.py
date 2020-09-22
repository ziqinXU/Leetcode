class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        parent=[-1]*26
        rank=[0]*26
        #小的字母为parent
        def find(x,parent):
            x_root=x
            while(parent[x_root]!=-1):
                x_root=parent[x_root]
            return x_root
        def union(x,y,parent,rank):
            x_root=find(x,parent)
            y_root=find(y,parent)
            if x_root==y_root:
                return 0
            else:
                #print(x,y,x_root,y_root)
                if x_root>y_root:
                    parent[x_root]=y_root
                elif x_root<y_root:
                    parent[y_root]=x_root
                
                return 1
        for i in range(len(A)):
            result=union(ord(A[i])-97,ord(B[i])-97,parent,rank)
        returnstring=""
        for i in range(len(S)):
            word=S[i]
            while(parent[ord(word)-97]!=-1):
                word=chr(parent[ord(word)-97]+97)
            returnstring+=word
        return returnstring
