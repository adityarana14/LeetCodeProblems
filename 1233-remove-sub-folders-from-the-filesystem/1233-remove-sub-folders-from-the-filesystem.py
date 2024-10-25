class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        set_base = set()

        for path in folder: 
            if path not in set_base:
                # print("This is path", path)
                contains = False
                for i in range(len(path)-1,1,-1):
                    if path[i] == "/":
                        sub_path = path[:i]
                        # print(sub_path)
                        if sub_path in set_base: 
                            contains = True 
                            break
                if not contains:
                    set_base.add(path)
            
        # print(set_base)

        return list(set_base)