from collections import deque 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_position_with_speed = sorted([(x,y) for x , y in zip(position,speed)],reverse = True)
        stack = deque()
        # print(sorted_position_with_speed)
        for key, val in sorted_position_with_speed:
            distance = target - key
            time_taken = distance / val
            # print(f"time taken {time_taken} distance {distance}. val {val} key {key}")
            if not stack:
                stack.append(time_taken)
            else: 
                if stack[-1] < time_taken:
                    stack.append(time_taken)

        # print(stack)
        return len(stack) 



        