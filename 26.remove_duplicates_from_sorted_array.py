class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lid = 0

        for rid in range(1,len(nums)):
            if nums[lid] != nums[rid]:
                lid+=1
                nums[lid] = nums[rid]

        return lid+1