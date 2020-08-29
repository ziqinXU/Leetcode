class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(S,left,right):
            if len(S)==2*n:
                #当找到一串时，输出
                res.append(S)
            if left<n:
                #若左括号小于一半长度，则可继续添加
                S=S+'('
                backtrack(S,left+1,right)
                S=S[:-1]
            if right<left:
                #若右括号小于左括号，可添加
                S=S+')'
                backtrack(S,left,right+1)
                S=S[:-1]


        backtrack("",0,0)
        return res 
