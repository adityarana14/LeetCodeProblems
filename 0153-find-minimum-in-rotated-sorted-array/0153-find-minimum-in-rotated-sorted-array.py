class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1  
        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right: 
            size = right - left + 1
            mid = (left + right ) // 2

            if left == right: 
                return nums[left]

            if nums[mid] > nums[mid-1] and nums[mid]>nums[mid+1] and size >=3:
                return nums[mid+1] 

            if size == 2: 
                if nums[left] > nums[right]:
                    return nums[right]
                else: 
                    return nums[left]
            
            if nums[left] <= nums[mid]:
                left = mid + 1 
            else: 
                right = mid 

        return nums[0]
        