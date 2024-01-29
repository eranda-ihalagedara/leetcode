class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = [nums[0]]
        bwd = [nums[-1]]
        n = len(nums)
        for i in range(1,n):
            fwd.append(fwd[-1]*nums[i])
            bwd.append(bwd[-1]*nums[n-1-i])
        
        prd = [bwd[-2]]
        for i in range(1,n-1):
            prd.append(fwd[i-1]*bwd[n-2-i])
        prd.append(fwd[-2])
    
        return prd

    def productExceptSelf_optimized(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        prd = 1
        for i in range(n):
            res.append(prd)
            prd*=nums[i]
        
        prd = 1
        for i in range(n-1,-1,-1):
            res[i] *=prd 
            prd*=nums[i]
    
        return res