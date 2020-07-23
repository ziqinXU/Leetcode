class Solution:
    def countAndSay(self, n: int) -> str:
        sequence=['1']
        for i in range(n):
            temp=""
            j=0
            while j< len(sequence[i]):
                current=sequence[i][j]
                count=1
                k=j+1
                while k< len(sequence[i]) and sequence[i][k]==current:
                    count=count+1
                    k=k+1
                j=k
                temp=temp+str(count)+current
            sequence.append(temp)
        return sequence[n-1]
