class Solution:

    # def compare(self, i, j, grid_matrix, transposed_matrix):
    #     k = 0 
    #     for ele in grid_matrix[i]:
    #         if ele == transposed_matrix



    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0 
        dict_matrix = {}
        for val in grid:
            if tuple(val) in dict_matrix: 
                dict_matrix[tuple(val)] += 1 
            else: 
                dict_matrix[tuple(val)] = 0 

        transposed_matrix = list(zip(*grid))

        for val in transposed_matrix: 
            if val in dict_matrix:
                if dict_matrix[val] == 0:  
                    count = count + 1
                else: 
                    value = dict_matrix[val]
                    count = count + value + 1 


        return count 

        



        # row_sum = []
        # column_sum = []

        # transposed = list(zip(*grid))

        # for num in grid: 
        #     sum = 0 
        #     for val in num: 
        #         sum = sum + val 
        #     row_sum.append(sum)
        
        # for num in transposed:
        #     sum = 0 
        #     for val in num: 
        #         sum = sum + val 
        #     column_sum.append(sum)

        # print(row_sum)
        # print(column_sum)  
        # count = 0 

        # for i, num in row_sum:
        #     for j, val in column_sum: 
        #         if num == val:
        #             check = compare(i, j, grid, transposed) 
        #             if check == True: 
        #                 count = count + 1 
                    



        # return 1 

        