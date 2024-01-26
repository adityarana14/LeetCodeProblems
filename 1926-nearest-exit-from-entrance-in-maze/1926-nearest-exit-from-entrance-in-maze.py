from collections import defaultdict 
from collections import deque 

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        row = len(maze) - 1 
        column = len(maze[0]) - 1 
        dict_neigh = defaultdict(list)

        def validPosition(i, j):
            if i>= 0 and i<= row: 
                if j>= 0 and j<= column: 
                    return True 
            return False 


        for i, val in enumerate(maze): 
            for j, v in enumerate(val):
                if v == ".":

                    # check for right 
                    check = validPosition(i, j + 1)
                    if check: 
                        if maze[i][j+1] == '.':
                            dict_neigh[(i,j)].append((i, j + 1))


                    # check for left 
                    check = validPosition(i, j - 1)
                    if check: 
                        if maze[i][j-1] == ".":
                            dict_neigh[(i,j)].append((i, j - 1))

                    # check for down 
                    check = validPosition(i + 1, j)
                    if check: 
                        if maze[i+1][j] == ".":
                            dict_neigh[(i,j)].append((i+1, j))

                    # check for up 
                    check = validPosition(i-1, j)
                    if check: 
                        if maze[i-1][j] == ".":
                            dict_neigh[(i,j)].append((i-1, j))

        # print(dict_neigh)

        def isExit(i,j):
            if i == 0 or i == row or j == 0 or j == column: 
                return True 
            return False 

        def bfs(i,j):
            if (i,j) not in dict_neigh: 
                return - 1 

            q = deque()
            visited = set()

            visited.add((i,j))
            q.append([(i,j),0])

            while q: 
                # print(f"I'm Queue {q}")
                top, level = q.popleft()
                for nei in dict_neigh[top]:
                    if nei in visited: 
                        continue
                    check = isExit(nei[0], nei[1])                   
                    if check: 
                        # print(f"I'm true {nei[0]} and {nei[1]}")
                        return level + 1 
                    else: 
                        q.append([nei, level + 1])
                        visited.add(nei)
            return -1

        return bfs(entrance[0], entrance[1])


                    

        