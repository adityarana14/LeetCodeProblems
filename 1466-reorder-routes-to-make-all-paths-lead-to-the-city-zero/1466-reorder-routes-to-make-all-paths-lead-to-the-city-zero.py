from collections import defaultdict
from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        answer = 0 
        incoming = defaultdict(list)
        outgoing = defaultdict(list)
        queue = deque()
        visited = [0] * n 

        [incoming[val[1]].append(val[0]) for val in connections]
        [outgoing[val[0]].append(val[1])for val in connections]

        # print(incoming)
        # print(outgoing)

        queue.append(0)
        visited[0] = 1 

        while queue: 
            top = queue.popleft()
            if top in outgoing: 
                for val in outgoing[top]:
                    if visited[val] == 0:
                        answer = answer + 1 
                        visited[val] = 1 
                        queue.append(val)
            if top in incoming: 
                for val in incoming[top]:
                    if visited[val] == 0: 
                        visited[val] = 1 
                        queue.append(val)

        return answer