class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        count = 0 
        answer = 0 
        temp = 0 
        i = 0
        j = 0 

        while i != len(nums):
            
            if nums[i] == 0 and count < k:
                temp = temp + 1 
                count = count + 1 
            elif nums[i] == 1: 
                temp = temp + 1 
            else:
                while count >= k:
                    if  nums[j] == 0: 
                        count = count - 1 
                        temp = temp - 1 
                    else: 
                        temp = temp - 1       
                    j = j + 1 
                temp = temp + 1
                count = count + 1 
                

            if temp > answer: 
                answer = temp 
            print(f"I : {i} temp : {temp}. count : {count} j = {j}")
            i = i + 1 


        return answer








