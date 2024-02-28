class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key= lambda x:x[0])

        arrow = points[0]
        num_arrows = 1

        for i in range(1,len(points)):

            if points[i][0]<=arrow[1]:
                arrow[0] = max(arrow[0], points[i][0])
                arrow[1] = min(arrow[1], points[i][1])

            else:
                arrow = points[i]
                num_arrows+=1
        
        return num_arrows

    def findMinArrowShots_optimized(self, points: List[List[int]]) -> int:

        thresh = -2**32
        num_arrows = 0

        for st,ed in sorted(points, key = lambda x: x[1]):
            if thresh < st:
                thresh = ed
                num_arrows+=1
            
        return num_arrows