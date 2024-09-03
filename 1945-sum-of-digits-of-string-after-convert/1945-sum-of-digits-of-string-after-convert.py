class Solution:
    def getLucky(self, s: str, k: int) -> int:
        char_int = []

        for char in s: 
            number = ord(char)-ord("a")+1
            if number >= 10: 
                while number: 
                    temp_num = number % 10 
                    char_int.append(temp_num)
                    number = number // 10 
            else: 
                char_int.append(number)



        sum_char_int = sum(char_int)

        while (sum_char_int % 10) != sum_char_int and k - 1:

            temp_sum = 0 
            while sum_char_int: 
                temp_sum += sum_char_int % 10 
                sum_char_int = sum_char_int // 10 


            sum_char_int = temp_sum
            k = k - 1 

        return sum_char_int

