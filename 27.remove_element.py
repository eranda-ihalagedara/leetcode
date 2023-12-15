class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Use 2 ids, left and right
        rid = len(nums)-1
        lid = rid

        while lid >= 0:
            if nums[rid] == val:
                rid -= 1
            elif nums[lid] == val:
                nums[lid] = nums[rid]
                rid -= 1
            lid-=1
        
        return rid+1

    def removeElement_optimized(self, nums: List[int], val: int) -> int:
        # Use 2 ids, left and right
        lid = 0

        for rid in range(len(nums)):
            if nums[rid] != val:
                nums[lid] = nums[rid]
                lid += 1
        
        return lid+1