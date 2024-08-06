class Solution:
    def __init__(self):
        self.answer = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combGenerator(candidates, [], 0, target)
        return self.answer
        
    def combGenerator(self, candidates, output, sum_num, target):
        if sum_num == target: 
            self.answer.append(output)
            return 
        if sum_num > target: 
            return 
        if not candidates: 
            return 
        
        output_copy = output.copy()
        output_copy.append(candidates[0]) 

        self.combGenerator(candidates[:], output_copy, sum_num + candidates[0], target) 
        self.combGenerator(candidates[1:], output.copy(), sum_num, target) 

        return 