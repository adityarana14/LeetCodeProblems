class Solution:
    def intToRoman(self, num: int) -> str:
        st = ""
        st = self.process(st, "M", "*", "*", num // 1000)
        num = num % 1000

        # print(st)

        st = self.process(st, "C", "D", "M", num // 100)
        num = num % 100 

        # print(st)


        st = self.process(st, "X", "L", "C", num // 10)
        num = num % 10 

        # print(st)


        st = self.process(st, "I", "V", "X", num)


        # print(st)
        return st 
        
        


    def process(self, s, minor, mid, major, number):
        if number <= 3: 
            for i in range(number):
                s = s + minor

        elif number < 5: 
            s = s + minor + mid

        elif number == 5: 
            s = s + mid 

        elif number <= 8: 
            s = s + mid 
            for i in range(6,number + 1):
                s = s + minor 

        elif number == 9:
            s = s + minor + major 

        else: 
            s = s + major 

        return s 