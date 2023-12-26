class Solution:
    def reverseWords(self, s: str) -> str:
        # list_words = []
        # answer = ""
        # i = 0 
        # while i <= len(s) - 1:
        #     temp_word = ""
        #     if s[i] != ' ':
        #         while  i <= len(s) - 1 and s[i] != ' ':
        #             temp_word = temp_word + s[i]
        #             i = i + 1 
        #     else: 
        #         i = i + 1 
        #     if temp_word != "":
        #         list_words.append(temp_word)
            
                    
        # # print(list_words)
        # for i in range(len(list_words)-1 , -1 , -1):
        #     answer = answer + list_words[i]
        #     if i != 0:
        #         answer = answer + " "

        check = s.split()
        print(check)
        check = check[::-1]
        print(check)
        answer = " ".join(check)
        return answer
        