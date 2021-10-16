class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = 0
        current = 0
        for i in range(len(nums)):
            current += nums[i]
            if current > maxi:
                maxi = current
            if current < 0:
                current = 0
        if max(nums) < 0:
            return max(nums)
        return maxi