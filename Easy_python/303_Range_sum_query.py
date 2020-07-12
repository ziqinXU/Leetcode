class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.arrsum=[0]
        for i in range(len(nums)):
            self.arrsum.append(sum(nums[:i+1]))
        

    def sumRange(self, i: int, j: int) -> int:
        return self.arrsum[j+1]-self.arrsum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
