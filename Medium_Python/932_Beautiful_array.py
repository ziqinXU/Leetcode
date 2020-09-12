class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        #递归将index为偶数至左边，奇数放右边，重复至只剩2个元素
        left=0
        right=N-1
        nums=[x for x in range(1,N+1)]
        
        def recursion(nums):
            if len(nums)<=2:
                return nums
            n1=recursion(nums[0::2])
            #print(n1)
            n2=recursion(nums[1::2])
            #print(n2)
            #print(n1+n2)
            return n1+n2
        return recursion(nums)
        
