from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.time_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        #if self.time_dict[key][value] < timestamp:
        self.time_dict[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        # print(self.time_dict[key][0])
        #print(f"We are at timestamp {timestamp}")
        if key in self.time_dict:
            left = 0 
            right = len(self.time_dict[key]) - 1 
            temp_res = ""
            while left <= right: 
                mid = (left + right) // 2 

                if self.time_dict[key][mid][0] == timestamp: 
                    return self.time_dict[key][mid][1]

                if left == right: 
                    if self.time_dict[key][mid][0] < timestamp: 
                        return self.time_dict[key][mid][1]
                    else: 
                        # if temp_res != "":
                        #     return temp_res
                        # else: return ""
                        return temp_res

                if self.time_dict[key][mid][0] > timestamp:
                    right = mid - 1
                else: 
                    temp_res = self.time_dict[key][mid][1]
                    left = mid + 1 

            return temp_res
        else: 
            return ""


        # if key in self.time_dict:
        #     size = len(self.time_dict[key])
        #     sub_keys = []
        #     for val in self.time_dict[key]: 
        #         sub_keys.append(val)
                
        #     left = 0 
        #     right = size 

        #     if timestamp < sub_keys[left]:
        #         return ""

        #     while left <= right: 
        #         mid = (left + right) // 2 

        #         if left == mid: 
        #             return self.time_dict[key][sub_keys[left]]  

        #         if left == right: 
        #             return self.time_dict[key][sub_keys[mid]]

        #         if sub_keys[mid] == timestamp: 
        #             return self.time_dict[key][sub_keys[mid]]

        #         if sub_keys[mid] > timestamp: 
        #             right = mid - 1 
        #         else: 
        #             left = mid 

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)