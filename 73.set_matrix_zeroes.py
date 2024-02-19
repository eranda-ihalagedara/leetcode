class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zrows = set()
        zcols = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zrows.add(i)
                    zcols.add(j)
        
        for r in zrows:
            matrix[r] = [0]*n
        for c in zcols:
            for r in range(m):
                matrix[r][c]=0