class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num_set_bit = 0 

        while num2: 
            rem = num2 % 2
            num2 = num2 // 2

            if rem == 1: 
                num_set_bit += 1 

        list_num1 = []

        while num1: 
            rem = num1 % 2
            num1 = num1 // 2 

            list_num1.append(rem)

        # First Settle all the ones 
        ans_list = [0] * len(list_num1)

        for i in range(len(list_num1)-1, -1, -1):
            if list_num1[i] == 1 and num_set_bit > 0:
                num_set_bit -= 1 
                ans_list[i] = 1 

            if num_set_bit == 0: 
                break 

        if num_set_bit: 
            for i, num in enumerate(ans_list): 
                if num == 0 and num_set_bit: 
                    ans_list[i] = 1 
                    num_set_bit -= 1 

        while num_set_bit: 
            ans_list.append(1)
            num_set_bit -= 1 

        ans = 0 

        for i, num in enumerate(ans_list):
            if num == 1: 
                ans = ans + 2 ** (i)
            
        return ans 
