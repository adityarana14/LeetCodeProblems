from collections import defaultdict
from collections import deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        answer = []

        for i, val in enumerate(equations):
            graph[val[0]].append([val[1],values[i]])
            graph[val[1]].append([val[0],1/values[i]])
 
        def bfs(source, target):
            
            if source not in graph or target not in graph: 
                return -1 
            

            visited = set()
            q = deque()
            q.append([source, 1])
            visited.add(source)

            while q:
                nei, w  = q.popleft()
                if nei == target: 
                    return w
                
                for val, weight in graph[nei]:
                    if val not in visited:
                        visited.add(val)
                        q.append([val, w*weight])

            return -1 

        for val in queries: 
            answer.append(bfs(val[0], val[1]))

        return answer

        