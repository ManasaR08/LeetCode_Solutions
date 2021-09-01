class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max = 1
        visited = [0]*len(nums)
        for i in range(len(nums)):
            count = 0
            while not visited[i]:
                visited[i] = 1
                i = nums[i]
                count = count+1
            if count > max:
                max = count
        return max
            