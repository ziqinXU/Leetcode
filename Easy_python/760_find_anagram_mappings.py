class Solution:
    #hashmap
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        hashmap={}
        returnarray=[]
        for idx,number in enumerate(B):
            hashmap[number]=idx
        for idx,number in enumerate(A):
            returnarray.append(hashmap[A[idx]])
        return returnarray
