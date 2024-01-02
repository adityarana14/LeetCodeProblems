class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        temp_length = 0 
        answer = 0 
        j = 0 
        count = 0 
        k = 0 
        while j != len(nums):
            if nums[j] == 1: 
                temp_length = temp_length + 1 
            elif nums[j] == 0 and count == 0: 
                count = count + 1 
            else: 
                while count > 0:
                    if nums[k] == 0:
                        count = count - 1
                        
                    temp_length -= 1
                    k = k + 1 
                count = count + 1 
                temp_length = temp_length + 1 
            if temp_length > answer: 
                answer = temp_length 
        
            j = j + 1 

        if count == 0: 
            return answer - 1 
        return answer
        