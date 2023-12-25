class Solution:
    def reverseVowels(self, s: str) -> str:
        string_array = []
        string_s = []
        vowel_array = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in s: 
            string_s.append(i)
            if i in vowel_array:
                string_array.append(i)

        k = len(string_array) - 1 
        j = 0 

        print(string_s)
        print(string_array)
        for i in string_s:
            if i in vowel_array: 
                string_s[j] = string_array[k]
                k = k - 1  
            j = j + 1 

        answer = "" 
        for i in string_s:
            answer = answer + i

        
        return answer
