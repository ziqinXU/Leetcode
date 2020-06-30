class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            A=list(str(x))
            A=reversed(A)
            number=int("".join(A)) 
            if number>=-pow(2,31) and number<=pow(2,31)-1:
                return number
            else:
                return 0 
        else:
            A=list(str(x)[1:])
            A=reversed(A)
            number=int("-"+"".join(A))
            if number>=-pow(2,31) and number<=pow(2,31)-1:
                return number
            else:
                return 0

        
