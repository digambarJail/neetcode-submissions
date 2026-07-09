class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if nums.count(0) > 1:
            return [0] * len(nums)

        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix = postfix * nums[i]
        
        return res