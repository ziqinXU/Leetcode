class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #假设有个1维数组，二分法
        if len(matrix)==0:
            return False
        left,right=0,len(matrix)*len(matrix[0])-1
        while left<=right:
            mid=left+(right-left)//2
            index1=mid//len(matrix[0])
            index2=mid%len(matrix[0])
            #print(index1,index2)
            if matrix[index1][index2]<target:
                left=mid+1
            elif matrix[index1][index2]>target:
                right=mid-1
            else:
                return True
        return False
