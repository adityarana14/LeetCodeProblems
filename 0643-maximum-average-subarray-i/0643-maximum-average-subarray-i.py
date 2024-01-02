class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        #sum of first k element sum 
        
        sum_range = 0 
        for i in range(0, k):
            sum_range = sum_range + nums[i]

        #Whose sum is more, definitely the average will be more 
        answer = sum_range 
        i = 0
        j = k - 1   
        while j != len(nums) - 1:
            j = j + 1 
            sum_range = sum_range - nums[i] + nums[j]
            if sum_range > answer: 
                answer = sum_range 
            i = i + 1 

        return answer/k



        