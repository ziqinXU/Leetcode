class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        A=sorted(nums,reverse=True)
        i=0
        number=0
        while i< len(nums):
            current=A[i]  
            number=number+1
            while i< len(nums)-1 and A[i+1]==current:
                i=i+1
            i=i+1
            if number==3:
                return current
        return A[0]
        
