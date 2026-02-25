class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_num = { "2": "abc", "3": "def", "4": "ghi", "5": "jkl","6": "mno",
                    "7": "pqrs", "8": "tuv", "9": "wxyz" }

        res = []

        def backtrack(index, current_string):
            if len(current_string) == len(digits):
                res.append(current_string)
                return
            
            letters = phone_num[digits[index]]
        
            for letter in letters:
                backtrack(index + 1, current_string + letter)

        backtrack(0, "")
        return res