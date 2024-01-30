class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        st = 0
        cgas, bgas = 0,0

        for ed in range(len(gas)):
            cgas = cgas + gas[ed] - cost[ed]
            if cgas < 0:
                st = ed+1
                bgas+=cgas
                cgas = 0
        
        if cgas+bgas>=0:
            return st
        else:
            return -1