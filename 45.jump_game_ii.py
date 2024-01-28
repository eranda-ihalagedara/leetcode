import heapq
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=2:
            return max(0,n-1)

        distance = [n+1]*n
        explored = [0]*n
        next_nodes = []

        heapq.heappush(next_nodes, (0,0))

        while next_nodes:
            hops, cid = heapq.heappop(next_nodes)
            if explored[cid] or nums[cid]==0:
                continue

            for j in range(nums[cid]+cid,cid,-1):
                if j >=n-1:
                    return hops+1
                if explored[j]:
                    continue
                distance[j] = min(distance[j], hops+1)
                heapq.heappush(next_nodes, (hops+1,j))
            
            explored[cid] = 1

        return distance[-1]


    def jump_optimized(self, nums: List[int]) -> int:
        
        n = len(nums)
        hops, max_jump, cpos = 0, 0, 0

        for i in range(n-1):
            max_jump = max(max_jump, i+nums[i])

            if i == cpos:
                hops+=1
                cpos = max_jump

        return hops