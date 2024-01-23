class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        n0, n1 = 0,1

        for i in range(1,n):
            n0, n1 = n1, n0+n1
        
        return n1
