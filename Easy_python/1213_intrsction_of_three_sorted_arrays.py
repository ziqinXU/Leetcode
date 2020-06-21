class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        A=Counter(arr1)#用Counter计算dict
        B=A&Counter(arr2)
        C=B&Counter(arr3)
        return C.elements()
