class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i>0 and flowerbed[i-1] == 1:
                continue
            if i < len(flowerbed)-1 and flowerbed[i+1] ==1:
                continue
            
            flowerbed[i] = 1
            n-=1

            if n==0:
                return True

        return n<=0

      

        