class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for i in asteroids:
            while stk and i < 0 and stk[-1]>0:
                if stk[-1] < -i:
                    stk.pop()
                    continue
                elif stk[-1] == -i:
                    stk.pop()
                break
            else:
                stk.append(i)
        return stk 

        