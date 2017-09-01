class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        n = len(points)
        starts = [ ]
        ends = [ ]
        for i in range(n):
            starts.append(points[i][0])
            ends.append(points[i][1])
            
        starts.sort()
        ends.sort()
        print starts
        print ends
        start = 0
        arrows = 0
        for i in range(n):
            if starts[i] < ends[end]:
                arrows += 1
            else:
                end += 1

           

        
        return arrows
    
print Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])
print Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])


'''
public int findMinArrowShots(int[][] points) {
        if (points.length == 0) {
            return 0;
        }
        Arrays.sort(points, (a, b) -> a[1] - b[1]);
        int arrowPos = points[0][1];
        int arrowCnt = 1;
        for (int i = 1; i < points.length; i++) {
            if (arrowPos >= points[i][0]) {
                continue;
            }
            arrowCnt++;
            arrowPos = points[i][1];
        }
        return arrowCnt;
    }
'''