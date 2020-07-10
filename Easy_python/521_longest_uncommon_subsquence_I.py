class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        #两个串相等返回-1，如果长度不同，返回长串
        if len(a)!=len(b) or a!=b:
            return max(len(a),len(b))
        else:
                return -1
