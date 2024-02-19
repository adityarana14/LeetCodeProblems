class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1


        while left <= right: 
            size = right - left + 1 

            if size == 2: 
                if nums[left] == target: 
                    return left
                elif nums[right] == target: 
                    return right 
                else: return -1 

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if left == right: 
                return -1 

            # Check which side is the sorted array 

            if nums[left] < nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid 
                else:
                    left = mid + 1 
            else: 
                if target >= nums[mid] and target <= nums[right]:
                    left = mid + 1
                else: 
                    right = mid 

        return -1    
        