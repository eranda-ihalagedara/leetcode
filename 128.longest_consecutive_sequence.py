class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        lnums = len(nums)

        maxsq = 0

        for n in nums:
            if n-1 not in nums:
                ni = n+1
                while ni in nums:
                    ni+=1
                maxsq = max(maxsq, ni-n)
                if maxsq == lnums:
                    return maxsq

        return maxsq