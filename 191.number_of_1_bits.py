class Solution:
    def hammingWeight(self, n: int) -> int:
        wt = 0

        while n>0:
            wt += n%2
            n = n//2
        
        return wt+n

	def hammingWeight_optimized(self, n: int) -> int:
        wt = 0

        while n>0:
            wt += n%2
            n = n>>1
        
        return wt+n
		
	
	def hammingWeight_optimized2(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= (n - 1)
        return count