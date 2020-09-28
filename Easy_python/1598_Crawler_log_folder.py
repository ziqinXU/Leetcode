class Solution:
    def minOperations(self, logs: List[str]) -> int:
        start=0
        for i in range(len(logs)):
            if len(logs[i])==2:
                if logs[i][0]=='.':
                    start=start
                else:
                    start+=1
            else:
                
                if logs[i][0]=='.' and start>=1:
                    
                    start-=1
                elif logs[i][0]=='.' and start==0:
                    
                    start=start
                else:
                    start+=1
        return start
