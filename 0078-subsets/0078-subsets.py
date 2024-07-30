class Solution:
    def __init__(self):
        self.answer = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.input_output_method(nums, [])
        return self.answer
        
    def input_output_method(self, inputs, outputs):

        if len(inputs) == 0: 
            self.answer.append(outputs)
            return

        # self.input_output_method(inputs[1:], outputs.copy())
        # self.input_output_method(inputs[1:], outputs.copy() + [inputs[0]])

        outputs_with_current = outputs.copy()
        outputs_with_current.append(inputs[0])

        self.input_output_method(inputs[1:], outputs.copy())
        self.input_output_method(inputs[1:], outputs_with_current)