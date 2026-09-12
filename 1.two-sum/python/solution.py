import math
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums[i+1:]:
                return [i,nums.index(target - nums[i],i+1)]
