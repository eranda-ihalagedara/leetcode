class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Starting point for each layer: 0,0 1,1 2,2

        n = len(matrix)

        for i in range(n//2):

            for j in range(i, n-1-i):
                d = j-i
                v0 = matrix[i][j]
                matrix[i][j] = matrix[n-1-i-d][i]
                matrix[n-1-i-d][i] = matrix[n-1-i][n-1-i-d]
                matrix[n-1-i][n-1-i-d] = matrix[i+d][n-1-i]
                matrix[i+d][n-1-i] = v0

    def rotate_II(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # Upside down
        for k in range(n//2):
            matrix[k], matrix[n-1-k] = matrix[n-1-k], matrix[k] 

        # Transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate_optimized_I(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Starting point for each layer: 0,0 1,1 2,2
		# [n-1-j] or [n-1-i] can be written as [~j] or [~i]

        n = len(matrix)

        for i in range(n//2):
            for j in range(i, n-1-i):
                matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] = matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]
