class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        r= {}

        for char in s:
            if char in r:
                r[char] +=1
            else:
                r[char] = 1
            if r[char] % 2 ==1:
                count+=1
            else:
                count -=1
            
        if count>1:
            return len(s) - count +1
        return len(s)
        