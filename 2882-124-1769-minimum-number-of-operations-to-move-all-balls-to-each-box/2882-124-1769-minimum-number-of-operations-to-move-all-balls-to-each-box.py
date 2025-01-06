class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        set_store = set()
        ans = []
        for i, char in enumerate(boxes): 
            if char == "1": 
                set_store.add(i)

        for i, char in enumerate(boxes): 
            temp_ans = 0 
            for ele in set_store: 
                if ele != i: 
                    temp_ans += abs(ele - i)

            ans.append(temp_ans)

        return ans 




            

        