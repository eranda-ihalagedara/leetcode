class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        n = len(nums)
        complement = {nums[0]:0}
        for i in range(1,n-1):
            for j in range(i+1,n):
                remain =  -(nums[i]+nums[j])
                if remain in complement:
                    triplets.append(tuple(sorted([nums[i], nums[j], remain])))
            
            complement[nums[i]] = i
        return set(triplets)

    def threeSum_optimized_I(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        n, z, p = [], [], []

        for num in nums:
            if num>0:
                p.append(num)
            elif num<0:
                n.append(num)
            else:
                z.append(num)
        N = set(n)
        P = set(p)

        if z:
            for num in P:
                if -num in N:
                    triplets.add((-num,0,num))
        if len(z)>=3:
            triplets.add((0,0,0))
        
        for i in range(0,len(n)-1):
            for j in range(i+1,len(n)):
                remain = -(n[i]+n[j])
                if remain in P:
                    triplets.add(tuple(sorted([n[i], n[j], remain])))

        for i in range(0,len(p)-1):
            for j in range(i+1,len(p)):
                remain = -(p[i]+p[j])
                if remain in N:
                    triplets.add(tuple(sorted([remain, p[i], p[j]])))
        
        return triplets
	
	
    def threeSum_optimized_II(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    triplets.add((nums[i], nums[l], nums[r]))
					l += 1
					r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return triplets