class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        suffix = [0]
        temp_value = 0 
        for i in range(1, len(nums)):
            temp_value = temp_value + nums[i-1]
            prefix.append(temp_value)
        temp_value = 0 
        for j in range(len(nums) - 2 , -1, -1):
            temp_value = temp_value + nums[j+1]
            suffix.append(temp_value)
        j = len(prefix) -1 
        print(prefix)
        print(suffix)
        for i, num in enumerate(prefix): 
            if num == suffix[j]:
                return i 
            j = j - 1 
            
        return -1 


