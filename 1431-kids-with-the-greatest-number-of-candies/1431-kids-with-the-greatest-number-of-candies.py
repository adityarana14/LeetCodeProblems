class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_candy = max(candies)
        print(max_candy)
        answer = []

        for i in candies: 
            if i + extraCandies >= max_candy:
                answer.append(True)
            else: 
                answer.append(False)

        return answer
        