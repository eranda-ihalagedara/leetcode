class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        l = len(nums)
        perms = []
        def permutations(pool, carr):
            if len(carr) == l:
                perms.append(carr)
                return
            for i in range(len(pool)):
                permutations(pool[:i]+pool[i+1:], carr + [pool[i]])

        permutations(nums, [])

        return perms

	# Inline
    def permute_optimizedI(self, nums: List[int]) -> List[List[int]]:
        
        l = len(nums)
        perms = []
        def permutations(start):
            if start >= l:
                perms.append(nums[:])
                return
            for i in range(start,l):
                nums[start], nums[i] = nums[i], nums[start]
                permutations(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        
        permutations(0)

        return perms
		
		
    def permute_optimizedII(self, nums: List[int]) -> List[List[int]]:
        
        l = len(nums)
        nums = deque(nums)
        perms = []
        def permutations(pool, perm):
            if len(perm)== l:
                perms.append(perm.copy())
                return

            for i in range(len(pool)):
                perm.append(pool.popleft())
                permutations(pool, perm)
                pool.append(perm.pop())
        
        permutations(nums,[])

        return perms