class Solution:
    def countLetters(self, S: str) -> int:
        left=0
        right=0
        countsum=0
        while right!=len(S):
            if S[left]==S[right]:
                right=right+1
            else:
                countsum=countsum+int((1+right-left)*(right-left)/2)
                left=right
                right=left
        countsum=countsum+int((1+right-left)*(right-left)/2) 
        return countsum
