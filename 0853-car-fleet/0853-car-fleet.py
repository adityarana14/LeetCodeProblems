from collections import deque 
class Solution:
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        return self.car_fleet(target, position, speed)
    
    def car_fleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet_sorted_info = sorted([(x,y) for x, y in zip(position, speed)], reverse = True)
        stack_fleet = deque()

        for pos, sp in fleet_sorted_info: 
            distance = target - pos
            time = distance / sp

            if not stack_fleet: 
                stack_fleet.append(time)
            else: 
                if stack_fleet[-1] < time: 
                    stack_fleet.append(time)

        return len(stack_fleet)



        return 1 
    
        