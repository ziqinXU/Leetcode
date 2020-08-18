class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.dictlist={}
        #print(nums)
        for i in range(len(self.nums)):
            if self.nums[i] in self.dictlist:
                self.dictlist[self.nums[i]]+=1
            else:
                self.dictlist[self.nums[i]]=1
    def showFirstUnique(self) -> int:
        #print(self.dictlist)
        flag=0
        for number in self.dictlist:
            if self.dictlist[number]==1:
                flag=1
                return number
        if flag==0:
            return -1
    def add(self, value: int) -> None:
        if value in self.dictlist:
            self.dictlist[value]+=1
        else:
            self.dictlist[value]=1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
