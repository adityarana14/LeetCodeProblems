class Solution:
    def findComplement(self, num: int) -> int:
        list_binary = []
        i = 0 
        answer = 0 

        while num: 
            remainder = num % 2 
            list_binary.append(remainder)
            num = num // 2 
        
        
        for list_val in list_binary: 
            if list_val == 0: 
                answer = answer + 2**i

            i = i + 1 

        return answer

        