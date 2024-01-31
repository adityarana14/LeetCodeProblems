class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 

        while left <= right: 
            m = (left + right) // 2 

            if m < len(nums) - 1 and nums[m] < nums[m + 1]:
                left = m + 1 
            elif m > 0 and nums[m] < nums[m - 1]:
                right = m - 1 
            else: 
                return m 


        