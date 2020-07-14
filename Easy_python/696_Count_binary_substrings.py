class Solution:
#找出01和10字符串，然后向左右拓展0和1
    def countBinarySubstrings(self, s: str) -> int:
        k=0
        count=0
        while s.find('01',k)!=-1:
            index=s.find('01',k)
            count=count+1
            i=index-1
            j=index+2
            while j<len(s) and s[i]=='0' and s[j]=='1':
                count=count+1
                i=i-1
                j=j+1
            k=index+1
        k=0
        while s.find('10',k)!=-1:
            index=s.find('10',k)
            count=count+1
            i=index-1
            j=index+2
            while j<len(s) and s[i]=='1' and s[j]=='0':
                count=count+1
                i=i-1
                j=j+1
            k=index+1
        return count
