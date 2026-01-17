class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        post = [0]*n
        pre = [0]*n

        pre[0] = 1
        post[-1]=1

        for i in range(1,n,1):
            pre[i] = pre[i-1]* nums[i-1]
        for i in range(n-1,0,-1):
            post[i-1] = post[i] * nums[i]
        for i in range(n):
            result[i] = pre[i] * post[i]
        return result


        