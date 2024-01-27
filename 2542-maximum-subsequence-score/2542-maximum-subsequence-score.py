import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        pairs = [(n1, n2) for n1 , n2 in zip(nums1, nums2)]

        pairs = sorted(pairs, key = lambda p : p[1], reverse = True)

        result = 0 
        sum_num = 0 
        min_heap = []
        heapq.heapify(min_heap)

        for num1, num2 in pairs: 
            sum_num = sum_num + num1 
            heapq.heappush(min_heap, num1)

            if len(min_heap) > k:
                top = heapq.heappop(min_heap)
                sum_num = sum_num - top 
                 

            if len(min_heap) == k: 
                if result < (sum_num * num2):
                    result = sum_num * num2 


        return result 
        

        