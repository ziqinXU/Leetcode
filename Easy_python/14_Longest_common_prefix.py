class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        current=strs[0]
        for i in range(len(strs)-1):
            nextword=strs[i+1]
            j=len(current)
            while j>=0:
                if nextword.find(current[:j])==0:
                    current=current[:j]
                    break
                j=j-1
        return current

                
