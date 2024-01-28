class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return True
        n = len(nums)
        maxj = 0
        for i in range(n-1):
            if nums[i] == 0 and maxj == 0:
                return False
            if nums[i]>maxj:
                maxj = nums[i]
            maxj-=1
            
        return True
		
	
	def canJump_optimized(self, nums: List[int]) -> bool:

        pos = len(nums)-1
        for i in range(pos,-1,-1):
            if i+nums[i] >= pos:
                pos = i
            
        return not pos