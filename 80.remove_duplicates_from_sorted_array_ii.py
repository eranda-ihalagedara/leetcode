class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lid = 0

        for n in nums:
            if lid < 2 or n > nums[lid-2]:
                nums[lid] = n
                lid+=1

        return lid
	
    def removeDuplicates_optimized(self, nums: List[int]) -> int:
        lid = 2

        for rid in range(2, len(nums)):
            if nums[rid] != nums[lid-2]:
                nums[lid] = nums[rid]
                lid+=1

        return lid