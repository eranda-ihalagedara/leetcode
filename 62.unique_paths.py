import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m+n-2)//math.factorial(m-1)//math.factorial(n-1)
		
    def uniquePaths_II(self, m: int, n: int) -> int:

        if m<n:
            n,m = m,n
        path = 1
        for i in range(1,n):
            path  = path*(m-1+i)/i
        
        return int(path)

    def uniquePaths_dynamic(self, m: int, n: int) -> int:
        paths = [[1]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[-1][-1]