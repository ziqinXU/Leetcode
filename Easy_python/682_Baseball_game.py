class Solution:
    def calPoints(self, ops: List[str]) -> int:
        currentlist=[]
        for i in range(len(ops)):
            if ops[i]=='+':
                currentlist.append(currentlist[-1]+currentlist[-2])
            elif ops[i]=='C':
                currentlist.pop()
            elif ops[i]=='D':
                currentlist.append(currentlist[-1]*2)
            else:
                currentlist.append(int(ops[i]))
                
        return sum(currentlist)
