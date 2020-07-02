class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=[]
        stack.append(S[0])
        k=0
        for i in range(1,len(S)):
            stack.append(S[i])
            k=k+1
            #print (k)
            if k>=1 and stack[k]==stack[k-1]:
                stack.pop()
                stack.pop()
                k=k-2
        return "".join(stack)

            
