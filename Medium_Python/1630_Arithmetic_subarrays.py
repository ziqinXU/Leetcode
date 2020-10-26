class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res=[]
        for i in range(len(l)):
            left,right=l[i],r[i]
            tempnum=nums[left:right+1]
            tempnum=sorted(tempnum)
            diff=tempnum[1]-tempnum[0]
            flag=0
            for j in range(2,len(tempnum)):
                if tempnum[j]-tempnum[j-1]!=diff:
                    flag=1
                    break
            if flag==1:
                res.append(False)
            else:
                res.append(True)     
        return res           
