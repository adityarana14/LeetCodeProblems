class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers) - 1 
        answer = []
        while i<j: 
            sum_num = numbers[i] + numbers[j]
            if sum_num == target: 
                answer.append(i+1)
                answer.append(j+1)
                return answer
            elif sum_num > target: 
                j = j - 1 
            else: 
                i = i + 1 
        return answer

        