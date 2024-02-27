class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i=0
        while i<n and newInterval[1] >= intervals[i][0]:
            i+=1

        if i == n:
            i+=1

        merged_intervals = intervals[:i] + [newInterval]
        
        for j in range(len(merged_intervals)-1,0,-1):
            if merged_intervals[j][0] <=merged_intervals[j-1][1]:
                merged_intervals[j-1][0] = min(merged_intervals[j-1][0], merged_intervals[j][0])
                merged_intervals[j-1][1] = max(merged_intervals[j-1][1], merged_intervals[j][1])
                merged_intervals.pop()
            else:
                break

        return merged_intervals + intervals[i:]
		

    def insert_optimized_I(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i=0
        while i < n and intervals[i][1] < newInterval[0] :
            i+=1
        
        merged_intervals = intervals[:i]

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1

        return merged_intervals + [newInterval] + intervals[i:]