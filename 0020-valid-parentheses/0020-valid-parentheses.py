class Solution(object):
    def isValid(self, s):
        stack = []
        sym = {")":"(", "]":"[" , "}":"{" }
        for char in s:
            if char not in sym:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    value = stack.pop()
                    if value!= sym[char]:
                        return False
        
        if not stack:
            return True
        else:
            return False

        