class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums=nums
        self.index=set()
        for i in range(len(self.nums)):
            if self.nums[i]!=0:
                self.index.add(i)
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        c=set.intersection(self.index,vec.index)
        arrsum=0
        for i in c:
            arrsum+=vec.nums[i]*self.nums[i]
        return arrsum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
