class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            dct[nums[i]] = i
        for i in range(len(nums)):
            value = target - nums[i]
            if value in nums:
                if nums.index(value) != i:
                    return i , nums.index(value)