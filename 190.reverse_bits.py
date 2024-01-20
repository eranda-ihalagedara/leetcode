class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        exp = 31

        while n > 0:
            if n%2 == 1:
                ans+= 2**exp
            n = n//2
            exp-=1
        
        return ans
