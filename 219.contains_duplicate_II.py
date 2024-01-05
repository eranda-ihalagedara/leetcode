class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        if len(nums) <= 1 or k == 0:
            return False

        buffer_num = {}

        for i in range(len(nums)):
            if len(buffer_num)>k:
                buffer_num.pop(nums[i-k-1])
            
            if nums[i] in buffer_num:
                return True
            
            buffer_num[nums[i]] = i

        return False