class NumArray:

    def __init__(self, nums: List[int]):
        self.cummulative = nums[:]
        for i in range(1,len(self.cummulative)):
            self.cummulative[i] = self.cummulative[i-1] + nums[i]
        
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.cummulative[right]
        else:
            return self.cummulative[right] - self.cummulative[left-1]
            
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)