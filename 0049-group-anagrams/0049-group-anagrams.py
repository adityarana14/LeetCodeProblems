class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict_anagram = {}
        for val in strs: 
            
            key_dict_anagram = ''.join(sorted(val))
            
            if key_dict_anagram in dict_anagram: 
                dict_anagram[key_dict_anagram].append(val)
            else: 
                dict_anagram[key_dict_anagram] = [val]
                

        answer = []

        for key in dict_anagram: 
            answer.append(dict_anagram[key])

        return answer
            

        