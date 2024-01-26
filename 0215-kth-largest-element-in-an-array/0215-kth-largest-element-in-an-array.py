import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # answer = heapq.nlargest(k,nums)
        
        # return answer[-1]
        heapq.heapify(nums)

        # remove the topmost item from the heap
        # until k reached.
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
