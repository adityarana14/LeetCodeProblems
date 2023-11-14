class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        count = 0 
        subcount = 1
        for i in range(1 , len(chars)):
            if chars[i-1] == chars[i]:
                subcount += 1 
            else:
                # print(f"{subcount}   {s}.    {i}")
                if subcount > 1:
                    s = s + chars[i-1] + str(subcount)
                else:
                    s = s + chars[i-1] 

                subcount = 1
                    
        last = chars[len(chars)-1]  
        if subcount > 1:
            s = s + last + str(subcount)
        else: s = s + last
            

        chars[:] = list(s)
        print(chars)
        print(s)
        return len(s)

        