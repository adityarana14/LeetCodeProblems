from collections import deque 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0 
        storage_area = deque()

        for idx, val in enumerate(heights):
            if not storage_area: 
                storage_area.append([val, idx])
            else: 
                if storage_area[-1][0] <= val: 
                    storage_area.append([val,idx])
                else: 
                    temp_count = 0 
                    while storage_area and storage_area[-1][0] > val:
                        ans = max(storage_area[-1][0], (idx - storage_area[-1][1])*storage_area[-1][0], ans)
                        temp_count = storage_area[-1][1]
                        storage_area.pop()
                    storage_area.append([val,temp_count])

        idx = len(heights) 
        while storage_area and storage_area[-1][0] > float("-inf"):
            ans = max(storage_area[-1][0], (idx - storage_area[-1][1])*storage_area[-1][0], ans)
            storage_area.pop()

        return ans   
        