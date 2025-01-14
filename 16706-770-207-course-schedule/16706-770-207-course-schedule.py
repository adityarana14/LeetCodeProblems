class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is a problem of detecting cycle in a directed graph, which we know how 
        # to solve using DFS approach 

        adj = defaultdict(list)
        visited = set()
        for course, pre in prerequisites: 
            adj[course].append(pre)

        for i in range(numCourses):
            if i not in visited: 
                res = self.detect_cycle(adj, i, set(), visited)
                if res: 
                    return False 

        return True 


    def detect_cycle(self, adj, start, curr, visited):
        if start in curr: 
            return True 
        if start in visited: 
            return False 


        curr.add(start)
        

        for nei in adj[start]:
            if self.detect_cycle(adj, nei, curr, visited):
                return True 

        curr.remove(start)
        visited.add(start) 
        return False 

        
        
         
