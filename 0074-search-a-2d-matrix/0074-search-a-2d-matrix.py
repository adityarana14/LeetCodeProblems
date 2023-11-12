class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        col = len(matrix[0]) - 1
        for i in range(len(matrix)):

            if(target <= matrix[i][col]):
                start = 0
                end = col
                
                while(start <= end):
                    mid = (start + end ) // 2
                    if(target == matrix[i][mid]):
                        return True

                    if(target > matrix[i][mid]):
                        start = mid + 1 
                    else: end = mid - 1


        return False            


                        
            

        