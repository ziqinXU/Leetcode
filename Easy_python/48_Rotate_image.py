class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = []
        for i in range(int(len(matrix)/2)):
            temp = matrix[i]
            matrix[i] = matrix[len(matrix)-i-1]
            matrix[len(matrix)-i-1] = temp
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
