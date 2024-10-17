class Solution:
    def maximumSwap(self, num: int) -> int:

        str_num = str(num)
        len_num = len(str_num)
        max_till_now = [["0",0]] * len_num
        max_all = str(float("-inf"))
        

        for i in range( len_num -1, -1, -1):
            if str_num[i] > max_all: 
                max_all = str_num[i]
                max_till_now[i] = [max_all, i]
            else: 
                max_till_now[i] = max_till_now[i+1]

        for i, char in enumerate(str_num):
            if char < max_till_now[i][0]:
                idx = max_till_now[i][1]
                str_num = str_num[:i] + max_till_now[i][0] + str_num[i+1:]
                str_num = str_num[:idx] + char + str_num[idx+1:]
                break
                
        return int(str_num)