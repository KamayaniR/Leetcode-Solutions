class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        prefix = [0] * n
        postfix = [0] * n

        prefix[0] = 1
        for i in range (1,n):
            prefix[i] = prefix[i-1] * nums[i-1]

        postfix[-1] = 1
        for i in range (n-1, 0 ,-1):
            postfix[i-1] = postfix[i] * nums[i]

        for i in range(n):
            answer[i] = postfix[i] * prefix[i]

        return answer
        



        