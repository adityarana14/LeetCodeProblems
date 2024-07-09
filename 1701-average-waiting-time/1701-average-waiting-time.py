class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        
        current_waiting_time = 0 
        now_time = 0 

        for customer in customers:

            arrival_time = customer[0]
            time_needed = customer[1]
            
            if now_time < arrival_time: 
                current_waiting_time += time_needed
                now_time = arrival_time + time_needed - 1

            elif now_time == arrival_time: 
                current_waiting_time += time_needed + 1 
                now_time +=  time_needed 

            else: 
                current_waiting_time += time_needed + (now_time - arrival_time ) + 1
                now_time += time_needed 

        return current_waiting_time / len(customers)
        