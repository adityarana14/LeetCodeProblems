class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s 

        temp_string = ""
        for i in range(numRows):
            idx = i 
            
            delta_down =  2*(numRows - i - 1) 
            delta_up = 2 * i
            
            going_down = True 
            while(idx < len(s)):
                temp_string = temp_string + s[idx]
                if i == 0:
                    idx = idx + delta_down
                    
                elif i == numRows - 1:
                    idx = idx + delta_up
                    
                else:

                    if going_down == True:
                        idx = idx + delta_down
                    else: 
                        idx = idx + delta_up
                
                    going_down = not going_down
        return temp_string


                
            
        