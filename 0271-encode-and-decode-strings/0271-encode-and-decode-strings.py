class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        
        for string in strs:
            encoded_string.append(str(len(string)) + '#' + string)
            
        return ''.join(encoded_string)
        
    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        
        while i < len(s):
            j = i
            
            while s[j] != '#':
                j += 1
            
            n = int(s[i : j])
            j += 1
            
            decoded_strings.append(s[j : j + n])
            i = j + n
            
        return decoded_strings