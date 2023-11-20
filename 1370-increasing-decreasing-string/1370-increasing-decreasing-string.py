

class Solution:
    def sortString(self, s: str) -> str:
        
        # count the frequency of elements are there in the string 
        s_dictionary = {}
        flag = 0
        final_string = ""

        for i in range(len(s)):
            s_dictionary[s[i]] = 0


        for i in range(len(s)):
            s_dictionary[s[i]] += 1 

        print(s_dictionary)

        # Dictionary Traversal

        while self.sumOfKeysValue(s_dictionary) != 0:
            
            if flag == 0:
                temp_array = []
                for key in s_dictionary:
                    
                    if s_dictionary[key] != 0:
                        temp_array.append(key)
                        temp_array.sort()                      
                        s_dictionary[key] -= 1
                    
                final_string += ''.join(temp_array)
                flag = 1 
            else: 
                temp_string = ""
                temp_array = []
                for keys in s_dictionary:
                    if s_dictionary[keys] != 0:
                        temp_array.append(keys)
                        temp_array.sort(reverse = True)
                        s_dictionary[keys] -= 1
                
                flag = 0
                
                final_string = final_string + ''.join(temp_array)

        print("This is the final string:"+final_string)
        return final_string
    

    def sumOfKeysValue(self, dict_string):
        count = 0 
        for keys in dict_string:
            count = count + dict_string[keys]
        
        return count 