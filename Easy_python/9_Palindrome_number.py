class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            temparr=str(x)
            for i in range(0,int(len(temparr)/2)):
                if temparr[i]!=temparr[len(temparr)-1-i]:
                    return False
            return True
                
