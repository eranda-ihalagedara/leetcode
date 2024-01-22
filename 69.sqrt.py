class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x==0 or x==1:
            return x
            
        low, high = 0,x

        while low<high:
            mid = (low+high)//2
            if mid**2 == x or mid==low:
                return mid
            elif mid**2 > x:
                high = mid
            else:
                low = mid
        
        return low
		
		
	def mySqrt_optimized(self, x: int) -> int:
        
        root = x

        while root**2 > x:
            root = (root + x//root)//2
        
        return root