class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.diction=[]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        found=0
        for m in self.diction:
            if m[0]==key:
                found=1
                m[1]=value
        if found==0:
            self.diction.append([key,value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for m in self.diction:
            if m[0]==key:
                return m[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx=0
        while idx<len(self.diction):
            #print(self.diction,idx)
            if self.diction[idx][0]==key:
                del self.diction[idx]
                break
            idx+=1
                
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
