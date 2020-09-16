class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #滑动窗口，双指针，hashmap，左指针滑动至hashmap里右指针所指的值被排出
        #注意当所有值均无重复的特殊情况
        left,right=0,0
        sMap={}
        maxlen=0
        
        while right<len(s):
            if s[right] not in sMap or sMap[s[right]]==0:
                sMap[s[right]]=1
            elif sMap[s[right]]==1:
                #print(left,right)
                while (sMap[s[right]]==1):
                    sMap[s[left]]-=1
                    left=left+1
                #print(left,right)
                sMap[s[right]]=1
            #print(left,right)
            #print(sMap)
            if right-left+1>maxlen:
                    maxlen=right-left+1
            right+=1
        
        return maxlen
