class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        rst = [intervals[0]]
        for i in range(1, len(intervals)):
            u, v = intervals[i]
            if u <= rst[-1][1]:
                rst[-1][1] = max(rst[-1][1] , v)
            else:
                rst.append([u,v])
        return rst