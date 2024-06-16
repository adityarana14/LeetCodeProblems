class Solution:

    def binary_search(self, list_matrix, target):
        left = 0 
        right = len(list_matrix) - 1 

        while left <= right: 
            mid = (left + right) // 2 
            if list_matrix[mid] > target: 
                right = mid - 1 
            elif list_matrix[mid] < target: 
                left = mid + 1 
            else: 
                return True 
        return False 

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[len(matrix)-1][len(matrix[0])-1]:
            return False 

        rows = len(matrix) - 1 
        cols = len(matrix[0]) - 1

        top = 0 
        bottom = len(matrix) - 1

        while top <= bottom: 
            mid = (top + bottom) // 2

            if target > matrix[mid][0]:
                if target <= matrix[mid][cols]:
                    bool_answer = self.binary_search(matrix[mid], target)
                    if bool_answer == True: 
                        return True
                    else: 
                        return False 
                else: 
                    top = mid + 1 
            elif target < matrix[mid][0]:
                bottom = mid - 1 
            else: 
                return True 

        return False  