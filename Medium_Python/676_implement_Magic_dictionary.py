class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """


    def buildDict(self, dictionary: List[str]) -> None:
        self.dictionary=dictionary


    def search(self, searchWord: str) -> bool:
        
        for idx,word in enumerate(self.dictionary):
            if len(searchWord)==len(word):
                if searchWord!=word:  
                    count=0
                    for idx,_ in enumerate(searchWord):
                        if searchWord[idx]!=word[idx]:
                            count=count+1
                            #print(word[idx])
                    if count==1:
                        return True
                    
            
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
