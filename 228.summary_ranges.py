class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []

        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        
        rang = [nums[0], nums[0]]

        for i in range(1, len(nums)):
            if rang[1]+1 == nums[i]:
                rang[1] = nums[i]
            else:
                if rang[0] == rang[1]:
                    ranges.append(str(rang[0]))
                else:
                    ranges.append(str(rang[0])+"->"+str(rang[1]))

                rang = [nums[i], nums[i]]
        
        if rang[0] == rang[1]:
                    ranges.append(str(rang[0]))
        else:
            ranges.append(str(rang[0])+"->"+str(rang[1]))

        return ranges
	
	
	def summaryRanges2(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []

        ranges = []        
        rang = [nums[0]]

        for i in range(1, len(nums)):
            if rang[-1]+1 == nums[i]:
                rang[1:] = nums[i],
            else:
                ranges.append('->'.join(map(str,rang)))
                rang = [nums[i]]
        
        ranges.append('->'.join(map(str,rang)))

        return ranges