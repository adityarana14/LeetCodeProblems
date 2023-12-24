class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        flag = 1 
        while len(word1) != 0 and len(word2) != 0:
            if flag == 1: 
                answer = answer + word1[0]
                flag = 0 
                word1 = word1[1:]
            else: 
                answer = answer + word2[0]
                flag = 1 
                word2 = word2[1:]

        if len(word1) != 0:
            answer = answer + word1
        else: 
            answer = answer + word2
        return answer
        