class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #注意全为1或0情况
        arr=[]
        i=0
        if nums[0]==1:
            arr.append(-1)
            while i<len(nums):
                j=i+1
                while j<len(nums) and nums[j]==nums[i]:
                    j+=1
                arr.append(j-i)
                i=j
        
            #print(arr)
        else:
            while i<len(nums):
                j=i+1
                while j<len(nums) and nums[j]==nums[i]:
                    j+=1
                arr.append(j-i)
                i=j
                
            #print(arr)
        if len(arr)==1:
            return 0
        if len(arr)==2 and arr[0]==-1:
            return len(nums)-1
        maxval=0
        if arr[1]>maxval:
            maxval=arr[1]

        for i in range(2,len(arr),2):
            if arr[i]==1:
                if i+1<len(arr):
                    if arr[i-1]+arr[i+1]>maxval:
                        maxval=arr[i-1]+arr[i+1]
                else:
                    if arr[i-1]>maxval:
                        maxval=arr[i-1]
            else:
                if i+1<len(arr):
                    if max(arr[i-1],arr[i+1])>maxval:
                        maxval=max(arr[i-1],arr[i+1])
                else:
                    if arr[i-1]>maxval:
                        maxval=arr[i-1]
        return maxval
