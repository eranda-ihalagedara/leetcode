class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        lnums = []
        for i in range(len(nums)-1,k-1,-1):
            lnums.append(nums[i])
            nums[i] = nums[i-k]

        for i in range(k-1,-1,-1):
            lnums.append(nums[i])
            nums[i] = lnums.pop(0)    
	
	def rotate_optimized(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        
        nums[k:], nums[:k]  = nums[:-k], nums[-k:]

# For O(1) space and O(n) time
# Reverse 0 : n-k-1 and  n-k : n-1 parts and reverse the whole array
    def reverse (self, nums, i, j) : 
        li = i
        ri = j
        
        while li < ri:
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp
            
            li += 1
            ri -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k < 0 : 
            k += len(nums)
        
        self.reverse(nums, 0, len(nums) - k - 1);
        self.reverse(nums, len(nums) - k, len(nums) - 1);
        self.reverse(nums, 0, len(nums) - 1);