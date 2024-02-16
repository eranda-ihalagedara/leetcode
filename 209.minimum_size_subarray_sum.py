class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n+1
        l,r,sub_sum = 0,0,0

        while r<n:
            sub_sum += nums[r]
            r += 1
            while sub_sum>=target:
                min_len = min(min_len,r-l)
                sub_sum-=nums[l]
                l+=1
                
            if min_len ==1:
                break

        if min_len>n:
            return 0
        else:
            return min_len