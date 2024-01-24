from collections import deque 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        dict_connected = {}
        no_of_nodes = 0 
        for i in range(len(isConnected)):
            dict_connected[i+1] = []
            count = 1 
            for val in isConnected[i]:
                if count - 1  == i:
                    count = count + 1
                    continue 
                else:
                    if val == 1: 
                        dict_connected[i+1].append(count)
                        no_of_nodes += 1 
                    count = count + 1 
        print(dict_connected)
        visited = [0] * len(isConnected)
        print(visited)

        def dfs(val):
            visited[val-1] = 1 
            for k in dict_connected[val]:
                if visited[k-1] == 0: 
                    dfs(k)

        answer = 0 
        for key in dict_connected:
            if visited[key-1] == 0: 
                answer = answer + 1
                dfs(key)

        return answer

        




        

        
        