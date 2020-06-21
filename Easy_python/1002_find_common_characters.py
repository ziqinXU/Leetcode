class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        #use Counter to check dict and list(temp1.elements()) convert dict into list
        temp1 = Counter(A[0])
        for i in range(1,len(A)):
            ans=Counter(A[i])&temp1
            temp1=ans
        return list(temp1.elements())
