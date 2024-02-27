class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda r: r[0])
        non_overlap = [intervals.pop(0)]

        while intervals:
            x = non_overlap.pop()
            y = intervals.pop(0)

            if x[1] >= y[0]:
                non_overlap.append([min(x[0],y[0]), max(x[1],y[1])])
            else:
                non_overlap.append(x)
                non_overlap.append(y)            
        
        return non_overlap

    def merge_optimized(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda r: r[0])
        i = 0
        for j in range(1, len(intervals)):
            x = intervals[i]
            y = intervals[j]

            if x[1] >= y[0]:
                intervals[i] = [min(x[0],y[0]), max(x[1],y[1])]
            else:
                intervals[i+1] = [y[0], y[1]]
                i+=1            
        
        return intervals[:i+1]