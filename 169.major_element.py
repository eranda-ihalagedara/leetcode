class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major_element = None
        major_count = 0
        element_count = {}
        n = len(nums)
        for i in range(n):
            count = element_count.get(nums[i],0)+1
            element_count[nums[i]] = count
            if count> major_count:
                major_count = count
                major_element = nums[i]
            
            if count>n/2:
                break
        
        return major_element
	
	
	# Moor voting majority algorithm
	def majorityElement_optimized(self, nums: List[int]) -> int:
        major_element = None
        major_count = 0

        for num in nums:
            if major_count==0:
				major_element = num
			
			if major_element == num:
				major_count += 1
			else:
				major_count -= 1
				
			
        
        return major_element