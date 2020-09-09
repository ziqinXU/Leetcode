class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap=[]
        

    def add(self, key: int) -> None:
        self.hashmap.append(key)

    def remove(self, key: int) -> None:
        i=0
        while i< len(self.hashmap):
            if self.hashmap[i]==key:
                del self.hashmap[i]
                i=i-1
            i=i+1

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hashmap:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
