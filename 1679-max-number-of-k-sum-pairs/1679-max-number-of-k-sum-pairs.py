class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        i = 0 
        j = len(nums) - 1
        count = 0 
        while i < j:
            if sorted_nums[i] + sorted_nums[j] == k:
                count = count + 1 
                i = i + 1 
                j = j - 1 
            elif sorted_nums[i] + sorted_nums[j] < k:
                i = i + 1
            else: 
                j = j - 1  

        return count 
        
        