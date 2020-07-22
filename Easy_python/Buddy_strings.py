class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        Alist=[]
        Blist=[]
        if len(A)!=len(B):
            return False
        else:
            if A==B:
                Acount=Counter(A)
                flag=0
                for i in Acount:
                    if Acount[i]>1:
                        flag=1
                        break
                if flag==1:
                    return True
                else:
                    return False
            pos=[]
            for i in range(len(A)):
                if A[i]!=B[i]:
                    pos.append(i)
            if len(pos)!=2:
                return False
            else:
                A=list(A)
                temp=A[pos[0]]
                A[pos[0]]=A[pos[1]]
                A[pos[1]]=temp
                if ''.join(A)==B:
                    return True
                else:
                    return False
                
