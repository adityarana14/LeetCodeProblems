class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1: 
            if flowerbed[0] == 0 :
                n = n - 1 
        else: 
            for i in range(len(flowerbed) - 1):
                #first 
                if flowerbed[i] == 0 and flowerbed[i+1] == 0 and i == 0:         
                    n = n - 1
                    flowerbed[i] = 1 
                elif flowerbed[i-1] == 0 and flowerbed[i + 1 ]  == 0 and flowerbed[i] == 0 and i!= len(flowerbed) -1:
                    n = n - 1
                    flowerbed[i] = 1
                elif i == len(flowerbed) - 2 and flowerbed[i+1] == 0 and flowerbed[i] == 0 :
                    n = n - 1

        
        if n > 0:
            return False
        else: 
            return True
     


