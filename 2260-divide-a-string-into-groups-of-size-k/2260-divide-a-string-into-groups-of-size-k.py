class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        length = len(s)
        answer = []

        i=0
        while i<length:
                answer.append(s[i:i+k])
                i+=k
        if len(answer[-1])!=k:
            answer[-1] += fill * (k - len(answer[-1]))
        return answer

                


        

        