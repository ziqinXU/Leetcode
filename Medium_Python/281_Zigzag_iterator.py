class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.nums=[]
        i=0
        while i!=len(v1) and i!=len(v2):
            self.nums.append(v1[i])
            self.nums.append(v2[i])
            i+=1
        if len(v2)>len(v1):
            while i!=len(v2):
                self.nums.append(v2[i])
                i+=1
        else:
            while i!=len(v1):
                self.nums.append(v1[i])
                i+=1
        
        self.idx=0
    def next(self) -> int:
        
        res = self.nums[self.idx]
        self.idx += 1
        return res


        

    def hasNext(self) -> bool:
        if self.idx<len(self.nums):
            return True
        else:
            return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
