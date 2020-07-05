class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        A=sorted(arr)
        for i in range(len(arr)):
            current=A[i]
            for j in reversed(range(len(arr))):
                if 2*current==A[j] and j!=i:  
                    return True
        return False
