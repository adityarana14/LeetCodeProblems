class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            val = abs(val)
            if nums[val] < 0:
                return val
            else: 
                val = (val)
                nums[val] = -1 * nums[val]
        
        return nums[0]