class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S=list(S)
        current=[]
        pos=[]
        for i in range(len(S)):
            if (S[i]>="a" and S[i]<="z") or (S[i]>="A" and S[i]<="Z"):
                current.append(S[i])
                pos.append(i)
        current=current[::-1]
        for i in range(len(pos)):
            S[pos[i]]=current[i]
        return "".join(S)

