class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # merger the interval and count
        if len(points) == 0 : return 0
        points.sort()
        rst = [ points[0]  ]
        
        for i, p in enumerate(points):
            u,v = p
            if i == 0: continue
            if rst[-1][1] >= u: rst[-1][0], rst[-1][1]= max( rst[-1][0], u), min(rst[-1][1], v)
            else: rst.append( [u,v] )
        
        
        return len(rst)