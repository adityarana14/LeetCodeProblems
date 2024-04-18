from collections import defaultdict
import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        ans = []
        count = 0
        heapq.heapify(arr)
        for point in points: 
            x,y = point
            heapq.heappush(arr, (self.calc_distance(x,y),[x,y]))

        while count != k: 
            val = heapq.heappop(arr)
            ans.append(val[1])
            count = count + 1 
        return ans

    def calc_distance(self, x=0, y=0):  
        return math.sqrt(x**2 + y**2)