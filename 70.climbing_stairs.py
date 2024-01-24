import math
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0

        count = 0

        for ones in range(n,-1,-2):
            twos = (n-ones)//2
            count+= math.factorial(ones+twos)//math.factorial(ones)//math.factorial(twos)

        return count

    def climbStairs_optimized(self, n: int) -> int:

        if n<=2:
            return max(0,n)

        n1, n2 = 1,2

        for i in range(2,n):
            n1, n2 = n2, n1+n2

        return n2